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

  def activate(self):
    print "SimpleGenerator plugin activated"

  def deactivate(self):
    print "SimpleGenerator plugin deactivated"

  def get_ui(self, parent, name):
    Panel = QtGui.QWidget(parent)
    ui = Ui_Panel()
    ui.setupUi(Panel)
    print "Created Panel ", Panel
    self.instances[name] = ui 
    return Panel

  def trigger(self, name, midiOuts, notequeue, value):
    Panel = self.instances[name]
    print Panel.midiChannelEdit.text()
    midichan = self.parseutil.parse_midi_channel_list(Panel.midiChannelEdit.text())
    if not midichan:
      return
    vels = self.parseutil.parse_number_ranges(Panel.allowedVelsEdit.text())
    if not vels:
      return
    values = self.parseutil.parse_number_ranges(Panel.allowedNotesEdit.text())
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

