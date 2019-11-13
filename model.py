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

    def __str__(self):
        return f'Nome: {self.name} - Likes: {self.likes}'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Nome: {self.name} - {self.duration} - Likes: {self.likes}'



class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Nome: {self.name} - {self.seasons} - Likes: {self.likes}'




avengers = Movie('avengers - infinity war', 2018, 160)
ricky = Serie ('Ricky and Morty', 2018, 4)

avengers.give_likes()
avengers.give_likes()
avengers.give_likes()

ricky.give_likes()
ricky.give_likes()

movies_and_series = {avengers, ricky}

for program in movies_and_series:
    print(program)
