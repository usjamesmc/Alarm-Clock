

class AlarmClock:

    def __init__(self):
        self.current_time = ''
        self.condition = 'off'
        self.set_time = ''
    def change_time(self):
        self.current_time = 1205
    def toggle(self):
        self.condition = 'on'
    def toggle(self):
        self.condition = 'off'

    def change_time(self):
        time = 1200
        hello_time = True
        while hello_time is True:
            print(time)
            if time == 1205: 
                hello_time = False
                print(time)
            else: 
                time += 1 
                print(time)
        self.current_time = 1205
    def toggle(self):
        if self.condition == 'off':
            self.condition = 'on'
        else:
            self.condition = 'off'
    def set_alarm(self):
        time = 1100
        sleep_time = True
        while sleep_time is True:
            print(time)
            if time == 1115: 
                sleep_time = False
                print(time)
            else: 
                time += 1 
                print(time)
        self.current_time = 1205


        
    
    