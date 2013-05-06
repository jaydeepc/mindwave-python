##################################################################################
#      This file is part of mindwave-python.                                     #
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

from PyQt4 import QtCore, QtGui, Qt
from mainwindow import Ui_MainWindow
import mindwave
from collections import deque
from statemachine import BlinkInterpreter

RAW_VAL_WIN_SIZE = 512
EYEBLINK_WIN_SIZE = 128 
NO_OF_POINTS = 100

EMPTY = 0

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
    self.MainWindow.eyeblink_signal.connect(self.handle_eyeblink)

    self.last_512_raw_waves = deque([0]*RAW_VAL_WIN_SIZE, RAW_VAL_WIN_SIZE)

    self.counter = 0
    self.eyeblink_counter = 0
    self.blink_interpreter = BlinkInterpreter()

    self.row = 0
    self.col = 0
    self.clock_divider = 0

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

  def check_eyeblink(self, sensitivity, lowfreq, highfreq):
    import pyeeg
    last_128_waves = list(self.last_512_raw_waves)[:EYEBLINK_WIN_SIZE]
    spectrum, rel_spectrum = pyeeg.bin_power(last_128_waves,[0.5,lowfreq,highfreq,256],512)
    try:
        if (rel_spectrum[1] > float(sensitivity)):
          self.MainWindow.eyeblink_signal.emit()
        else:
          pass
    except ValueError:
        QtGui.QMessageBox.information(self.MainWindow, 'Eye blink sensitivity', 'Invalid eyeblink sensitivity specified. Try 0.45 as a start.', QtGui.QMessageBox.Ok)
    return False

  def handle_eyeblink(self):
    self.eyeblink_counter += 1
    self.blink_interpreter.handle_eyeblink()
    # blink to stop current operation
    #print "BLINK {0}".format(self.eyeblink_counter)

  def update_selection(self):
    self.operationTable.setRangeSelected(QtGui.QTableWidgetSelectionRange(self.row, self.col, self.row, self.col), False)
    try:
      self.row, self.col, self.clock_divider, new_speed = self.blink_interpreter.step(int(self.speedEdit.text()), self.clock_divider)
      self.speedEdit.setText("{0}".format(new_speed))
    except ValueError:
      pass
    self.operationTable.setRangeSelected(QtGui.QTableWidgetSelectionRange(self.row, self.col, self.row, self.col), True)

  def update_ui(self):
    self.counter += 1

    if self.counter % EYEBLINK_WIN_SIZE == 0:
      self.counter = 0
      self.check_eyeblink(self.eyeBlinkSensitivity.text(),
                          self.lowerEyeBlinkFrequency.text(),
                          self.higherEyeBlinkFrequency.text())
      self.update_selection()

class MainWindowWithCustomSignal(QtGui.QMainWindow):

  update_ui_signal = QtCore.pyqtSignal()
  eyeblink_signal = QtCore.pyqtSignal()

  def __init__(self, *args, **kwargs):
    super(MainWindowWithCustomSignal, self).__init__(*args, **kwargs)
#    self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)

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
