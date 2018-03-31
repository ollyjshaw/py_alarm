class Clock:
  def sound(self, time_string):
    time = _Time(time_string)
    if (time.hours == 7 and time.mins == 0):
      return "wake up!"
    elif time.mins == 0:
      return "beep"
    else:
      return "tick"

class _Time:
  def __init__(self, time):
    self.hours = int(time[0:2])
    self.mins = int(time[3:4])