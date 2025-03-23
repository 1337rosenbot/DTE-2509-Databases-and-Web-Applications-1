class Book():
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def year(self):
        return self._year
        