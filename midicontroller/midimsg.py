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

NOTE_ON = (0b1001 << 4)
NOTE_OFF= (0b1000 << 4)
MONOPRESSURE = (0b1101 << 4)
POLYPRESSURE = (0b1010 << 4)
PROGRAMCHANGE = (0b1100 << 4)
PITCHBEND = (0b1110 << 4)
CONTROLCHANGE = (0b1011 << 4)

BANKSELECT_MSB = 0
MODULATIONWHEEL_MSB = 1
BREATHCONTROLLER_MSB = 2
FOOTCONTROLLER_MSB = 4
PORTAMENTOTIME_MSB = 5
DATAENTRY_MSB = 6
CHANNELVOLUME_MSB = 7
BALANCE_MSB = 8
PAN_MSB = 10
EXPRESSION_MSB = 11
EFFECTCONTROL1_MSB = 12
EFFECTCONTROL2_MSB = 13
GENERALPURPOSECONTROLLER1_MSB = 16
GENERALPURPOSECONTROLLER2_MSB = 17
GENERALPURPOSECONTROLLER3_MSB = 18
GENERALPURPOSECONTROLLER4_MSB = 19
BANKSELECT_LSB = 32
MODULATIONWHEEL_LSB = 33
BREATHCONTROLLER_LSB = 34
FOOTCONTROLLER_LSB = 36
PORTAMENTOTIME_LSB = 37
DATAENTRY_LSB = 38
CHANNELVOLUME_LSB = 39
BALANCE_LSB = 40
PAN_LSB = 42
EXPRESSION_LSB = 43
EFFECTCONTROL1_LSB = 44
EFFECTCONTROL2_LSB = 45
GENERALPURPOSECONTROLLER1_LSB = 48
GENERALPURPOSECONTROLLER2_LSB = 49
GENERALPURPOSECONTROLLER3_LSB = 50
GENERALPURPOSECONTROLLER4_LSB = 51
SUSTAINPEDAL = 64
PORTAMENTOONOFF = 65
SOSTENUTO = 66
SOFTPEDAL = 67
LEGATOFOOTSWITCH = 68
HOLD2 = 69
SOUNDCONTROLLER1 = 70
SOUNDCONTROLLER2 = 71
SOUNDCONTROLLER3 = 72
SOUNDCONTROLLER4 = 73
SOUNDCONTROLLER5 = 74
SOUNDCONTROLLER6 = 75
SOUNDCONTROLLER7 = 76
SOUNDCONTROLLER8 = 77
SOUNDCONTROLLER9 = 78
SOUNDCONTROLLER10 = 79
GENERALPURPOSECONTROLLER5 = 80
GENERALPURPOSECONTROLLER6 = 81
GENERALPURPOSECONTROLLER7 = 82
GENERALPURPOSECONTROLLER8 = 83
PORTAMENTOCONTROL = 84
EFFECTS1DEPTH = 91 # reverb send
EFFECTS2DEPTH = 92 # tremolo depth
EFFECTS3DEPTH = 93 # chorus send
EFFECTS4DEPTH = 94 # celeste (detuning) depth
EFFECTS5DEPTH = 95 # phase depth
DATAINCREMENT = 96
DATADECREMENT = 97
NONREGISTEREDPARAMETERNUMBER_LSB = 98
NONREGISTEREDPARAMETERNUMBER_MSB = 99
REGISTEREDPARAMETERNUMBER_LSB = 100
REGISTEREDPARAMETERNUMBER_MSB = 101
ALLSOUNDOFF = 120
RESETALLCONTROLLERS = 121
LOCALCONTROLONOFF = 122
ALLNOTESOFF = 123
OMNIMODEOFF = 124
OMNIMODEON = 125
POLYMODEOFF = 126
POLYMODEON = 127

class MidiMsg(object):
  def __init__(self):
    pass

  def pack_mask_channel(self, mask, channel):
    return ( mask | (channel & 15) )

  def clip_note(self, note):
    clipped = (note & 127)
    assert (clipped != 0)
    return note

  def clip_velocity(self, note):
    clipped = (note & 127)
    return clipped

  def note_on(self, channel, note, velocity):
    """
    note on message

    channel = 1..16
    note = 1..127
    velocity = 0..127
    """
    msgbytes = []
    if note:
      msgbytes.append(self.pack_mask_channel(NOTE_ON, channel))
      msgbytes.append(self.clip_note(note))
      msgbytes.append(self.clip_velocity(velocity))
    return msgbytes

  def note_off(self, channel, note, release_velocity=64):
    """
    note off message with optional release_velocity (rarely used)
    
    channel = 1..16
    note = 1..127
    release_velocity = 0..127
    """
    msgbytes = []
    msgbytes.append(self.pack_mask_channel(NOTE_OFF, channel))
    msgbytes.append(self.clip_note(note))
    msgbytes.append(self.clip_velocity(release_velocity))
    return msgbytes

  def all_notes_off(self, channel):
    return self.control_change(channel, ALLNOTESOFF, 0)

  def monopressure(self, channel, pressure):
    """
    define pressure (aftertouch) for all notes in channel

    channel = 1..16
    pressure = 0..127
    """
    msgbytes = []
    msgbytes.append(self.pack_mask_channel(MONOPRESSURE, channel))
    msgbytes.append(self.clip_velocity(pressure))
    return msgbytes

  def polypressure(self, channel, note, pressure):
    """
    define pressure for single note 

    channel = 1..16
    note = 1..127
    pressure = 0..127
    """
    msgbytes = []
    msgbytes.append(self.pack_mask_channel(POLYPRESSURE, channel))
    msgbytes.append(self.clip_note(note))
    msgbytes.append(self.clip_velocity(pressure))
    return msgbytes

  def programchange(self, channel, program):
    """
    channel = 1..16
    program = 0..127
    """
    msgbytes = []
    msgbytes.append(self.pack_mask_channel(PROGRAMCHANGE, channel))
    msgbytes.append(self.clip_velocity(program))
    return msgbytes

  def pitchbend(self, channel, value):
    """
    channel = 1..16
    value = 1..16383
    """
    msgbytes = []
    msgbytes.append(self.pack_mask_channel(PITCHBEND, channel))
    msgbytes.append(self.value & 127)  # lsb
    msgbytes.append((self.value >> 7) & 127) # msb
    return msgbytes

  def controlchange(self, channel, control_type, control_change):
    """
    control change message

    channel = 1..16
    control_type = type of control change message (e.g. BANKSELECT)
    """
    msgbytes = []
    msgbytes.append(self.pack_mask_channel(CONTROLCHANGE, channel))
    msgbytes.append(self.clip_velocity(control_type))
    msgbytes.append(self.clip_velocity(control_change))
    return msgbytes

