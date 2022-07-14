from PyQt6.QtWidgets import QMainWindow, QToolBar, QStatusBar, QMenu
from PyQt6.QtGui import QContextMenuEvent
from funciones.pyqt_functions import define_action, open_dialog
from gui.licensing import Licensing
from gui.smassh_ import Smassh

import sys
import os


class MainWindow(QMainWindow):
    apps = {
        0: 'empty',
        1: 'licensing',
        2: 'coordinates transform',
        3: 'matrix calculator',
        4: 'smash'
    }

    def __init__(self):
        super(MainWindow, self).__init__()

        self.appowner = 0

        self.setup_ui()
        self.set_toolbars_and_menus()

        welcome_message = Licensing(button=True)
        self.appowner = 1

        self.last_path = os.path.dirname(sys.executable)

        self.setCentralWidget(welcome_message)
        welcome_message.psig_aceptado.connect(self.change_widget_default)

        # # ##############################Statusbar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)


    def set_toolbars_and_menus(self):
        """
        Create the toolbars of the application
        :return:
        """
        # #################################### Toolbar#######################################
        toolbar = QToolBar('Main toolbar')
        self.addToolBar(toolbar)
        # #################################### File Menu#####################################
        menu = self.menuBar()
        menu_file = menu.addMenu("&File")
        menu_apps = menu.addMenu("&Applications")
        menu_help = menu.addMenu("Help")
        # #################################### Actions#######################################
        # Open Action
        icon = './icons/open-outline.svg'
        name = '&Open...'
        tooltip = 'Opens a file.'
        shortcut = 'Ctrl+o'
        action = define_action(icon, name, tooltip, self.on_open_click, shortcut, self)
        toolbar.addAction(action)
        menu_file.addAction(action)
        # Save Action
        icon = './icons/save-outline.svg'
        name = '&Save...'
        tooltip = 'Saved the file you are currently working on'
        shortcut = 'Ctrl+s'
        action = define_action(icon, name, tooltip, self.on_save_click, shortcut, self)
        toolbar.addAction(action)
        menu_file.addAction(action)

        # ------------------------------------------
        menu_file.addSeparator()
        # ------------------------------------------

        # Print Action
        icon = './icons/print-outline.svg'
        name = '&Print'
        tooltip = 'Print the current app if printable'
        shortcut = 'Ctrl+p'
        action = define_action(icon, name, tooltip, self.on_print_click, shortcut, self)
        toolbar.addAction(action)
        menu_file.addAction(action)

        # ------------------------------------------
        menu_file.addSeparator()
        # ------------------------------------------

        # Exit Action
        icon = './icons/cross.png'
        name = '&Exit'
        tooltip = 'Exit the App'
        action = define_action(icon, name, tooltip, self.on_exit, shortcut=None, parent=self)
        menu_file.addAction(action)
        # Help Action
        icon = None
        name = 'About'
        tooltip = 'Shows the information about the software'
        action = define_action(icon, name, tooltip, self.on_about_click, shortcut=None, parent=self)
        menu_help.addAction(action)

        # SMASSH
        icon = None
        name = 'Sm&ash'
        tooltip = 'Open SMASsH to do multi tasks via ssh'
        shortcut = 'Ctrl+h'
        action = define_action(icon, name, tooltip, self.on_smash_click, shortcut, parent=self)
        menu_apps.addAction(action)

    def setup_ui(self):
        """
        Function to set up the initialization of the main window
        :return:
        """
        # Object name
        self.setObjectName('MainWindow')

        # title
        self.setWindowTitle('Javo Tools')

        # size
        self.resize(1200, 720)
        self.setMinimumSize(800, 600)

        # background of the app
        # self.setStyleSheet("background-color: #1b5e20;")

    def on_smash_click(self):
        smash = Smassh(parent=self)
        self.setCentralWidget(smash)
        self.appowner = 4

    def on_open_click(self):
        print(f'App owner is: {self.apps[self.appowner]}')
        if self.appowner > 1:
            if self.appowner == 4:
                files = open_dialog(self, '(*.xlsx)', multi_select=False)
                print(','.join(files))
            else:
                files = open_dialog(self, '*.*')
                print(','.join(files))

    def on_save_click(self):
        print('SaveFile')

    def on_print_click(self):
        print('PrintMe')

    def on_about_click(self):
        about = Licensing()
        self.setCentralWidget(about)
        self.appowner = 1

    def on_copy_click(self):
        print('Copy')

    def on_exit(self):
        print('exit me self')

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        """
        Context action for Main Window. It might change this is an example
        :param event: qt event object with the event
        :return:
        """
        menu_context = QMenu(self)
        # It seems that the software already has copy paste and such in the editable text widgets
        # # Copy
        # icon = './icons/copy-outline.svg'
        # name = 'Copy'
        # tooltip = 'Copy the selected element'
        # shortcut = 'Ctrl+c'
        # action = define_action(icon, name, tooltip, self.on_save_click, shortcut, self)
        # menu_context.addAction(action)
        # # Paste
        # icon = './icons/clipboard-outline.svg'
        # name = 'Paste'
        # tooltip = 'Paste what\'s on the clipboard'
        # shortcut = 'Ctrl+x'
        # action = define_action(icon, name, tooltip, self.on_save_click, shortcut, self)
        # menu_context.addAction(action)
        menu_context.exec(event.globalPos())

    def change_widget_default(self):
        transform = Smassh(parent=self)
        self.setCentralWidget(transform)
        self.appowner = 2


