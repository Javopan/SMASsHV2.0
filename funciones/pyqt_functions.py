import pandas as pd
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QFileDialog, QListWidgetItem
from PyQt6.QtCore import QRunnable, pyqtSignal, pyqtSlot, QObject


class WorkerSignals(QObject):
    # will signal a progress bar a number between 1 and 100
    signal_progress = pyqtSignal(int)
    # to return values via a signal. It might be any value
    signal_result_matrix_calculation = pyqtSignal(pd.DataFrame, dict, int, int)


class Worker(QRunnable):
    """
    This class will work as a container for multi threading for some long processes. It will get the
    fuction to multi thread and execute it
    """

    def __init__(self, function, *args):
        super(Worker, self).__init__()
        self.function = function
        self.parameters = args
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        if self.function.__name__ == 'calculate_matrix':
            dict_links, df_all_links, pops, targets = self.function(self.parameters[0], self.parameters[1],
                                                                    self.parameters[2])
            self.signals.signal_result_matrix_calculation.emit(dict_links, df_all_links, pops, targets)


def define_action(icon, name, tooltip, trigger, shortcut=None, parent=None):
    """
    Defines an action to the toolbar
    :param shortcut: str, shortcut that we want to use, e.g. "Ctrl+o"
    :param icon: str, path to an icon file e.g. icons/open.svg
    :param name: str, name of the action e.g. Open...
    :param tooltip: str, tooltip of the action e.g. opens a file
    :param trigger: function, function that the action will trigger e.g. open_file (withoout the ())
    :param parent: object, parent of the action
    :return: object, returns a pyqt action
    """
    # Open action
    if icon is not None:  # if we have a icon
        action = QAction(QIcon(icon), name, parent)  # Creates the Action
    else:  # create the action without icon. Prints the name
        action = QAction(name, parent)
    action.setToolTip(tooltip)  # Sets a tooltip
    action.setStatusTip(action.toolTip())  # Sets the tooltip to the status bar
    action.triggered.connect(trigger)  # What the action triggers

    if shortcut:
        action.setShortcut(QKeySequence(shortcut))

    return action


def open_dialog(parent, filter_, multi_select=None):
    if multi_select:
        pass
    else:
        dlg_open = QFileDialog(caption=f'Open file for {parent.apps[parent.appowner]}', filter=f'{filter_}',
                               directory=parent.last_path)
        dlg_open.exec()
        n_files = len(dlg_open.selectedFiles())
        files = dlg_open.selectedFiles()

    if files:
        parent.last_path = files[0][:files[0].rfind('/')]
    return files


def log_message(log_widget, message):
    message_item = QListWidgetItem(message)
    log_widget.insertItem(0, message_item)
