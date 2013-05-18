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

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
import mindwave
import eyeblinkdetector
from collections import deque
import rtmidi
import notequeue

RAW_VAL_WIN_SIZE = 512
EYEBLINK_WIN_SIZE = 128
NO_OF_POINTS = 100

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
    self.rescanMidiButton.clicked.connect(self.rescanMidi)
    self.MainWindow.update_ui_signal.connect(self.update_ui)
    self.midiDeviceComboBox.currentIndexChanged.connect(self.choose_midi_device)

    self.last_512_raw_waves = deque([0]*RAW_VAL_WIN_SIZE, RAW_VAL_WIN_SIZE)

    self.counter = 0

    self.notequeue = notequeue.NoteQueue(3)

    self.eyeblink_counter = 0
    self.eyeblink_in_progress = False
    self.eyeblink_detector = eyeblinkdetector.EyeblinkDetector(self.handle_blink_event)
    self.rescanMidi()

  def monitor(self):
    if self.running:
      self.notequeue.clear_all_notes()
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
        self.h.meditation_handlers.append(self.handle_meditation_event)
        self.h.attention_handlers.append(self.handle_attention_event)
      else:
        self.running = False

  def rescanMidi(self):
    self.midiOut = rtmidi.MidiOut(rtmidi.API_UNIX_JACK)
    self.available_ports = self.midiOut.get_ports()
    self.midiDeviceComboBox.clear()
    for p in self.available_ports:
      self.midiDeviceComboBox.addItem(p)
    if self.available_ports:
      self.midiOut.open_port(0)

  def choose_midi_device(self, index):
    print "opening midi device ", self.available_ports[index]
    self.notequeue.clear_all_notes()
    self.midiOut.close_port()
    self.midiOut.open_port(index)

  def raw_wave_handler(self, headset, value):
    self.last_512_raw_waves.pop()
    self.last_512_raw_waves.appendleft(value)
    self.MainWindow.update_ui_signal.emit()

  def check_eyeblink(self, sensitivity, lowfreq, highfreq):
    import pyeeg
    last_128_waves = list(self.last_512_raw_waves)[:EYEBLINK_WIN_SIZE]
    try:
      return self.eyeblink_detector.check_eyeblink(sensitivity, lowfreq, highfreq, last_128_waves)
    except ValueError:
        QtGui.QMessageBox.information(self.MainWindow, 'Eye blink sensitivity', 'Invalid eyeblink sensitivity specified. Try 0.45 as a start.', QtGui.QMessageBox.Ok)
    return False

  def handle_blink_event(self):
    if self.eyeBlinkCheckBox.isChecked():
      import random
      try:
        # parse "0,1,2" into [0, 1, 2]
        ms = self.eyeBlinkMidiChannel.text()
        ms_split = ms.split(",")
        midichan = [ int(i) for i in ms_split ]
      except ValueError:
        return

      msgbytes  = self.notequeue.play_note( 
                    random.choice(midichan), 
                    random.choice([i+36 for i in range(24)]),
                    random.choice([i+1 for i in range(126)]))
      #print "send midi msg: ", msgbytes
      for msg in msgbytes:
        self.midiOut.send_message(msg)

  def handle_meditation_event(self, headset, value):
    if self.meditationCheckBox.isChecked():
      import random
      try:
        # parse "0,1,2" into [0, 1, 2]
        ms = self.meditationMidiChannel.text()
        ms_split = ms.split(",")
        midichan = [ int(i) for i in ms_split ]
      except ValueError:
        return

      #print value
      if value:
        msgbytes  = self.notequeue.play_note( 
                      random.choice(midichan), 
                      value,
                      random.choice([i+1 for i in range(126)]))

        #print "send midi msg: ", msgbytes
        for msg in msgbytes:
          self.midiOut.send_message(msg)

  def handle_attention_event(self, headset, value):
    if self.attentionCheckBox.isChecked():
      import random
      try:
        # parse "0,1,2" into [0, 1, 2]
        ms = self.attentionMidiChannel.text()
        ms_split = ms.split(",")
        midichan = [ int(i) for i in ms_split ]
      except ValueError:
        return

      #print value
      if value:
        msgbytes  = self.notequeue.play_note( 
                      random.choice(midichan), 
                      value,
                      random.choice([i+1 for i in range(126)]))

        #print "send midi msg: ", msgbytes
        for msg in msgbytes:
          self.midiOut.send_message(msg)

  def update_ui(self):
    self.counter += 1

    if self.counter % EYEBLINK_WIN_SIZE == 0:
      self.counter = 0
      if self.check_eyeblink(self.eyeBlinkSensitivity.text(),
                             self.lowerEyeBlinkFrequency.text(),
                             self.higherEyeBlinkFrequency.text()):
        self.eyeblink_counter += 1
        #print "BLINK {0}".format(self.eyeblink_counter)

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
