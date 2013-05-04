from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import mindwave
from collections import deque
import pyeeg
import numpy as np

RAW_VAL_WIN_SIZE = 512
NO_OF_POINTS = 100
WAVE_TYPES = ['delta', 'theta', 'alpha', 'beta', 'gamma', 'rest']
BANDS = ['0.5-4','4-8', '8-13', '13-30', '30-100', '100-256', '']
    
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
    self.view['delta'] = self.deltaView
    self.view['theta'] = self.thetaView
    self.view['alpha'] = self.alphaView
    self.view['beta'] = self.betaView
    self.view['gamma'] = self.gammaView
    self.view['rest'] = self.restView
    for i, wavetype in enumerate(WAVE_TYPES + ['raw']):
      title = wavetype + " " + BANDS[i]
      if wavetype != "raw": 
        title += " Hz"
      self.view[wavetype].setTitle(title)
      if wavetype == "raw":
        self.view[wavetype].setYRange(-600,600)

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
 
    if self.counter % 10 == 0:
      self.view['raw']
      self.view['raw'].plot(self.last_512_raw_waves, pen=(255,255,255), clear=True)
    if self.counter >= RAW_VAL_WIN_SIZE:
        self.counter = 0
        spectrum, normalized_spectrum = pyeeg.bin_power(self.last_512_raw_waves, [0.5, 4, 8, 13, 30, 100, 256], 512)
        for i, wavetype in enumerate(WAVE_TYPES):
          self.vals[wavetype].pop()
          self.vals[wavetype].appendleft(normalized_spectrum[i])
          self.view[wavetype].plot(self.vals[wavetype], pen=(255, i*30, i*30), clear=True)
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
