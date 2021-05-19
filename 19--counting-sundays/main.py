SUNDAY = 6

def main():
    # 1 Jan 1900 was a Monday
    REFERENCE_DATE = Date(1900, 1, 1, 0)

    # date = 1 Jan 1901
    date = REFERENCE_DATE
    while not date.equals(1901, 1, 1):
        date = date.tomorrow()

    total = 0
    while not date.equals(2001, 1, 1):
        if date.weekday == SUNDAY and date.day == 1:
            total += 1
        date = date.tomorrow()
    print(total)

class Month:
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class Date:
    # month: 1-indexed (January = 1)
    # weekday: Monday = 0 ... Sunday = 6
    def __init__(self, year, month, day, weekday):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

    def tomorrow(self):
        last_day = Date.num_days(self.year, self.month)
        next_weekday = (self.weekday + 1) % 7
        if self.day < last_day:
            return Date(self.year,   self.month,   self.day+1, next_weekday)
        elif self.month < 12:
            return Date(self.year,   self.month+1, 1,          next_weekday)
        else:
            return Date(self.year+1, 1,            1,          next_weekday)

    @staticmethod
    def num_days(year, month):
        # Thirty days has...
        if month in [Month.SEPTEMBER, Month.APRIL, Month.JUNE, Month.NOVEMBER]:
            return 30
        # All the rest have thirty-one
        elif month != Month.FEBRUARY:
            return 31
        # Saving February alone...
        else:
            is_leap_year = Date.is_leap_year(year)
            return 29 if is_leap_year else 28

    @staticmethod
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    # Using a userspace-named method instead of __eq__ because the latter approach would require
    # creating Date objects (which require known weekday) for any comparisons
    def equals(self, year, month, day):
        return self.year == year and self.month == month and self.day == day

if __name__ == '__main__':
    main()
