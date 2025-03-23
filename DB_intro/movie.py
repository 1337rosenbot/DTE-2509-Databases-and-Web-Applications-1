class Movie:
    def __init__(self, id, title, year, country, genre, age_rating, duration, price):
        self._id = id
        self._title = title
        self._year = year
        self._country = country
        self._genre = genre
        self._age_rating = age_rating
        self._duration = duration
        self._price = price

    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def year(self):
        return self._year
    
    @property
    def country(self):
        return self._country
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def age_rating(self):
        return self._age_rating
    
    @property
    def duration(self):
        return self._duration
    
    @property
    def price(self):
        return self._price
        