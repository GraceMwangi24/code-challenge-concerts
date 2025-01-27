class Band:
    def __init__(self, name, hometown):
        if not  isinstance(name,str) or len(name) == 0:
            raise Exception("invalid input: Name must be of type str with more than zero characters.")
        self._name = name
        if not  isinstance(hometown,str) or len(hometown) == 0:
            raise Exception("invalid input:Hometown must be of type str with more than zero characters.")
        
        self._hometown = hometown



    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Invalid input: Name must be of type str with more than zero characters.")
        self._name = value
    

    @property
    def hometown(self):
        return self._hometown   

    def concerts(self):
        pass

    def venues(self, name, city):
        if not  isinstance(name,str) or len(name) == 0:
            raise Exception("invalid input: Name must be of type str with more than zero characters.")
        self._name = name
        if not  isinstance(city,str) or len(name) == 0:
            raise Exception("invalid input: Name must be of type str with more than zero characters.")
        self._city = city

    @property
    def name (self):
        return self._name

    @name.setter 
    def name(self,value):
        if not  isinstance(value,str) or len(value) == 0:
            raise Exception("invalid input: Name must be of type str with more than zero characters.")
        self._name = value
    
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value,str) or len(value) ==0:
            raise Exception("invalid input : City  must be of type str with more than zero characters ") 
        self._city = value   


 
        

    def play_in_venue(self, venue, date):
        pass

    def all_introductions(self):
        pass


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        pass

    def introduction(self):
        pass


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def concerts(self):
        pass

    def bands(self):
        pass
