import json


class MapMagic:
	def __init__(self):
		self.__map_open = "I solemnly swear that I am up to no good."
		self.__map_close = "Mischief managed."


class MarauderMap(MapMagic):
	def __init__(self, path, films_awards, films_titles):
		super().__init__()
		self.path = path
		self.films_awards = films_awards
		self.films_titles = films_titles
		self.__save_films_awards()

	def __save_films_awards(self):
		with open(self.path, 'w') as f:
			json.dump(self.films_awards, f)

	def map_generator(self, main_func):
		print(self._MapMagic__map_open)
		main_func(self.films_awards, self.films_titles)
		print(self._MapMagic__map_close)
