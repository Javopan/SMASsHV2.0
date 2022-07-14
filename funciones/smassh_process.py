from PyQt6.QtCore import pyqtSignal, QRunnable, QObject
from funciones.SshDriverV2 import SikluSsh


class WorkerSignals(QObject):
    """Defines all the signals that we will use"""
    # signal for the information we need to send
    answer_signal = pyqtSignal(str, str, str)
    error_signal = pyqtSignal(str, str, str)
    status_signal = pyqtSignal(str, str, str)
    connect_signal = pyqtSignal(bool)
    loop_signal = pyqtSignal(str, int)
    start_signal = pyqtSignal(str)
    stop_signal = pyqtSignal(str)


# thread for each process of pooling many times
class SshWorker(QRunnable):

    # list of running workers so that we can interact with them and stop them
    running_workers = []

    def __init__(self, worker_id, ip, username, password, port, timeout, wait_for_buffer, reps, commands, split=';'):
        # contructor
        super(SshWorker, self).__init__()

        self.signals = WorkerSignals()

        self.ip = ip
        self.user = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.buffer = wait_for_buffer
        self.reps = reps
        self.commands = commands
        self.worker_id = worker_id  # id of the worker this needs to be unique
        self.flag_stop = False  # flag to stop the process

        self.setAutoDelete(True)

        self.split_commands(split)

    def split_commands(self, split):
        """
        splits the commands in a list of commands
        :return:
        """
        split_commands = []
        for token in self.commands.split(split):
            if token:
                split_commands.append(token)

        self.commands = split_commands

    def run(self):
        """
        Executes a connection and a worker and sends commands for X repetitions and x commands
        :return:
        """
        siklu = SikluSsh(self.ip, self.user, self.password, self.port, self.timeout, self.buffer)
        if siklu.connect():
            self.signals.start_signal.emit(self.worker_id)
            self.signals.status_signal.emit(self.worker_id, '0', f'Connected to host {self.ip}')
            self.signals.connect_signal.emit(True)
            self.running_workers.append(self)
            for rep in range(self.reps):  # loops the repetition
                if not self.flag_stop:
                    for ij, command in enumerate(self.commands):  # loops the commands
                        answer = siklu.send_command(command, emit=False)
                        if answer:
                            answer = siklu.process_text(answer)  # this gives us a list
                            answer_line = self.tg_answers_process(answer, '{', '}', '\t', ';')
                            self.signals.answer_signal.emit(self.worker_id, f'{ij}', answer_line)
                        else:
                            self.signals.answer_signal.emit(self.worker_id, f'{ij}', 'No answer from host...')
                        # signal to decrement the remaining loops
                        if ij == 0:
                            self.signals.loop_signal.emit(self.worker_id, 1)
        self.signals.stop_signal.emit(self.worker_id)
        siklu.close()

    @staticmethod
    def stop_worker(stop_id, workers):
        # stops a worker with know id
        if workers:
            stopped_id = None
            for ii, worker in enumerate(workers):
                if worker.worker_id == stop_id:
                    worker.flag_stop = True
                    stopped_id = ii
                    break
            pop_item = workers.pop(stopped_id)
            del pop_item

    @staticmethod
    def stop_all(workers):
        # stops all workers
        for worker in workers:
            worker.flag_stop = True

        for worker in range(len(workers)):
            pop_item = workers.pop(0)
            del pop_item

    @staticmethod
    def tg_answers_process(answer, op, cl, separator, line_split):
        """
        Does pretty print for a string of character it will use tabs
        from: <hola<como<te va>>>
        to:
            hola
                como
                    te va
        it will count the number of open and close characters to create the exit
        :param answer: str, string of characters
        :param op: str, opening character eg. < { (, etc
        :param cl: str, closing character eg. > } ), etc
        :param separator: str, control character that will be added
        :param line_split: str, sontrol character to split lines inside op's and cl's
        :return: formatted answer
        """
        multiplier = 0
        last = 0
        output = ''
        answer_line = ''.join(answer)
        if op in answer_line:
            for index, char in enumerate(answer_line):
                if char == op:
                    multiplier += 1
                    output += answer_line[last: index]
                    output += '\n' + separator * multiplier
                    last = index + 1
                elif char == cl:
                    output += answer_line[last: index]
                    multiplier -= 1
                    output += '\n' + separator * multiplier
                    last = index + 1
                elif char == ';':
                    output += answer_line[last: index]
                    output += '\n' + separator * multiplier
                    last = index + 1
        else:
            output = '\n'.join(answer)
        return output


def generate_ip_range(ip_start, ip_end):
    start_range = int(ip_start[ip_start.rfind('.') + 1:])
    end_range = int(ip_end[ip_end.rfind('.') + 1:])
    ips = []
    for i in range(start_range, end_range + 1):
        ips.append(f'{ip_start[:ip_start.rfind(".") + 1]}{i}')
    return ips

# test
# if __name__ == '__main__':
#     from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel
#     import sys
#     import time
#
#
#     class MainWindow(QMainWindow):
#         def __init__(self):
#             super(MainWindow, self).__init__()
#             welcome_message = QLabel('Hola Javi')
#             self.setCentralWidget(welcome_message)
#
#         def createworkers(self):
#             self.worker_1 = SshWorker(1, '192.168.0.1', 'admin', 'admin', 22, 10, 0.2, 100, 'show system name;show rf tx-power')
#             self.worker_2 = SshWorker(2, '192.168.0.1', 'admin', 'admin', 22, 10, 0.2, 50, 'show system uptime;show rf-debug cinr;')
#
#             self.worker_1.answer_signal.connect(self.print_message)
#             self.worker_2.answer_signal.connect(self.print_message)
#
#             print('starting worker 1')
#             self.worker_1.start()
#             print('starting worker 2')
#             self.worker_2.start()
#
#         def print_message(self, worker_id, slot, answer):
#             print(f'w:{worker_id} s:{slot} a:{"".join(answer)}')
#
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#     window = MainWindow()
#     window.show()
#     window.createworkers()
#     time.sleep(1)
#     print(SshWorker.running_workers)
#     time.sleep(1)
#     SshWorker.stop_all(SshWorker.running_workers)
#     print(SshWorker.running_workers)
#     sys.exit(app.exec())