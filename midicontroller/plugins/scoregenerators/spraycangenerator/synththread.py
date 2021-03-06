import threading 

class SynthThread(threading.Thread):
  """
  helper class to synthesis a flurry of midi events in the absence of external stimuli
  """
  def __init__(self, midiOuts, notequeue, midiChan, values, vels, spreads, notesPerSecond, maxJitter):
    """
    initialize the synthesis thread
    """
    threading.Thread.__init__(self)
    self.midiOuts = midiOuts
    self.notequeue = notequeue
    self.midiChan = midiChan
    self.values = values
    self.vels = vels
    self.spreads = spreads
    self.notesPerSecond = notesPerSecond
    self.maxJitter = maxJitter
    self.stop_processing = False

  def run(self):
    """
    start synthesizing midi events
    """
    #print "RUN"
    import random
    while not self.stop_processing:
      chan = random.choice(self.midiChan)
      sign = random.choice([1,-1])
      value = random.choice(self.values)+(sign*random.choice(self.spreads))
      vel = random.choice(self.vels)
      msgbytes = self.notequeue.play_note(
          chan,
          value,
          vel)
      for msg in msgbytes:
        #print "send"
        self.midiOuts[chan].send_message(msg)
      import time
      sign = random.choice([1,-1])
      time.sleep(1.0/(random.choice(self.notesPerSecond)+(sign*random.choice(self.maxJitter))))

  def stop(self):
    """
    stop synthesizing midi events
    """
    #print "STOP"
    self.stop_processing = True

