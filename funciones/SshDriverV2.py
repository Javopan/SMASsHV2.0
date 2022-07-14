import socket
import paramiko
import time
from PyQt6 import QtCore as Qtc


class SikluSsh(Qtc.QObject):
    siklussh_error = Qtc.pyqtSignal(str)  # string with errors
    siklussh_logs = Qtc.pyqtSignal(str)  # string with log information is needed
    siklussh_messages = Qtc.pyqtSignal(bytes)  # string with the answer from the command
    siklussh_messages_decoded = Qtc.pyqtSignal(list)  # list of decoded message the same as return
    """
    This class will use the default parameters of the radio from siklu
    """
    def __init__(self, ip='192.168.0.1', username='admin', password='admin', port=22, timeout=5, wait_for_buffer=0.1,
                 addpolicy=True):

        super(SikluSsh, self).__init__()  # constructor to call the Qtc.QObject

        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.wait_for_buffer = wait_for_buffer
        self.ssh = None
        self.addpolicy = addpolicy
        self.channel = None
        self.command = None

    def connect(self, tg=False):
        """
        Creates a connection with the given parameters via a SSH Shell.
        By default it will auto add keys
        :return:
        """
        self.ssh = paramiko.SSHClient()
        if self.addpolicy:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(self.ip, port=self.port, username=self.username, password=self.password,
                             timeout=self.timeout)
        except paramiko.AuthenticationException:
            self.siklussh_error.emit(f'Unable to connect. Autentication error! Please check that the username and '
                                     f'password are correct.')
            return False  # return connection was not successful
        except (TimeoutError, socket.timeout):
            self.siklussh_error.emit(f'Unable to connect. We could not reach the desired unit after {self.timeout}'
                                     f' seconds. Please make sure the unit is online.')
            return False
        except ConnectionResetError:
            self.siklussh_error.emit(f'The connection was closed by the remote host, check that it is abailable or'
                                     f'reduce the number of connections.')
            return False
        try:
            # height and width set the size in lines and chars of the shell we summon
            self.channel = self.ssh.invoke_shell(height=10000, width=255)
        except paramiko.ChannelException as e:
            self.siklussh_error.emit(f'Unable to create a command channel. Make sure the unit is online.')
        self.siklussh_logs.emit(f'Connection was a success and the ssh shell channel established')
        return True  # Connection was a success and we have a shell invoked

    def send_command(self, command_, emit=False):
        """
        This fuction will send the commands to the radio via SSH shell.
        We will get the result in the in the same channel in the in_buffer as bytes
        We also have to wait until the in_buffer gets some information or until the
        timeout happens and break the connection
        :param emit: bool, if emit is yes, we will send the signal
        :param command_: str, command to send
        Command will be the command to execute.
        :return:
        """
        # send the command to the shell
        self.command = command_
        self.channel.send(command_ + '\n')
        self.siklussh_logs.emit('Command sent')
        # start counting time to wait for an answer
        start = time.time()

        while len(self.channel.in_buffer) == 0 and time.time() < start + self.timeout:
            # wait until time out or buffer size is bigger than 0
            time.sleep(self.wait_for_buffer)
        # get the size of the buffer
        buffer_size = len(self.channel.in_buffer)
        # if the size is bigger than 0 it means we have something on the buffer
        if buffer_size > 0:  # If the buffer has something
            buffer_size = len(self.channel.in_buffer)
            time.sleep(self.wait_for_buffer)
            # while the buffer increases we wait
            while len(self.channel.in_buffer) > buffer_size:  # we will check that the buffer will be static
                buffer_size = len(self.channel.in_buffer)
                time.sleep(self.wait_for_buffer)
            # buffer = self.channel.in_buffer._buffer
            # return what we have on the buffer
            answer = self.channel.in_buffer.read(len(self.channel.in_buffer))
            if emit:
                self.siklussh_messages.emit(answer)
                self.siklussh_messages_decoded.emit(self.process_text(answer))
            return answer
        return None

    def close(self):
        try:
            self.ssh.close()
        except:
            self.siklussh_error.emit('Could not close the connection. It was already closed or something '
                                     'was wrong')

    def process_text(self, answer_):
        if answer_:
            text = answer_.decode()
            text_tokens = text.split('\r\n')
            answer_ = []
            for token in text_tokens:
                if token == self.command or token == '' or '>' in token or '#' in token:
                    continue
                answer_.append(token.strip())
            return answer_
        return []


#### testing
if __name__ == '__main__':

    siklu_conn = SikluSsh()  # using the default parameters
    if siklu_conn.connect():
        answer = siklu_conn.send_command('show system')
        if answer:
            print('\n'.join(siklu_conn.process_text(answer)))
        siklu_conn.close()

