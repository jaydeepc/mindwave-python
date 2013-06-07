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

# NOTE: duplicated from ../../.. -> need to find out how to use code from parent folders with yapsy

import notelookup

class ParseUtil(object):
  def __init__(self):
    self.notelookup = notelookup.NoteLookup()

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


