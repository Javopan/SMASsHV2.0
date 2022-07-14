from PyQt6.QtWidgets import QWidget, QHeaderView, QDialog, QFileDialog
from PyQt6.QtCore import QThreadPool
from gui.Smassh import Ui_wdg_smash
from gui.IpRange_Dialog import Ui_Dialog
from Models.smash_model import SmashModel
from funciones.smassh_process import generate_ip_range, SshWorker
from os import path
from funciones.pyqt_functions import open_dialog
import sys


class Smassh(QWidget, Ui_wdg_smash):
    def __init__(self, parent):
        super(Smassh, self).__init__(parent)
        self.setupUi(self)
        self.smash_model = SmashModel()
        self.tbl_smash_view.setModel(self.smash_model)
        self.tbl_smash_view.resizeColumnsToContents()
        self.smashing = False
        self.thread_manager = QThreadPool()

        # Alternating colors
        self.tbl_smash_view.setAlternatingRowColors(True)

        # enable modification

        # setting the cloumn sizes
        self.tbl_smash_view.setColumnWidth(0, 50)  # ID
        self.tbl_smash_view.hideColumn(0)
        self.tbl_smash_view.setColumnWidth(1, 40)  # Running
        self.tbl_smash_view.setColumnWidth(2, 130)  # IP
        self.tbl_smash_view.setColumnWidth(3, 60)  # USER
        self.tbl_smash_view.setColumnWidth(4, 60)  # PASS
        self.tbl_smash_view.setColumnWidth(5, 60)  # REPS
        self.tbl_smash_view.setColumnWidth(6, 60)  # REM
        self.tbl_smash_view.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)

        # agregar uso de botones
        self.btn_add_node.clicked.connect(self.agrega_renglon)
        self.btn_remove_node.clicked.connect(self.remover_renglon)
        self.btn_smash.clicked.connect(self.smash)
        self.btn_duplicate_line.clicked.connect(self.duplicate_lines)
        self.btn_ip_range.clicked.connect(self.ip_range)
        self.tbl_smash_view.doubleClicked.connect(self.stop_smash)
        self.btn_save_results.clicked.connect(self.save_smash)
        self.btn_load_file.clicked.connect(self.load_smash)

    def agrega_renglon(self):
        # agrega un renglón vacio a través de una funcion del modelo
        self.smash_model.add_row_empty()
        self.smash_model.layoutChanged.emit()

    def remover_renglon(self):
        # remueve el renglon seleccionado o el último renglón
        index_to_remove = self.tbl_smash_view.selectedIndexes()
        self.smash_model.remove_row(index_to_remove)
        self.smash_model.layoutChanged.emit()
        self.tbl_smash_view.clearSelection()

    def stop_smash(self, index):
        if index.column() == 1:
            w_id = self.smash_model.get_worget_id(index.row())
            if '-' not in w_id:
                SshWorker.stop_worker(w_id, SshWorker.running_workers)
                self.smash_model.stop(w_id)
        if len(SshWorker.running_workers) == 0:
            self.btn_smash.setText('SMASH')
            self.smashing = False

    def smash(self):
        if not self.smashing:
            if self.smash_model.is_empty()[0] > 0:
                self.btn_smash.setText('Stop SMASH')
                self.smashing = True
                self.smash_model.updaing = True
                self.thread_manager.setMaxThreadCount(self.spn_threads.value())
                self.smash_model.clean_answers()
                for row in self.smash_model.instruction_df.iterrows():
                    # set remaining reps to the amount of reps in the model
                    worker_id = row[1]['ID']
                    if '-' not in worker_id:
                        self.smash_model.set_remaining(row[1]['ID'])
                        reps = int(row[1]['Reps']) if row[1]['Reps'] != '' else 0
                        worker = SshWorker(worker_id,
                                           row[1]['IP'],
                                           row[1]['User'],
                                           row[1]['Pass'],
                                           self.spn_port.value(),
                                           self.spn_timeout.value(),
                                           self.spn_wait_buffer.value(),
                                           reps,
                                           row[1]['Commands'])
                        worker.signals.answer_signal.connect(self.smash_model.add_answer)
                        worker.signals.status_signal.connect(self.status_messages)
                        worker.signals.loop_signal.connect(self.smash_model.reduce_element)
                        worker.signals.start_signal.connect(self.smash_model.running)
                        worker.signals.stop_signal.connect(self.smash_model.stop)
                        worker.signals.stop_signal.connect(self.stop_smash_all)
                        self.thread_manager.start(worker)
        elif self.smashing:
            self.btn_smash.setText('SMASH')
            self.smashing = False
            self.smash_model.updaing = False
            self.smash_model.stop_all()
            SshWorker.stop_all(SshWorker.running_workers)

    def stop_smash_all(self, work_id):
        if self.thread_manager.activeThreadCount() == 0:
            self.btn_smash.setText('SMASH')
            self.smashing = False
            self.smash_model.updaing = False

    def print_smash(self):
        print(self.smash_model.instruction_df)

    def status_messages(self, w_id, slot, message):
        self.parent().status_bar.showMessage(f'W{w_id}-S{slot} - {message}')

    def duplicate_lines(self):
        indexes = []
        for line in self.tbl_smash_view.selectedIndexes():
            indexes.append(line.row())
        self.smash_model.duplicate_line(set(indexes))  # we use set to remove duplicates
        self.smash_model.layoutChanged.emit()

    def ip_range(self):
        dialog = IpRangeDialog(self)
        if dialog.exec():
            ip_s, ip_e, ip_reps, ip_com, ip_us, ip_pa = dialog.get_values()
            ips = generate_ip_range(ip_s, ip_e)
            for ip in ips:
                self.smash_model.add_row('n', ip, ip_us, ip_pa, ip_reps, '', ip_com)
            self.smash_model.layoutChanged.emit()

    def save_smash(self):
        if not self.smash_model.updaing:
            save_path = QFileDialog.getSaveFileName(self, 'Save File Name...', path.dirname(sys.executable), '*.xlsx')
            path_ = save_path[0]
            if path_ != '':
                self.smash_model.save_model(path_)

    def load_smash(self):
        if not self.smash_model.updaing:
            file_load = open_dialog(self.parent(), '*.xlsx', multi_select=None)
            if file_load:
                self.smash_model.read_model(file_load[0])


class IpRangeDialog(QDialog):
    """IP Range Dialog"""
    def __init__(self, parent=None):
        super(IpRangeDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def get_values(self):
        return [self.ui.txt_ip_start.text(),
                self.ui.txt_ip_end.text(),
                self.ui.txt_reps.text(),
                self.ui.txt_commands.text(),
                self.ui.txt_user.text(),
                self.ui.txt_pass.text()]