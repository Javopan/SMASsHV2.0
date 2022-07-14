from PyQt6.QtWidgets import QWidget, QTextEdit, QGridLayout, QPushButton
from PyQt6.QtCore import pyqtSignal


class Licensing(QWidget):
    psig_aceptado = pyqtSignal(bool)  # Signal that the license was shown boolean

    def __init__(self, button=None, parent=None):
        super(Licensing, self).__init__(parent=parent)

        message = """<p>This is a free tool under the <a href='https://www.gnu.org/licenses/gpl-3.0.en.html'>GPL v 3.</a></p>
                  <p>This software uses the following tools:</p>
                  <p>-<a href='https://riverbankcomputing.com/commercial/pyqt'>PyQT6</a><br>
                  -<a href='https://pandas.pydata.org'>Pandas</a><br>
                  -<a href='https://foss.heptapod.net/openpyxl/openpyxl'>Openpyxl</a><br>
                  -<a href='https://www.paramiko.org'>Paramiko</a><br>
                  -<a href='https://pyinstaller.org/en/stable/'>PyInstaller</a>
                  <p>We use the folowing icons:</p>
                  -<a href='https://p.yusukekamiyamane.com'>Fugue Icons</a> by Yusuke Kamiyamane
                  -<a href='https://github.com/ionic-team/ionicons'>ionicons</a>
                  <p>The software if provided as is and no warranties are given</p>
                  <p>The software was done by Javopanawesomesystems for Siklu Services Team <br> as a token of love.</p>
                  <p>If you want information on the software you can contact me at javiertm@gmail.com</p>"""

        txt_texto = QTextEdit(message)
        if button:
            btn_aceptar = QPushButton("Understood! Now let's smash something")
            btn_aceptar.clicked.connect(self.aceptado)

        layout = QGridLayout()
        layout.addWidget(txt_texto, 0, 0, 1, 1)
        if button:
            layout.addWidget(btn_aceptar, 1, 0, 1, 1)

        self.setLayout(layout)

    def aceptado(self):
        self.psig_aceptado.emit(True)
