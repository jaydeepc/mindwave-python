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

import notelookup

class ParseUtil(object):
  def __init__(self):
    self.notelookup = notelookup.NoteLookup()

  def cleanup(self, text):
    cl = "{0}".format(text).lower().strip()
    cl = cl.replace(" ","")
    cl = cl.replace("\t","")
    cl = cl.replace("\n","")
    cl = cl.replace("\r","")
    return cl

  def parse_midi_channel_list(self, text):
    """
    parse "1,2 , 3, 4 ,5" into ([1,2,3,4,5], False)
    parse "1,  2, $,3  ,4"  into ([1,2,3,4], True)
    """
    chans = []
    headsetpresent = False
    text = self.cleanup(text)
    ms_split = "{0}".format(text).split(",")
    for c in ms_split:
      try:
        channel = int(c)
        chans.append(channel)
      except ValueError:
        if c == '$':
          headsetpresent = True
    return chans, headsetpresent

  def parse_number_ranges(self, text):
    """
    parse "4:8:2, a4:c#5:2" into [4,6,8,69,71,73]
    """
    values = []
    headsetpresent = False
    text = self.cleanup(text)
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
          if colon_split[0] == '$':
            headsetpresent = True
          else:
            start = self.notelookup.lookup(colon_split[0])
            stop = start
            step = 1
        if start is not None and stop is not None:
          values.extend( [start+i*step for i in range((stop-start)/step+1)])
    except ValueError:
      values = []
 
#    print values, headsetpresent
    return values, headsetpresent

  def parse_int(self, text):
    text = self.cleanup(text)
    if text == "$":
      headsetpresent = True
    else:
      headsetpresent = False

    value = []
    try:
      value = [int(text)]
    except ValueError:
      value = []
    return value, headsetpresent

  def parse_list_float(self, text):
    text = self.cleanup(text)
    vals = []
    headsetpresent = False
    for i in text.split(","):
      try: 
        f = float(i)
        vals.append(f)
      except ValueError:
        if i == "$":
          headsetpresent = True
    return vals, headsetpresent

