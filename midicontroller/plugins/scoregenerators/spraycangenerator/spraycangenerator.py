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
    self.props = {}
    self.playing_suspended = {} 

  def get_ui(self, parent, name):
    Panel = QtGui.QWidget(parent)
    ui = Ui_Panel()
    ui.setupUi(Panel)
    self.instances[name] = (ui,Panel) 
    return Panel

  def get_state_as_dict(self):
    result = {}
    for name in self.instances:
      ui = self.instances[name][0]
      result[name] = {}
      result[name]["midiChannelEdit"] = "{0}".format(ui.midiChannelEdit.text())
      result[name]["allowedVelsEdit"] = "{0}".format(ui.allowedVelsEdit.text())
      result[name]["centralNoteEdit"] = "{0}".format(ui.centralNoteEdit.text())      
      result[name]["spreadEdit"] = "{0}".format(ui.spreadEdit.text())
      result[name]["notesPerSecondEdit"] = "{0}".format(ui.notesPerSecondEdit.text())
      result[name]["maxJitterEdit"] = "{0}".format(ui.maxJitterEdit.text())

    return result

  def set_state_from_dict(self, dct):
    for name in dct:
      ui = self.instances[name][0]
      ui.midiChannelEdit.setText("{0}".format(dct[name]["midiChannelEdit"]))
      ui.allowedVelsEdit.setText("{0}".format(dct[name]["allowedVelsEdit"]))
      ui.centralNoteEdit.setText("{0}".format(dct[name]["centralNoteEdit"]))
      ui.spreadEdit.setText("{0}".format(dct[name]["spreadEdit"]))
      ui.notesPerSecondEdit.setText("{0}".format(dct[name]["notesPerSecondEdit"]))
      ui.maxJitterEdit.setText("{0}".format(dct[name]["maxJitterEdit"]))


  def trigger(self, name, midiOuts, notequeue, value):

    if name not in self.instances:
      return

    if name in self.playing_suspended and self.playing_suspended[name]:
      return

    self.props[name] =  (midiOuts, notequeue, value)

    ui = self.instances[name][0]
    midichan, headsetpresent = self.parseutil.parse_midi_channel_list(ui.midiChannelEdit.text())
#    print "midi channel: ", midichan
    if headsetpresent and value:
      midichan.append(value)
    if not midichan:
      return

    vels,headsetpresent = self.parseutil.parse_number_ranges(ui.allowedVelsEdit.text())
#    print "velocities: ", vels
    if headsetpresent and value:
      vels.append(value)
    if not vels:
      return

    values,headsetpresent = self.parseutil.parse_number_ranges(ui.centralNoteEdit.text())
    if headsetpresent and value:
      values.append(value)
#    print "central note: ", values
    if not values:
      return

    spreads,headsetpresent = self.parseutil.parse_midi_channel_list(ui.spreadEdit.text())
#    print "Spreads ", spreads
    if headsetpresent and value:
      spreads.append(value)
    if not spreads:
      return

    notesPerSecond,headsetpresent = self.parseutil.parse_int(ui.notesPerSecondEdit.text())
#    print "notes per sec: ", notesPerSecond
    if headsetpresent and value:
      notesPerSecond.append(value)
    if not notesPerSecond:
      return

    maxJitter,headsetpresent = self.parseutil.parse_list_float(ui.maxJitterEdit.text())
#    print "max jitter: ", maxJitter
    if headsetpresent and value:
      maxJitter.append(value)
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
    if name in self.instances:
      del self.instances[name]

  def suspend(self, name):
    if name in self.s:
      self.s[name].stop()
      self.s[name].join()
      self.playing_suspended[name] = True

  def is_suspended(self, name):
    return name in self.playing_suspended and self.playing_suspended[name]

  def resume(self, name):
    self.playing_suspended[name] = False
    if name in self.playing_suspended and self.playing_suspended[name]:
      self.trigger(name, *self.props[name])

  def get_midi_channel_list(self, name):
    if name in self.instances:
      ui = self.instances[name][0]
      midichan, headsetpresent = self.parseutil.parse_midi_channel_list(ui.midiChannelEdit.text())
      return midichan
    return []



