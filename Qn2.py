class clockTime:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    def setHours(self,hours):
        self.hours = hours
    def setMinutes(self,minutes):
        self.minutes = minutes
    def setSeconds(self,seconds):
        self.seconds = seconds
    def setTime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def showTime(self):
        print(f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}')

clock = clockTime()
while True:
    try:
        hour = int(input("Enter hour in 24h format (0-23): "))
        if hour >= 0 and hour <= 23:
            break
        print("Wrong Format")
    except Exception as e:
        print(e)
clock.setHours(hour)
while True:
    try:
        minutes = int(input("Enter minutes (0-59): "))
        if minutes >= 0 and minutes <= 59: 
            break
        print("Wrong Format")
    except Exception as e:
        print(e)
clock.setMinutes(minutes)
while True:
    try:
        seconds = int(input("Enter seconds (0-59): "))
        if seconds >= 0 and seconds <= 59: 
            break
        print("Wrong Format")
    except Exception as e:
        print(e)
clock.setSeconds(seconds)
clock.showTime()

#test setTime by reset to 00:00:00
clock.setTime(0, 0, 0)
clock.showTime()
