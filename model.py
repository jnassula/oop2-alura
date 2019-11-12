class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._like = 0

    @property
    def likes(self):
        return self._like

    def give_likes(self):
        self._like += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Movie(Program):
    def __init__(self, name, year, duration):
        self._name = name.title()
        self.year = year
        self.duration = duration
        self._like = 0


class Serie(Program):
    def __init__(self, name, year, seasons):
        self._name = name.title()
        self.year = year
        self.seasons = seasons
        self._like = 0



avengers = Movie('avengers - infinity war', 2018, 160)
print(f"Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration}")

ricky = Serie ('Ricky and Morty', 2018, 4)
print(f"Name: {ricky.name} - Year: {ricky.year} - Seasons: {ricky.seasons}")