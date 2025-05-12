

class Date:
    
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    def __eq__(self,other):
        if (self.year == other.year and self.month == other.month and self.day == other.day):
            return True
        return False

    def __lt__(self,other):
        if (self.year < other.year):
            return True
        if (self.year == other.year and self.month < other.month):
            return True
        if (self.year == other.year and self.month == other.month and self.day < other.day):
            return True
        return False

    def __le__(self,other):
        if (self.year <= other.year):
            return True
        if (self.year == other.year and self.month <= other.month):
            return True
        if (self.year == other.year and self.month == other.month and self.day <= other.day):
            return True
        return False
