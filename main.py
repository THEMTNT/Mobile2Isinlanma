import time
from pymem import Pymem
from pymem.ptypes import RemotePointer
import Pointer as Pt
from gui import Ui_Marley
from PyQt5 import QtWidgets, QtCore
import sendkey
import threading
import sys
import win32gui

class MyGui(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyGui, self).__init__()
        self.ui = Ui_Marley()
        self.ui.setupUi(self)
        self.setWindowTitle("Yaşasın Okulumuz")
        self.flagPauseZipla = False
        self.vk = sendkey.VirtualKeyboard()
        self.oku()
        self.ui.pushButtonziplabaslat.clicked.connect(self.zipla)
        self.ui.pushButtonzipladurdur.clicked.connect(lambda: self.setFlagPauseZipla(True))
        self.ui.pushButtonisinlan.clicked.connect(self.isinla)
        self.ui.pushButtonxarttir.clicked.connect(self.xarttir)
        self.ui.pushButtonyarttir.clicked.connect(self.yarttir)
        self.ui.pushButtonzarttir.clicked.connect(self.zarttir)
        self.ui.pushButtonxazalt.clicked.connect(self.xazalt)
        self.ui.pushButtonyazalt.clicked.connect(self.yazalt)
        self.ui.pushButtonzazalt.clicked.connect(self.zazalt)
        self.ui.pushButtonkoordinatekle.clicked.connect(self.koordinatekleliste)
        self.ui.pushButtonkoordinatsil.clicked.connect(self.koordinatsilliste)
        self.ui.pushButtonkoordinatsave.clicked.connect(self.koordinatsave)
        self.ui.checkBoxherzamanustte.clicked.connect(self.ustte)
        self.ui.pushButtonsecilenegit.clicked.connect(self.secilenegit)
        self.ui.pushButtongitgel.clicked.connect(self.gitgel)
        self.ui.pushButtontextekle.clicked.connect(self.listetextekle)



    def listetextekle(self):
        text = f"{self.ui.lineEditx.text()} {self.ui.lineEdity.text()} {self.ui.lineEditz.text()}"
        new_item = QtWidgets.QListWidgetItem(text)
        self.ui.listWidgetkoordinat.addItem(new_item)
    def gitgel(self):
        def calis():
            global pm
            while self.ui.checkBoxxyzkitle.isChecked():
                try:
                    pm = Pymem(Pt.gamename)
                    for index in range(self.ui.listWidgetkoordinat.count()):
                        item = self.ui.listWidgetkoordinat.item(index)
                        text = item.text()
                        x, y, z = text.split()
                        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]),value=float(x))
                        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]),value=float(y))
                        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),value=float(z))
                        hwnd = win32gui.FindWindow(None, "Mobile2 Global  ")
                        if hwnd is not None:
                            self.vk.sendkey(hwnd,'a')
                        time.sleep(float(self.ui.lineEditgitgeltime.text()))

                    if self.ui.checkBoxxyzkitle.isChecked() is not True:
                        break
                except:
                    pass

        threading.Timer(0.1, calis).start()




    def secilenegit(self):
        selected_item = self.ui.listWidgetkoordinat.currentItem()
        if selected_item is not None:
            text = selected_item.text()
            x,y,z = text.split()
            pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]),value=float(x))
            pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]),value=float(y))
            pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),value=float(z))


    def ustte(self):
        flags = self.windowFlags()

        # checkBoxherzamanustte'nin durumuna göre pencereyi her zaman üstte tut veya tutma
        flags = self.windowFlags()

        # checkBoxherzamanustte'nin durumuna göre pencereyi her zaman üstte tut veya tutma
        if self.ui.checkBoxherzamanustte.isChecked():
            self.setWindowFlags(flags | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(flags & ~QtCore.Qt.WindowStaysOnTopHint)

        # Pencereyi güncelle
        self.show()


    def koordinatsave(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Listeyi Kaydet", "", "Metin Dosyaları (*.txt)")
        if file_path:
            with open(file_path, 'w') as file:
                for row in range(self.ui.listWidgetkoordinat.count()):
                    item = self.ui.listWidgetkoordinat.item(row)
                    file.write(f"{item.text()}\n")

    def koordinatsilliste(self):
        selected_item = self.ui.listWidgetkoordinat.currentItem()
        if selected_item is not None:
            row = self.ui.listWidgetkoordinat.row(selected_item)
            self.ui.listWidgetkoordinat.takeItem(row)

    def koordinatekleliste(self):
        x = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]))
        y = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]))
        z = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]))
        text = f"{round(x,2)} {round(y,2)} {round(z,2)}"
        self.ui.listWidgetkoordinat.addItem(text)




    def xarttir(self):
        x = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]))
        print(f"Suanki x degeri {x}")
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]),value=x + float(self.ui.lineEditzipla.text()))
    def yarttir(self):

        y = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]))
        print(f"Suanki y degeri {y}")
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]),value=y + float(self.ui.lineEditzipla.text()))
    def zarttir(self):
        z = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]))
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),value = z + float(self.ui.lineEditzipla.text()))
    def xazalt(self):
        x = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]))
        print(f"Suanki x degeri {x}")
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]),value=x - float(self.ui.lineEditzipla.text()))
    def yazalt(self):

        y = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]))
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]),value=y - float(self.ui.lineEditzipla.text()))
    def zazalt(self):

        z = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]))
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),value=z - float(self.ui.lineEditzipla.text()))

    def isinla(self):
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]),value=float(self.ui.lineEditx.text()))
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]),value=float(self.ui.lineEdity.text()))
        pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),value=float(self.ui.lineEditz.text()))

        def calis():
            while self.ui.checkBoxxyzkitle.isChecked():
                pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]),value=float(self.ui.lineEditx.text()))
                pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]),value=float(self.ui.lineEdity.text()))
                pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),value=float(self.ui.lineEditz.text()))

                if self.ui.checkBoxxyzkitle.isChecked() is not True:
                    break

        threading.Timer(0.1, calis).start()


    def setFlagPauseZipla(self, value):
        self.flagPauseZipla = value
        self.ui.pushButtonzipladurdur.isEnabled()
        self.ui.pushButtonziplabaslat.isEnabled()
    def zipla(self):
        self.flagPauseZipla=False
        z = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]))
        self.ui.pushButtonzipladurdur.isEnabled()
        self.ui.pushButtonziplabaslat.isEnabled()

        def calis():
            while self.flagPauseZipla is not True:
                pm.write_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]),z+float(self.ui.lineEditzipla.text()))

        threading.Timer(0.1, calis).start()

    def oku(self):
        try:
            x = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsx[0], offsets=Pt.offsetsx[1:]))
            y = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsy[0], offsets=Pt.offsetsy[1:]))
            z = pm.read_float(getPointerAddress(pm.base_address + Pt.offsetsz[0], offsets=Pt.offsetsz[1:]))
            self.ui.labelx.setText("{:.2f}".format(x))
            self.ui.labely.setText("{:.2f}".format(y))
            self.ui.labelz.setText("{:.2f}".format(z))
        except:
            pass
        threading.Timer(1.0, self.oku).start()

if __name__ == "__main__":
    a = Pt.read_offsets_from_file()
    Pt.offsetsx = a['x']
    Pt.offsetsy = a['y']
    Pt.offsetsz = a['z']

    def getPointerAddress(base, offsets):
        remote_pointer = RemotePointer(pm.process_handle, base)
        for offset in offsets:
            if offset != offsets[-1]:
                remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
            else:
                return remote_pointer.value + offset
    pm = Pymem(Pt.gamename)
    app = QtWidgets.QApplication(sys.argv)
    win = MyGui()
    win.show()
    sys.exit(app.exec_())
    

