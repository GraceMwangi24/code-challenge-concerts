class Band:
    def __init__(self, name, hometown):
        if not  isinstance(name,str) or len(name) == 0:
            raise Exception("invalid input: Name must be of type str with more than zero characters.")
        self._name = name

        if not  isinstance(hometown,str) or len(hometown) == 0:
            raise Exception("invalid input:Hometown must be of type str with more than zero characters.")
        
        self._hometown = hometown
        self._concerts = []
       



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
        return self._concerts
    
    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise Exception("Invalid input: Venue must be of type Venue.")
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        venue.add_concert(concert)
        return concert
    
    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))        
       


class Concert:
    all = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Invalid input: Date must be a non-empty string.")
        if not isinstance(band, Band):
            raise Exception("Invalid input: Band must be an instance of Band.")
        if not isinstance(venue, Venue):
            raise Exception("Invalid input: Venue must be an instance of Venue.")
        Concert.all.append(self)
        self.date = date
        self.band = band
        self.venue = venue
        venue.add_concert(self)
        
        
    @property
    def date(self):
        return self._date   
    @date.setter 
    def date(self, value):
        if not isinstance (value, str) or len(value) == 0: 
            raise Exception("Invalid input: Date must be of type str with more than zero characters.")
        self._date = value

    @property
    def band(self):
        return self._band
    @band.setter
    def band(self,value):
        if not isinstance(value,Band):
            raise Exception("Invalid input : Band must be an instance of Band")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise Exception ("Invalid input: Venue must be an instance of Venue.")   
        self._venue = value 


    def hometown_show(self):
        return self.venue.city == self.band.hometown

       

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
        
      

class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid input: Name must be a non-empty string.")
        if not isinstance(city, str) or len(city) == 0:
            raise Exception("Invalid input: City must be a non-empty string.")
        
        self._name = name
        self._city = city
        self._concerts = [] 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Invalid input: Name must be a non-empty string.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Invalid input: City must be a non-empty string.")
        self._city = value

    def concerts(self):
        return self._concerts 

    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise Exception("Invalid input: Concert must be an instance of Concert.")
        self._concerts.append(concert)

