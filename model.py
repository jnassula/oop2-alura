class Program:
    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year



class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__like = 0

    @property
    def likes(self):
        return self.__like

    def give_likes(self):
        self.__like += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name




class Serie:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__like = 0

    @property
    def likes(self):
        return self.__like

    def give_likes(self):
        self.__like += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



avengers = Movie('avengers - infinity war', 2018, 160)
print(f"Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration}")

ricky = Serie ('Ricky and Morty', 2018, 4)
print(f"Name: {ricky.name} - Year: {ricky.year} - Seasons: {ricky.seasons}")