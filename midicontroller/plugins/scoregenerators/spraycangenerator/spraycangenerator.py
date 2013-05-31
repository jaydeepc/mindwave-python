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

from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManagerSingleton
import parseutils

from PyQt4 import QtGui
from mainwindow import Ui_Panel

class SprayCanGenerator(IPlugin):

  name = "Spray Can Generator"

  def __init__(self):
    super(SprayCanGenerator, self).__init__()
    self.parseutil = parseutils.ParseUtil()
    self.instances = {}
    self.s = {}

  def get_ui(self, parent, name):
    Panel = QtGui.QWidget(parent)
    ui = Ui_Panel()
    ui.setupUi(Panel)
    self.instances[name] = ui 
    return Panel

  def get_state_as_dict(self):
    result = {}
    for name in self.instances:
      Panel = self.instances[name]
      result[name] = {}
      result[name]["midiChannelEdit"] = "{0}".format(Panel.midiChannelEdit.text())
      result[name]["allowedVelsEdit"] = "{0}".format(Panel.allowedVelsEdit.text())
      result[name]["centralNoteEdit"] = "{0}".format(Panel.centralNoteEdit.text())      
      result[name]["spreadEdit"] = "{0}".format(Panel.spreadEdit.text())
      result[name]["notesPerSecondEdit"] = "{0}".format(Panel.notesPerSecondEdit.text())
      result[name]["maxJitterEdit"] = "{0}".format(Panel.maxJitterEdit.text())

    return result

  def set_state_from_dict(self, dct):
    for name in dct:
      Panel = self.instances[name]
      Panel.midiChannelEdit.setText("{0}".format(dct[name]["midiChannelEdit"]))
      Panel.allowedVelsEdit.setText("{0}".format(dct[name]["allowedVelsEdit"]))
      Panel.centralNoteEdit.setText("{0}".format(dct[name]["centralNoteEdit"]))
      Panel.spreadEdit.setText("{0}".format(dct[name]["spreadEdit"]))
      Panel.notesPerSecondEdit.setText("{0}".format(dct[name]["notesPerSecondEdit"]))
      Panel.maxJitterEdit.setText("{0}".format(dct[name]["maxJitterEdit"]))


  def trigger(self, name, midiOuts, notequeue, value):
    Panel = self.instances[name]
    midichan = self.parseutil.parse_midi_channel_list(Panel.midiChannelEdit.text())
    #print "midi channel: ", midichan
    if not midichan:
      return

    vels = self.parseutil.parse_number_ranges(Panel.allowedVelsEdit.text())
    #print "velocities: ", vels
    if not vels:
      return

    values = self.parseutil.parse_number_ranges(Panel.centralNoteEdit.text())
    if value:
      values.append(value)
    #print "central note: ", values
    if not values:
      return

    spreads = self.parseutil.parse_midi_channel_list(Panel.spreadEdit.text())
    #print "Spreads ", spreads
    if not spreads:
      return

    notesPerSecond = self.parseutil.parse_int(Panel.notesPerSecondEdit.text())
    #print "notes per sec: ", notesPerSecond
    if not notesPerSecond:
      return

    maxJitter = self.parseutil.parse_list_float(Panel.maxJitterEdit.text())
    #print "max jitter: ", maxJitter
    if not maxJitter:
      return

    import synththread

    if name in self.s:
      self.s[name].stop()
      self.s[name].join()

    self.s[name] = synththread.SynthThread(midiOuts, notequeue, midichan, values, vels, spreads, notesPerSecond, maxJitter)
    self.s[name].start()
    
  def stop(self, name):
    if name in self.s:
      self.s[name].stop()
      self.s[name].join()
      del self.s[name]


