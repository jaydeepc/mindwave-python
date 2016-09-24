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
import simpleserializer


RAW_VAL_WIN_SIZE = 512
EYEBLINK_WIN_SIZE = 128
NO_OF_POINTS = 100
MEDITATION = 'meditation'
ATTENTION = 'attention'
EYEBLINK = 'eyeBlink'
SECTIONS = [MEDITATION, ATTENTION, EYEBLINK]


class MyMainWindow(Ui_MainWindow):

  def __init__(self, MainWindow):
    """
    set up ui
    connect signals/slots
    """
    super(MyMainWindow, self).__init__()
    self.setupUi(MainWindow)
    self.MainWindow = MainWindow
    self.last_loaded_scene = None 

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
    # reset midi channel buttons
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

    resetAllMidiButton = self.resetAllMidiButton
    resetAllMidiButton.clicked.connect(self.reset_button_for_all)

    self.midiAllDevice = self.selectAllMidiDevice
    self.midiAllDevice.currentIndexChanged.connect(self.choose_midi_device_for_all)

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

    # instantiate an object that can transform note names to midi numbers
    self.notelookup = notelookup.NoteLookup()

    # more signals: what to do if a checkbox is clicked
    self.attentionCheckBox.clicked.connect(self.attentionCheckBoxClicked)
    self.meditationCheckBox.clicked.connect(self.meditationCheckBoxClicked)
    self.eyeBlinkCheckBox.clicked.connect(self.eyeBlinkCheckBoxClicked)

    # make sure the menu entries do something
    self.actionQuit.triggered.connect(QtGui.qApp.quit)

    # attach signals to the scene buttons
    self.loadSceneButtons = [ self.loadScene1Button, self.loadScene2Button, self.loadScene3Button,
                              self.loadScene4Button, self.loadScene5Button, self.loadScene6Button,
                              self.loadScene7Button, self.loadScene8Button, self.loadScene9Button]
    self.saveSceneButtons = [ self.saveScene1Button, self.saveScene2Button, self.saveScene3Button,
                              self.saveScene4Button, self.saveScene5Button, self.saveScene6Button,
                              self.saveScene7Button, self.saveScene8Button, self.saveScene9Button]
    for i,b in enumerate(self.loadSceneButtons):
      self.loadSceneButtons[i].clicked.connect(self.load_nth_scene(i))
      self.saveSceneButtons[i].clicked.connect(self.save_nth_scene(i))

    # determine which ui elements should be saved/loaded
    self.setup_serialization()

    # discover the plugins and display in the ui as needed
    self.setup_plugins()

  def setup_serialization(self):
    """
    function that collects all information required for saving ui state to model file
    """
    def lineedit_getter(lineedit):
      return "{0}".format(lineedit.text())

    def lineedit_setter(lineedit, value):
      lineedit.setText(value)

    def checkbox_getter(checkbox):
      return checkbox.isChecked()

    def checkbox_setter(checkbox, value):
      checkbox.setChecked(value)

    def combobox_getter(combobox):
      return "{0}".format(combobox.currentText())

    def combobox_setter(combobox, value):
      idx = combobox.findText(value)
      if idx != -1:
        combobox.setCurrentIndex(idx);
      else:
        print "Warning: couldn't restore combobox to value ", value

    self.serializer = simpleserializer.SimpleSerializer()
    self.serializer.register("deviceComboBox", self.deviceComboBox, combobox_getter, combobox_setter)
    self.serializer.register("eyeBlinkSensitivity", self.eyeBlinkSensitivity, lineedit_getter, lineedit_setter)
    self.serializer.register("lowerEyeBlinkFrequency", self.lowerEyeBlinkFrequency, lineedit_getter, lineedit_setter)
    self.serializer.register("higherEyeBlinkFrequency", self.higherEyeBlinkFrequency, lineedit_getter, lineedit_setter)
    for i,cb in enumerate(self.midiDeviceComboBoxes):
      self.serializer.register("midiDevice{0}ComboBox".format(i), cb, combobox_getter, combobox_setter)

    self.serializer.register("attentionCheckBox", self.attentionCheckBox, checkbox_getter, checkbox_setter)
    self.serializer.register("attentionPluginComboBox", self.attentionPluginComboBox, combobox_getter, combobox_setter)

    self.serializer.register("meditationCheckBox", self.meditationCheckBox, checkbox_getter, checkbox_setter)
    self.serializer.register("meditationPluginComboBox", self.meditationPluginComboBox, combobox_getter, combobox_setter)

    self.serializer.register("eyeBlinkCheckBox", self.eyeBlinkCheckBox, checkbox_getter, checkbox_setter)
    self.serializer.register("eyeBlinkPluginComboBox",self.eyeBlinkPluginComboBox, combobox_getter, combobox_setter)

  def setup_plugins(self):
    """
    discover all plugins and populate the plugin combo boxes
    setup signals so that selecting a plugin has some effect
    """
    self.prevAttentionPluginIndex = 0
    self.prevMeditationPluginIndex = 0
    self.prevEyeBlinkPluginIndex = 0
    
    #enable the following 2 lines of code to debug yapsy discovery
    #import logging
    #logging.basicConfig(level=logging.DEBUG)
 
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    from getinstallpath import getInstallPath
    import os.path
    places = [ os.path.join(getInstallPath(), "midicontroller/plugins/scoregenerators") ]
    manager.setPluginPlaces(places)
    manager.locatePlugins()
    manager.loadPlugins()
    print "Discovered the following plugins:"
    for plugin in manager.getAllPlugins():
      n = plugin.plugin_object.name
      print n
      self.attentionPluginComboBox.addItem(n)
      self.meditationPluginComboBox.addItem(n)
      self.eyeBlinkPluginComboBox.addItem(n)

    self.attentionPluginComboBox.currentIndexChanged.connect(self.attentionPluginSelected)
    self.meditationPluginComboBox.currentIndexChanged.connect(self.meditationPluginSelected)
    self.eyeBlinkPluginComboBox.currentIndexChanged.connect(self.eyeBlinkPluginSelected)
    self.attentionPluginSelected(0)
    self.meditationPluginSelected(0)
    self.eyeBlinkPluginSelected(0)

  def suspend_plugin(self, plugin_object, section):
    """
    define how to suspend a running plugin without deleting it, e.g. when the checkbox is unchecked
    """
    plugin_object.suspend(section)
    midichan = plugin_object.get_midi_channel_list(section)
    for m in midichan:
       msgbytes = self.notequeue.clear_notes(m)
       for msg in msgbytes:
          self.midiOut[m].send_message(msg)

  def attentionCheckBoxClicked(self):
    """
    what to do if the attention check box is clicked
    """
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    plugin = manager.getAllPlugins()[self.prevAttentionPluginIndex]
    if not self.attentionCheckBox.isChecked():
      self.suspend_plugin(plugin.plugin_object, ATTENTION)
    else:
      plugin.plugin_object.resume(ATTENTION)
  
  def attentionPluginSelected(self, index):
    """
    what to do if an attention plugin is selected
    """
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    plugin = manager.getAllPlugins()[self.prevAttentionPluginIndex]
    self.suspend_plugin(plugin.plugin_object, ATTENTION)
    self.prevAttentionPluginIndex = index
    plugin = manager.getAllPlugins()[index]
    self.attentionPluginWidget.setParent(None)
    self.attentionPluginWidget = plugin.plugin_object.get_ui(self.MainWindow.centralWidget(), "attention")
    self.gridLayout.addWidget(self.attentionPluginWidget, 1, 0)
    self.attentionCheckBoxClicked()

  def meditationCheckBoxClicked(self):
    """
    what to do if meditation checkbox is clicked
    """
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    plugin = manager.getAllPlugins()[self.prevMeditationPluginIndex]
    if not self.meditationCheckBox.isChecked():
      self.suspend_plugin(plugin.plugin_object, MEDITATION)
    else:
      plugin.plugin_object.resume(MEDITATION)
 

  def meditationPluginSelected(self, index):
    """
    what to do if a meditation plugin is selected
    """
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    plugin = manager.getAllPlugins()[self.prevMeditationPluginIndex]
    self.suspend_plugin(plugin.plugin_object, MEDITATION)
    self.prevMeditationPluginIndex = index
    plugin = manager.getAllPlugins()[index]
    self.meditationPluginWidget.setParent(None)
    self.meditationPluginWidget = plugin.plugin_object.get_ui(self.MainWindow.centralWidget(), "meditation")
    self.gridLayout.addWidget(self.meditationPluginWidget, 3, 0)
    self.meditationCheckBoxClicked()


  def eyeBlinkCheckBoxClicked(self):
    """
    what to do if the eye blink check box is clicked
    """
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    plugin = manager.getAllPlugins()[self.prevEyeBlinkPluginIndex]
    if not self.eyeBlinkCheckBox.isChecked():
      self.suspend_plugin(plugin.plugin_object, EYEBLINK)
    else:
      plugin.plugin_object.resume(EYEBLINK)

  def eyeBlinkPluginSelected(self, index):
    """
    what to do if an eye blink plugin is selected
    """
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    plugin = manager.getAllPlugins()[self.prevEyeBlinkPluginIndex]
    self.suspend_plugin(plugin.plugin_object, EYEBLINK)
    self.prevEyeBlinkPluginIndex = index
    plugin = manager.getAllPlugins()[index]
    self.eyeBlinkPluginWidget.setParent(None)
    self.eyeBlinkPluginWidget = plugin.plugin_object.get_ui(self.MainWindow.centralWidget(), "eyeBlink")
    self.gridLayout.addWidget(self.eyeBlinkPluginWidget, 5, 0)
    self.eyeBlinkCheckBoxClicked()

  def load_nth_scene(self, n):
    """
    callback function that loads the nth scene from file
    """
    def load_nth_scene_helper():
      filename = "midicontroller/scenes/midicontroller-%d.json" % (n+1)
      self.last_loaded_scene = (n+1)
      self.update_statusbar()
      return self.load_state(filename)
    return load_nth_scene_helper


  def save_nth_scene(self, n):
    """
    callback function that saves the nth scene to file
    """
    def save_nth_scene_helper():
      filename = "midicontroller/scenes/midicontroller-%d.json" % (n+1)
      return self.save_state(filename)
    return save_nth_scene_helper


  def save_state(self, filename):
    """
    get state of ui and all plugins, and save to file
    """
    model = self.serializer.ui_to_model()
    plugin_model = {}
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    for plugin in manager.getAllPlugins():
      name = plugin.plugin_object.name
      plugin_model[name] = plugin.plugin_object.get_state_as_dict(self.MainWindow.centralWidget())
    model['plugins'] = plugin_model
    import json
    modelstring = json.dumps(model, sort_keys=True,
                              indent=4, separators=(",",": "))
    with open(filename, "w") as f:
      f.write(modelstring)

  def load_state(self, filename):
    """
    get state of ui and all plugins from file, and set to the ui
    """
    try:
      with open(filename, "r") as f:
        modelstring = f.read()
    except IOError:
      return

    import json
    model = json.loads(modelstring)
    plugin_model = model['plugins']
    del model['plugins']
    self.serializer.model_to_ui(model)
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()

    for plugin in manager.getAllPlugins():
      for section in SECTIONS:
        self.suspend_plugin(plugin.plugin_object, section)
      name = plugin.plugin_object.name
      if name in plugin_model:
        plugin.plugin_object.set_state_from_dict(self.MainWindow.centralWidget(),plugin_model[name])  
    self.attentionCheckBoxClicked()
    self.meditationCheckBoxClicked()
    self.eyeBlinkCheckBoxClicked()

  def quit_gracefully(self):
    """
    switch off all playing notes and delete all plugins
    """
    for i,mo in enumerate(self.midiOut):
      bytemsg = self.notequeue.clear_notes(i)
      for msg in bytemsg:
        self.midiOut[i].send_message(msg)
    from yapsy.PluginManager import PluginManagerSingleton
    manager = PluginManagerSingleton.get()
    for plugin in manager.getAllPlugins():
      for section in SECTIONS: 
          plugin.plugin_object.stop(section)

  def monitor(self):
    """
    start/stop button pressed
    """
    print "monitor"
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
    """
    react to a poor signal event
    """
    self.signal_quality = "poor signal quality {0}%".format(value)
    self.MainWindow.update_statusbar_signal.emit()

  def handle_good_signal(self, headset, value):
    """
    handle to a good signal event
    """
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
    for p in self.available_ports:
        self.selectAllMidiDevice.addItem(p)
    #if self.available_ports:
    #  for mo in self.midiOut:
    #    mo.open_port(0)

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

  def choose_midi_device_for_all(self):
      value = self.midiAllDevice.currentText()
      idx = self.midiAllDevice.findText(value)
      for i in range(16):
          self.choose_midi_device_for_channel(i)(0)
          if idx != -1:
            self.midiDeviceComboBoxes[i].setCurrentIndex(idx);

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
  
  def reset_button_for_all(self):
      for i in range(16):
          self.reset_button_for_channel(i)(0)

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

  def handle_blink_event(self):
    """
    function to do something if an eye blink event is detected
    """
    if self.eyeBlinkCheckBox.isChecked():
      from yapsy.PluginManager import PluginManagerSingleton
      manager = PluginManagerSingleton.get()
      plugin = manager.getAllPlugins()[self.eyeBlinkPluginComboBox.currentIndex()]
      plugin.plugin_object.trigger("eyeBlink", self.midiOut, self.notequeue, None)
 
  def handle_meditation_event(self, headset, value):
    """
    function to do something when a meditation event is detected
    """
    if self.meditationCheckBox.isChecked():
      from yapsy.PluginManager import PluginManagerSingleton
      manager = PluginManagerSingleton.get()
      plugin = manager.getAllPlugins()[self.meditationPluginComboBox.currentIndex()]
      plugin.plugin_object.trigger("meditation", self.midiOut, self.notequeue, value)

  def handle_attention_event(self, headset, value):
    """
    function to do something when an attention event is detected
    """
    if self.attentionCheckBox.isChecked():
      from yapsy.PluginManager import PluginManagerSingleton
      manager = PluginManagerSingleton.get()
      plugin = manager.getAllPlugins()[self.attentionPluginComboBox.currentIndex()]
      plugin.plugin_object.trigger("attention", self.midiOut, self.notequeue, value)


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
    self.statusbar.showMessage("{0} - {1} - Last loaded scene: {2}".format(self.connected,self.signal_quality,self.last_loaded_scene if self.last_loaded_scene is not None else "None"))

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
