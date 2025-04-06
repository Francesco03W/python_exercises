class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def __str__(self):
        return (f'{self.year}-{self.month}-{self.day}')
    #rendere classe Date "Totally ordered set of objects" ossia,
    # gli oggetti sono confrontabili in tutti i modi: overload operatori di confronto
    def __eq__(self,other):
       return(True if self.year == other.year and self.month == other.month and self.day == other.day else False)
    
    def __lt__(self,other):
        #si può comporre un numero dove:
        #anno: più significativo
        #mese: tra anno e mese
        #giorno: meno significativo
        #si può usare un confronto numerico formando un numero così?
        #annomesegiorno, non ci sono incongruenze come con la somma tipo mese>giorno, perché si tiene conto dell'importanza..
        #1933,5,1 > 1933,1,5? Si, 193351>193315
        #1933,1,5 > 1933,1,12? No, 193315>1933112
        #1933,2,28 > 2025,1,1? No, 1933228>202511 non va bene ! n° cifre!
       return( False if self.year > other.year or (self.year == other.year and self.month > other.month) or (self.year == other.year and self.month == other.month and self.day >= other.day) else True) 

    def __le__(self,other):
       return( False if self.year > other.year or (self.year == other.year and self.month > other.month) or (self.year == other.year and self.month == other.month and self.day > other.day) else True) 


