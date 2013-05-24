import string

class NoteLookup(object):
  def __init__(self):
    self.chromatic_scale_notes = [
        [ "C", "B#", "Dbb" ],
        [ "C#", "Bx", "Db" ],
        [ "D", "Cx", "Ebb" ],
        [ "D#", "Eb", "Fbb"],
        [ "E", "Dx", "Fb" ],
        [ "F", "E#", "Gbb"],
        [ "F#", "Ex", "Gb"],
        [ "G", "Fx", "Abb"],
        [ "G#", "Ab"      ],
        [ "A", "Gx", "Bbb"],
        [ "A#", "Bb", "Cbb"],
        [ "B", "Ax", "Cb"]
        ]
    self.lookup_table = {}
    for octave in [-1,2,3,4,5,6,7,8,9]:
      for i,equiv_note in enumerate(self.chromatic_scale_notes):
        for n in equiv_note:
          notename  = "{0}{1}".format(n,octave)
          notenumber= (octave+1)*12 + i
          if 0 <= notenumber <= 127:
            self.lookup_table["{0}".format(notename)] = notenumber
            self.lookup_table[string.lower("{0}".format(notename))] = notenumber
    
  def lookup(self, note):
    try:
      return int(note)
    except ValueError:
      try:
        return self.lookup_table[note]
      except KeyError:
        try:
          return self.lookup_table[string.lower("{0}".format(note))]
        except KeyError:
          return None

    return None


if __name__ == "__main__":
  n = NoteLookup()
  assert n.lookup("C-1") == 0
  assert n.lookup("F-1") == 5
  assert n.lookup("A#7") == 106
  assert n.lookup("Bbb4") == 69
  assert n.lookup("bbb4") == 69
  assert n.lookup("6") == 6
  print n.lookup("c#5") 
