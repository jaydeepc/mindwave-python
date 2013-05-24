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
import notelookup

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

    # connect signals and slots
    self.startButton.clicked.connect(self.monitor)
    self.rescanMidiButton.clicked.connect(self.rescanMidi)
    self.MainWindow.update_ui_signal.connect(self.update_ui)
    self.MainWindow.update_statusbar_signal.connect(self.update_statusbar)
    self.midiDeviceComboBoxes = [ 
        self.midiDevice0ComboBox,
        self.midiDevice1ComboBox,
        self.midiDevice2ComboBox,
        self.midiDevice3ComboBox,
        self.midiDevice4ComboBox,
        self.midiDevice5ComboBox,
        self.midiDevice6ComboBox,
        self.midiDevice7ComboBox,
        self.midiDevice8ComboBox,
        self.midiDevice9ComboBox,
        self.midiDevice10ComboBox,
        self.midiDevice11ComboBox,
        self.midiDevice12ComboBox,
        self.midiDevice13ComboBox,
        self.midiDevice14ComboBox,
        self.midiDevice15ComboBox 
        ]
    for i,cb in enumerate(self.midiDeviceComboBoxes):
      cb.currentIndexChanged.connect(self.choose_midi_device_for_channel(i))

    self.resetButtons = [
        self.resetChannel0Button,
        self.resetChannel1Button,
        self.resetChannel2Button,
        self.resetChannel3Button,
        self.resetChannel4Button,
        self.resetChannel5Button,
        self.resetChannel6Button,
        self.resetChannel7Button,
        self.resetChannel8Button,
        self.resetChannel9Button,
        self.resetChannel10Button,
        self.resetChannel11Button,
        self.resetChannel12Button,
        self.resetChannel13Button,
        self.resetChannel14Button,
        self.resetChannel15Button
        ]
    for i,rb in enumerate(self.resetButtons):
      rb.clicked.connect(self.reset_button_for_channel(i))

    # provide storage to remember the last 512 raw eeg data points
    self.last_512_raw_waves = deque([0]*RAW_VAL_WIN_SIZE, RAW_VAL_WIN_SIZE)

    self.counter = 0

    # reserve a notequeue to remember 3 notes on each channel
    self.notequeue = notequeue.NoteQueue(3)

    # setup eyeblink checker
    self.eyeblink_counter = 0
    self.eyeblink_in_progress = False
    self.eyeblink_detector = eyeblinkdetector.EyeblinkDetector(self.handle_blink_event)

    # make sure the midi device combo boxes are populated
    self.rescanMidi()

    # statusbar text elements
    self.connected = "not connected"
    self.signal_quality = "unknown signal quality"
    self.update_statusbar()

    self.notelookup = notelookup.NoteLookup()

    self.actionQuit.triggered.connect(QtGui.qApp.quit)

  def quit_gracefully(self):
    for i,mo in enumerate(self.midiOut):
      bytemsg = self.notequeue.clear_notes(i)
      for msg in bytemsg:
        self.midiOut[i].send_message(msg)

  def monitor(self):
    """
    start/stop button
    """
    if self.running:
      self.connected = "Not connected"
      self.signal_quality = "unknown signal quality"
      for i,mo in enumerate(self.midiOut):
        bytemsg = self.notequeue.clear_notes(i)
        for msg in bytemsg:
          self.midiOut[i].send_message(msg)
      if self.h:
        self.h.serial_close()
      self.running = False
    else:
      self.connected = "Connected"
      self.signal_quality = "unknown signal quality"
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
        self.h.poor_signal_handlers.append(self.handle_poor_signal)
        self.h.good_signal_handlers.append(self.handle_good_signal)
      else:
        self.running = False

    self.update_statusbar()

  def handle_poor_signal(self, headset, value):
    self.signal_quality = "poor signal quality {0}%".format(value)
    self.MainWindow.update_statusbar_signal.emit()

  def handle_good_signal(self, headset, value):
    self.signal_quality = "good signal quality"
    self.MainWindow.update_statusbar_signal.emit()

  def rescanMidi(self):
    """
    list all recognized midi devices
    """
    self.midiOut = [rtmidi.MidiOut(rtmidi.API_UNIX_JACK) for i in range(16) ]
    self.available_ports = self.midiOut[0].get_ports()
    for midiDeviceComboBox in self.midiDeviceComboBoxes:
      midiDeviceComboBox.clear()
      for p in self.available_ports:
        midiDeviceComboBox.addItem(p)
    if self.available_ports:
      for mo in self.midiOut:
        mo.open_port(0)

  def choose_midi_device_for_channel(self, channel):
    """
    returns a callback function suitable to connect to midi device for channel
    """
    def choose_midi_device(index):
      print "opening midi device ", self.available_ports[index], " for midi channel ", channel
      msgbytes = self.notequeue.clear_notes(channel)
      for msg in msgbytes:
        self.midiOut[channel].send_message(msg)
      self.midiOut[channel].close_port()
      self.midiOut[channel].open_port(index)
    return choose_midi_device

  def reset_button_for_channel(self, channel):
    """
    returns a callback function suitable to connect to midi channel reset button
    """
    def reset_channel(index):
      print "clear all notes on channel ", channel, " for the current midi device"
      msgbytes = self.notequeue.clear_notes(channel)
      for msg in msgbytes:
        self.midiOut[channel].send_message(msg)
    return reset_channel 

  def raw_wave_handler(self, headset, value):
    """
    callback function that accumulates raw eeg data
    for each new raw data point, a custom qt signal (update_ui_signal) is emitted
    """
    self.last_512_raw_waves.pop()
    self.last_512_raw_waves.appendleft(value)
    self.MainWindow.update_ui_signal.emit()

  def check_eyeblink(self, sensitivity, lowfreq, highfreq):
    """
    function that checks if last 128 raw eeg points contain an eye blink event
    """
    last_128_waves = list(self.last_512_raw_waves)[:EYEBLINK_WIN_SIZE]
    try:
      return self.eyeblink_detector.check_eyeblink(sensitivity, lowfreq, highfreq, last_128_waves)
    except ValueError:
        QtGui.QMessageBox.information(self.MainWindow, 'Eye blink sensitivity', 'Invalid eyeblink sensitivity specified. Try 0.45 as a start.', QtGui.QMessageBox.Ok)
    return False

  def parse_midi_channel_list(self, text):
    """
    parse "1,2 , 3, 4 ,5" into [1,2,3,4,5]
    """
    try:
      ms_split = text.split(",")
      chans = [ int(i) for i in ms_split ]
      return chans
    except ValueError:
      return []

  def parse_number_ranges(self, text):
    """
    parse "4:8:2, a4:c#5:2" into [4,6,8,69,71,73]
    """
    values = []
    try:
      ranges = text.split(",")
      for rng in ranges:
        colon_split = rng.split(":")
        start = None
        stop = None
        step = 1
        if len(colon_split) == 3:
          start = self.notelookup.lookup(colon_split[0])
          stop = self.notelookup.lookup(colon_split[1])
          step = int(colon_split[2])
        elif len(colon_split) == 1:
          start = self.notelookup.lookup(colon_split[0])
          stop = start
          step = 1
        if start is not None and stop is not None:
          values.extend( [start+i*step for i in range((stop-start)/step+1)])
    except ValueError:
      values = []

    return values

  def handle_blink_event(self):
    """
    function to do something if an eye blink event is detected
    """
    if self.eyeBlinkCheckBox.isChecked():
      midichan = self.parse_midi_channel_list(self.eyeBlinkMidiChannel.text())
      if not midichan:
        return
      values = self.parse_number_ranges(self.eyeBlinkAllowedValueEdit.text())
      if not values:
        return
      vels = self.parse_number_ranges(self.eyeBlinkAllowedVelsEdit.text())
      if not vels:
        return

      import random
      chan = random.choice(midichan)
      value= random.choice(values)
      vel  = random.choice(vels)

      msgbytes  = self.notequeue.play_note( 
                    chan, 
                    value,
                    vel)

      #print "send midi msg: ", msgbytes
      for msg in msgbytes:
        self.midiOut[chan].send_message(msg)

  def handle_meditation_event(self, headset, value):
    """
    function to do something when a meditation event is detected
    """
    if self.meditationCheckBox.isChecked():
      midichan = self.parse_midi_channel_list(self.meditationMidiChannel.text())
      if not midichan:
        return
      vels = self.parse_number_ranges(self.meditationAllowedVelsEdit.text())
      if not vels:
        return
      values = self.parse_number_ranges(self.meditationAllowedValueEdit.text())
      values.append(value)

      import random
      chan = random.choice(midichan)
      value= random.choice(values)
      vel  = random.choice(vels)
 
      #print value
      if value:
        msgbytes  = self.notequeue.play_note( 
                      chan, 
                      value,
                      vel)

        #print "send midi msg: ", msgbytes
        for msg in msgbytes:
          self.midiOut[chan].send_message(msg)

  def handle_attention_event(self, headset, value):
    """
    function to do something when an attention event is detected
    """
    if self.attentionCheckBox.isChecked():
      midichan = self.parse_midi_channel_list(self.attentionMidiChannel.text())
      if not midichan:
        return
      vels = self.parse_number_ranges(self.attentionAllowedVelsEdit.text())
      if not vels:
        return
      values = self.parse_number_ranges(self.attentionAllowedValueEdit.text())
      values.append(value)

      import random
      chan = random.choice(midichan)
      value= random.choice(values)
      vel  = random.choice(vels)
 
      #print value
      if value:
        msgbytes  = self.notequeue.play_note( 
                      chan, 
                      value,
                      vel)

        #print "send midi msg: ", msgbytes
        for msg in msgbytes:
          self.midiOut[chan].send_message(msg)

  def update_ui(self):
    """
    triggered whenever a raw eeg data point arrives
    """
    self.counter += 1

    if self.counter % EYEBLINK_WIN_SIZE == 0:
      self.counter = 0
      if self.check_eyeblink(self.eyeBlinkSensitivity.text(),
                             self.lowerEyeBlinkFrequency.text(),
                             self.higherEyeBlinkFrequency.text()):
        self.eyeblink_counter += 1
        #print "BLINK {0}".format(self.eyeblink_counter)

  def update_statusbar(self):
    self.statusbar.showMessage("{0} - {1}".format(self.connected,self.signal_quality))

class MainWindowWithCustomSignal(QtGui.QMainWindow):
  """
  specialized QtGui.MainWindow

  has to be specialized to let it react to a new qt signal
  (needed to update ui from callback function called from different thread)
  """
  update_ui_signal = QtCore.pyqtSignal()
  update_statusbar_signal = QtCore.pyqtSignal()

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
