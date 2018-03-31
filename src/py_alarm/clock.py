class _Time:
  def __init__(self, time:str):
    self.hours = int(time[0:2])
    self.mins = int(time[3:4])

class Clock:
  def sound(self, time_string:str) -> str:
    time = _Time(time_string)
    return self.getString(time)

  #type hints need the type defined further up
  def getString(self, time:_Time):
      if time.hours == 7 and time.mins == 0:
        return "wake up!"
      elif time.mins == 0:
        return "beep"
      else:
        return "tick"
