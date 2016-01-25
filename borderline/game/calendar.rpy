init -2 python:
    class SimpleCalendar():

        months = [
            ["January", 31],
            ["Februrary", 28],
            ["March", 31],
            ["April", 30],
            ["May", 31],
            ["June", 30],
            ["July", 31],
            ["August", 31],
            ["September", 30],
            ["October", 31],
            ["November", 30],
            ["December", 31]]

        def __init__(self, day, month):
            self.day = day
            for m in self.months:
                if (month == m[0]):
                    self.month = m

        # changes the number of days based on variable 't'
        def change_days(self, t):
            for i in range(1, t+1):
                new_day = self.day + 1
                if (new_day > self.month[1]):
                    if (self.month == self.months[11]):
                        self.month = self.months[0]
                    else:
                        self.month = self.months[self.months.index(self.month) + 1]

                    self.day = new_day - self.day

                else:
                    self.day += 1
        
        def get_month(self):
            return self.month[0]