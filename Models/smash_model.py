from PyQt6.QtCore import Qt, QAbstractTableModel, pyqtSignal, QRegularExpression
from PyQt6.QtGui import QIcon, QRegularExpressionValidator
import pandas as pd
from openpyxl import Workbook


class SmashModel(QAbstractTableModel):
    stop_signal = pyqtSignal(int)  # worker_id

    def __init__(self):
        super(SmashModel, self).__init__()
        columnas = ['ID', 'R', 'IP', 'User', 'Pass', 'Reps', 'Rem', 'Commands']
        self.instruction_df = pd.DataFrame(columns=columnas)
        self.index = 0
        self.updaing = False

    def data(self, index, role):

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 1:
                return ''
            return str(self.instruction_df.iloc[index.row(), index.column()])
        if role == Qt.ItemDataRole.EditRole:
            return str(self.instruction_df.iloc[index.row(), index.column()])
        if role == Qt.ItemDataRole.DecorationRole:
            if index.column() == 1:
                if self.instruction_df.iloc[index.row(), index.column()] == 'n':
                    return QIcon('./icons/cross.png')
                elif self.instruction_df.iloc[index.row(), index.column()] == 'y':
                    return QIcon('./icons/tick.png')
                elif '-' in self.instruction_df.iloc[index.row(), 0]:
                    return QIcon('./icons/analytics-outline.svg')
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if '-' in self.instruction_df.iloc[index.row(), 0]:
                return Qt.AlignmentFlag.AlignLeft
            return Qt.AlignmentFlag.AlignCenter

    def rowCount(self, index):
        return self.instruction_df.shape[0]

    def columnCount(self, index):
        return self.instruction_df.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.instruction_df.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(self.instruction_df.index[section] + 1)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:  # we validate the IP address
                ip_regex = QRegularExpression(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|'
                                              r'[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
                ip_validator = QRegularExpressionValidator(ip_regex)
                if ip_validator.validate(value, 0)[0].value != 0:
                    self.instruction_df.iloc[index.row(), index.column()] = value
                else:
                    self.instruction_df.iloc[index.row(), index.column()] = 'enter a valid ip'
            elif index.column() == 5:  # we validate the repetition field
                number_regex = QRegularExpression(r'^\d+$')
                number_validator = QRegularExpressionValidator(number_regex)
                if number_validator.validate(value, 0)[0].value != 0:
                    self.instruction_df.iloc[index.row(), index.column()] = value
                else:
                    self.instruction_df.iloc[index.row(), index.column()] = '0'
            elif index.column() == 6:  # we make sure nothing can be added on the remainding field
                pass
            else:
                self.instruction_df.iloc[index.row(), index.column()] = value
            return True

    # # makes the model editable
    def flags(self, index):
        if index.column() > 1 and index.column() != 6:
            return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def add_row(self, running, ip, username, passw, reps, rem, commands):
        self.instruction_df = self.instruction_df.append(
            {
                'ID': f'{self.index + 1}',
                'R': running,
                'IP': ip,
                'User': username,
                'Pass': passw,
                'Reps': reps,
                'Rem': rem,
                'Commands': commands,
            },
            ignore_index=True
        )
        self.index += 1

    def add_row_empty(self):
        self.instruction_df = self.instruction_df.append(
            {
                'ID': f'{self.index + 1}',
                'R': 'n',
                'IP': '',
                'User': '',
                'Pass': '',
                'Reps': '',
                'Rem': '',
                'Commands': '',
            },
            ignore_index=True
        )
        self.index += 1

    def remove_row(self, index):
        if not self.updaing:
            if index:
                rows = self.get_rows_to_remove(index)
                rows = list(rows)[::-1]  # we start counting from lagest value to smallest value so we can remove without order
                for row in rows:
                    worker_id = self.instruction_df.iloc[row, 0]
                    self.instruction_df = self.instruction_df.drop(row, axis=0)
            else:
                if len(self.instruction_df.index) > 0:  # remove the last element of the list
                    self.instruction_df = self.instruction_df.drop(self.instruction_df.index[-1], axis=0)
            self.instruction_df.reset_index()

    @staticmethod
    def get_rows_to_remove(elements):
        rows = []
        for element in elements:
            rows.append(element.row())
        return set(rows)

    def stop(self, worker_id):
        w_id = self.instruction_df.index[self.instruction_df.iloc[:, 0] == worker_id][-1]
        self.instruction_df.iloc[w_id, 1] = 'n'
        self.layoutChanged.emit()

    def stop_all(self):
        for row in self.instruction_df.iterrows():
            row[1].iloc[1] = 'n' if row[1].iloc[1] == 'y' else row[1].iloc[1]
        self.layoutChanged.emit()

    def duplicate_line(self, index):
        for row in index:
            ltd = self.instruction_df.iloc[row]
            self.add_row('n', ltd['IP'], ltd['User'], ltd['Pass'], ltd['Reps'], '', ltd['Commands'])

    def reduce_element(self, worker_id, number):
        w_id = self.instruction_df.index[self.instruction_df.iloc[:, 0] == worker_id][-1]
        value = int(self.instruction_df.iloc[w_id, 6])
        self.instruction_df.iloc[w_id, 6] = value - number
        self.layoutChanged.emit()

    def set_remaining(self, worker_id):
        w_id = self.instruction_df.index[self.instruction_df.iloc[:, 0] == worker_id][-1]
        self.instruction_df.iloc[w_id, 6] = self.instruction_df.iloc[w_id, 5]

    def running(self, worker_id):
        w_id = self.instruction_df.index[self.instruction_df.iloc[:, 0] == worker_id][-1]
        self.instruction_df.iloc[w_id, 1] = 'y'
        self.layoutChanged.emit()

    def get_worget_id(self, row_index):
        return self.instruction_df.iloc[row_index, 0]

    def add_answer(self, worker_id, slot, answer):
        if any(self.instruction_df.iloc[:, 0] == f'{worker_id}-{slot}'):  # answer line exists we just need to update
            w_id = self.instruction_df.index[self.instruction_df.iloc[:, 0] == f'{worker_id}-{slot}'][-1]
            self.instruction_df.iloc[w_id, 7] = answer
        else:  # Answer doesn't exists'
            w_id = self.instruction_df.index[self.instruction_df.iloc[:, 0] == worker_id][-1] + int(slot)
            upper_df = self.instruction_df[: w_id + 1]
            lower_df = self.instruction_df[w_id + 1:]

            upper_df = upper_df.append(
                {
                    'ID': f'{worker_id}-{slot}',
                    'R': '',
                    'IP': '',
                    'User': '',
                    'Pass': '',
                    'Reps': '',
                    'Rem': '',
                    'Commands': answer,
                },
                ignore_index=True
            )

            self.instruction_df = pd.concat([upper_df, lower_df])
            self.instruction_df.reset_index(drop=True, inplace=True)
        self.layoutChanged.emit()

    def clean_answers(self):
        drop_rows = []
        for row in self.instruction_df.iterrows():
            if row[1][1] == '':  # it means it is an anwer and we need to store the index to drop it
                drop_rows.append(row[0])
        self.instruction_df.drop(drop_rows, inplace=True)
        self.instruction_df.reset_index(drop=True, inplace=True)
        self.layoutChanged.emit()

    def save_model(self, path):
        if not self.updaing and len(self.instruction_df.index) > 0:
            wb = Workbook()
            current_sheet = 'blank'
            for row in self.instruction_df.iterrows():
                if '-' not in row[1]['ID']:  # this is a command
                    current_row = 1
                    current_sheet = f'{row[1]["IP"]} - {row[1]["ID"]}'
                    wb.create_sheet(title=current_sheet)
                    wb[current_sheet][f'A{current_row}'] = f'Executed commands'
                    wb[current_sheet][f'B{current_row}'] = f'{row[1]["Commands"]}'
                    current_row += 1
                else:  # this is an answer
                    wb[current_sheet][f'B{current_row}'] = f'{row[1]["Commands"]}'
                    current_row += 1
            del wb['Sheet']
            try:
                wb.save(path)
            except:
                pass

    def read_model(self, path):
        temp_df = pd.read_excel(path)
        for row in temp_df.iterrows():
            self.add_row('n', row[1]['IP'], row[1]['USER'], row[1]['PASS'], row[1]['REPS'], '', row[1]['COMMANDS'])
            self.instruction_df.reset_index(drop=True, inplace=True)
            self.layoutChanged.emit()


    def is_empty(self):
        return self.instruction_df.shape
