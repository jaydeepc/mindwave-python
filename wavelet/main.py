##################################################################################
#  This file is part of mindwave-python.                                         #
#                                                                                #
#      mindwave-python is free software: you can redistribute it and/or modify   #
#      it under the terms of the GNU General Public License as published by      #
#      the Free Software Foundation, either version 3 of the License, or         #
#      (at your option) any later version.                                       #
#                                                                                #
#      mindwave-python is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#      GNU General Public License for more details.                              #
#                                                                                #
#      You should have received a copy of the GNU General Public License         #
#      along with mindwave-python.  If not, see <http://www.gnu.org/licenses/>.  #
##################################################################################

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import mindwave
from collections import deque
import pywt

RAW_VAL_WIN_SIZE = 512
NO_OF_POINTS = 100
WAVE_TYPES = ['level {0}'.format(6-i-1) for i in range(6)]

class MyMainWindow(Ui_MainWindow):

  def __init__(self, MainWindow):
    """
    set up ui
    connect signals/slots
    """
    super(MyMainWindow, self).__init__()
    self.setupUi(MainWindow)
    self.MainWindow = MainWindow
    
    self.running = False
    self.startButton.clicked.connect(self.monitor)
    self.MainWindow.update_ui_signal.connect(self.update_ui)

    self.last_512_raw_waves = deque([0]*RAW_VAL_WIN_SIZE, RAW_VAL_WIN_SIZE)

    self.vals = {}
    for wavetype in WAVE_TYPES:
      self.vals[wavetype] = deque([0]*NO_OF_POINTS, NO_OF_POINTS)

    self.view = {}
    self.view['raw'] = self.rawView
    self.view['level 5'] = self.deltaView
    self.view['level 4'] = self.thetaView
    self.view['level 3'] = self.alphaView
    self.view['level 2'] = self.betaView
    self.view['level 1'] = self.gammaView
    self.view['level 0'] = self.restView
    for wavetype in WAVE_TYPES + ['raw']:
      self.view[wavetype].setTitle(wavetype)

    self.counter = 0

  def monitor(self):
    if self.running:
      if self.h:
        self.h.serial_close()
      self.running = False
    else:
      self.running = True
      self.h = None
      import serial
      try:
        device = self.deviceComboBox.currentText()
        self.h = mindwave.Headset("{0}".format(device))
      except serial.serialutil.SerialException, e:
        print "{0}".format(e)
        QtGui.QMessageBox.information(self.MainWindow, 'Couldn\'t find the headset', 'Headset not found. Did you pair and connect to serial device {0}?'.format(device), QtGui.QMessageBox.Ok)

      if self.h:
        self.h.raw_wave_handlers.append(self.raw_wave_handler)
      else:
        self.running = False

  def raw_wave_handler(self, headset, value):
    self.last_512_raw_waves.pop()
    self.last_512_raw_waves.appendleft(value)
    self.MainWindow.update_ui_signal.emit()

  def update_ui(self):
    self.counter += 1

    if self.counter % 512 == 0:
      self.counter = 0
      self.view['raw']
      self.view['raw'].plot(self.last_512_raw_waves, pen=(255,255,255), clear=True)
      approx = []
      detail = []
      wavelet_decomposition = self.last_512_raw_waves
      s = "{0}".format(self.waveletChoice.currentText())
      for i in range(6):
        dwt = pywt.dwt(wavelet_decomposition,s) 
        wavelet_decomposition = dwt[0]
        approx.append(dwt[0])
        detail.append(dwt[1])
      for i, wavetype in enumerate(WAVE_TYPES):
        self.view[wavetype].plot(approx[i], pen=(255, i*30, i*30), clear=True)
        self.view[wavetype].plot(detail[i], pen=(i*30, i*30, 255), clear=False)

class MainWindowWithCustomSignal(QtGui.QMainWindow):

  update_ui_signal = QtCore.pyqtSignal()

  def __init__(self, *args, **kwargs):
    super(MainWindowWithCustomSignal, self).__init__(*args, **kwargs)


def main():
  import sys
  app = QtGui.QApplication(sys.argv)
  app.setApplicationName("Eeg spectrogram FP1")
  win = MainWindowWithCustomSignal()
  ui = MyMainWindow(win)
  win.show()
  sys.exit(app.exec_())


if __name__ == "__main__":
  main()
