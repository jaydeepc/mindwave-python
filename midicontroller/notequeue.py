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

import collections
import midimsg

class NoteQueue(object):
  def __init__(self, capacity):
    """
    set up a note queue
    a note queue remembers "capacity" (say: 3) notes
    if a fourth note is played, the oldest note is switched off
    at any time at most capacity notes play simultaneously
    """
    self.capacity = capacity
    self.qs = [collections.deque([(0,0)]*capacity,capacity) for i in range(16)]
    self.notes_inserted = [0 for i in range(16)]
    self.midimsg = midimsg.MidiMsg()

  def play_note(self, channel, note, velocity):
    """
    create a note on message, and remember the note so it can be
    switched off again later on (last capacity notes run in parallel)
    """
    msgbytes = []
    oldest_note = self.qs[channel].pop()
    self.qs[channel].appendleft( (note, velocity) )
    self.notes_inserted[channel] += 1
    msgbytes.append(self.midimsg.note_on(channel, note, velocity))
    if self.notes_inserted[channel] > self.capacity:
        msgbytes.append(self.midimsg.note_off(channel, oldest_note[0], oldest_note[1]))
    return msgbytes

  def clear_notes(self, channel):
    """
    create note off midi msgs for all notes in the channel
    """
    msgbytes = []
    q = self.qs[channel]
    while q:
      oldest_note = q.pop()
      #print oldest_note
      if oldest_note[0]:
        msgbytes.append(self.midimsg.note_off(channel, oldest_note[0], oldest_note[1]))
    self.qs[channel] = collections.deque([(0,0)]*self.capacity,self.capacity)
    self.notes_inserted[channel] = 0
    return msgbytes

  def clear_all_notes(self):
    """
    create note off midi msgs for all notes in all channels
    """
    msgbytes = []
    for i,q in enumerate(self.qs):
      msgbytes.extend(self.clear_notes(i))
    return msgbytes


