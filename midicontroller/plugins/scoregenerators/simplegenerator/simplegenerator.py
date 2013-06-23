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

import sys
import os
sys.path += [os.path.normpath(os.path.join(os.path.abspath(__file__), "..", "..", "..", ".."))]

from yapsy.IPlugin import IPlugin
import parseutils

from PyQt4 import QtGui
from mainwindow import Ui_Panel

class SimpleGenerator(IPlugin):

  name = "Simple Generator"

  def __init__(self):
    """
    set up simple generator plugin
    """
    super(SimpleGenerator, self).__init__()
    self.parseutil = parseutils.ParseUtil()
    self.instances = {}
    self.playing_suspended = {} 

  def get_ui(self, parent, name):
    """
    create the ui for embedding in main ui
    keep a reference for later usage
    """
    if name in self.instances:
      return self.instances[name][1]

    Panel = QtGui.QWidget(parent)
    ui = Ui_Panel()
    ui.setupUi(Panel)
    self.instances[name] = (ui, Panel)
    return Panel

  def get_state_as_dict(self, parent):
    """
    return internal state of the plugin as a dictionary;
    used during save state to file
    """
    result = {}
    for name in self.instances:
      if name not in self.instances:
        self.get_ui(parent, name)
      ui = self.instances[name][0]
      result[name] = {}
      result[name]["midiChannelEdit"] = "{0}".format(ui.midiChannelEdit.text())
      result[name]["allowedVelsEdit"] = "{0}".format(ui.allowedVelsEdit.text())
      result[name]["allowedNotesEdit"] = "{0}".format(ui.allowedNotesEdit.text())
    return result

  def set_state_from_dict(self, parent, dct):
    """
    set internal state of the plugin from a dictionary;
    used during load state from file
    """
    for name in dct:
      if name not in self.instances:
        self.get_ui(parent, name)
      ui = self.instances[name][0]
      ui.midiChannelEdit.setText("{0}".format(dct[name]["midiChannelEdit"]))
      ui.allowedVelsEdit.setText("{0}".format(dct[name]["allowedVelsEdit"]))
      ui.allowedNotesEdit.setText("{0}".format(dct[name]["allowedNotesEdit"]))

  def trigger(self, name, midiOuts, notequeue, value):
    """
    method called by the main program to ask the plugin to do something
    """
    if name not in self.instances:
      return

    if name in self.playing_suspended and self.playing_suspended[name]:
      return

    ui = self.instances[name][0]
    midichan,headsetpresent = self.parseutil.parse_midi_channel_list(ui.midiChannelEdit.text())
    if headsetpresent and value:
      if not midichan:
        midichan = []
      midichan.append(value)
    if not midichan:
      return

    vels,headsetpresent = self.parseutil.parse_number_ranges(ui.allowedVelsEdit.text())
    if headsetpresent and value:
      if not vels:
        vels = []
      vels.append(value)
    if not vels:
      return

    values,headsetpresent = self.parseutil.parse_number_ranges(ui.allowedNotesEdit.text())
    if headsetpresent and value:
      if not values:
        values = []
      values.append(value)
    if not values:
      return

    import random
    chan = random.choice(midichan)
    value= random.choice(values)
    vel  = random.choice(vels)

    msgbytes  = notequeue.play_note( 
                  chan, 
                  value,
                  vel)

    #print "send midi msg: ", msgbytes
    for msg in msgbytes:
      midiOuts[chan].send_message(msg)

  def suspend(self, name):
    """
    suspend generating music while not deleting the plugin
    """
    self.playing_suspended[name] = True

  def resume(self, name):
    """
    resume generating music
    """
    self.playing_suspended[name] = False

  def is_suspended(self, name):
    """
    true if plugin is currently suspended
    """
    return name in self.playing_suspended and self.playing_suspended[name]

  def stop(self, name):
    """
    stop and delete plugin
    """
    if name in self.instances:
      del self.instances[name]

  def get_midi_channel_list(self, name):
    """
    return a list of all channels this plugin can write midi msgs to
    """
    if name in self.instances:
      ui = self.instances[name][0]
      midichan,headsetpresent = self.parseutil.parse_midi_channel_list(ui.midiChannelEdit.text())
      return midichan
    return []

