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

class SimpleGenerator(IPlugin):

  name = "Simple Generator"

  def __init__(self):
    super(SimpleGenerator, self).__init__()
    self.parseutil = parseutils.ParseUtil()
    self.instances = {}

  def get_ui(self, parent, name):
    Panel = QtGui.QWidget(parent)
    ui = Ui_Panel()
    ui.setupUi(Panel)
    self.instances[name] = (ui, Panel)
    return Panel

  def get_state_as_dict(self):
    result = {}
    for name in self.instances:
      ui = self.instances[name][0]
      result[name] = {}
      result[name]["midiChannelEdit"] = "{0}".format(ui.midiChannelEdit.text())
      result[name]["allowedVelsEdit"] = "{0}".format(ui.allowedVelsEdit.text())
      result[name]["allowedNotesEdit"] = "{0}".format(ui.allowedNotesEdit.text())
    return result

  def set_state_from_dict(self, dct):
    for name in dct:
      ui = self.instances[name][0]
      ui.midiChannelEdit.setText("{0}".format(dct[name]["midiChannelEdit"]))
      ui.allowedVelsEdit.setText("{0}".format(dct[name]["allowedVelsEdit"]))
      ui.allowedNotesEdit.setText("{0}".format(dct[name]["allowedNotesEdit"]))

  def trigger(self, name, midiOuts, notequeue, value):
    ui = self.instances[name][0]
    midichan = self.parseutil.parse_midi_channel_list(ui.midiChannelEdit.text())
    if not midichan:
      return
    vels = self.parseutil.parse_number_ranges(ui.allowedVelsEdit.text())

    if not vels:
      return
    values = self.parseutil.parse_number_ranges(ui.allowedNotesEdit.text())
    if value:
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

  def stop(self, name):
    if name in self.instances:
      del self.instances[name]
    pass
