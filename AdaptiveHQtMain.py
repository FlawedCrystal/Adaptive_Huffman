import os

import bitstring
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
import sys

from AdaptiveHFrom import Ui_Form
from addaptive_huffman import Coder, Decoder


class HuffmanWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.unpack)
        self.pushButton_2.clicked.connect(self.open_files)
        self.pushButton_3.clicked.connect(self.open_dir)
        self.pushButton_4.clicked.connect(self.pack)
        self.dir = ""
        self.files = ""

    def unpack(self):
        if self.files and self.dir:
            for file_name in self.files:
                msg = QMessageBox()
                print(os.path.normpath(file_name))
                with open(os.path.normpath(file_name), 'rb') as file:
                    text = ''.join([bin(symbol)[2:].zfill(8) for symbol in file.read()])
                decoder = Decoder(text)
                try:
                    res = decoder.unclench()
                except Exception as err:
                    msg.setText(f" : {err}")
                else:
                    res = ''.join([bin(ord(symbol))[2:].zfill(8) for symbol in res])
                    new_file_name = os.path.join(self.dir, os.path.basename(file_name[:-5]))
                    with open(new_file_name, 'wb') as f:
                        f.write(b'')
                        bitstring.Bits(bin=res).tofile(f)
                    msg.setText(f"Результат готов, путь : {new_file_name}")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()


        else:
            msg = QMessageBox()
            msg.setText(f"Вы не выбрали файл или директорию")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def pack(self):
        if self.files and self.dir:
            for file_name in self.files:
                print(os.path.normpath(file_name))
                with open(os.path.normpath(file_name), 'rb') as file:
                    text = ''.join([chr(i) for i in file.read()])
                coder = Coder(text)
                res = coder.squeeze()
                new_file_name = os.path.join(self.dir, os.path.basename(file_name)+'.huff')
                with open(new_file_name, 'wb') as f:
                    f.write(b'')
                    bitstring.Bits(bin=res).tofile(f)
                msg = QMessageBox()
                msg.setText(f"Результат готов, путь : {new_file_name}")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText(f"Вы не выбрали файл или директорию")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def open_files(self):
        file_name, _ = QFileDialog.getOpenFileNames(self, 'Выберете файл для дальнейшей работы с ним', r".", )
        self.files = file_name
        print(self.files)

    def open_dir(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Выберете директорию для сохранения результата', r".", )
        self.dir = os.path.normpath(dir_name)
        print(self.dir)


def create_window():
    app = QApplication(sys.argv)
    window = HuffmanWidget()
    window.show()
    app.exec()


def main():
    create_window()


if __name__ == '__main__':
    main()
