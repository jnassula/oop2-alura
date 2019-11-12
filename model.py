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
        super().__init__(name, year)
        self.duration = duration



class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons




avengers = Movie('avengers - infinity war', 2018, 160)
ricky = Serie ('Ricky and Morty', 2018, 4)

avengers.give_likes()
avengers.give_likes()
avengers.give_likes()

ricky.give_likes()
ricky.give_likes()

print(f'Nome: {avengers.name} - Likes: {avengers.likes}')
print(f'Nome: {ricky.name} - Likes: {ricky.likes}')
