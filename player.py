import os
import string

from film_data import films_data
from film_player.films_worker import Film
from film_player.media_player import Player

filmDirPath = "./film_player/film_storage/"
os.makedirs(filmDirPath, exist_ok=True)

# Create dirs from 'A' to 'Z' inside each dir
for letter in string.ascii_uppercase:
	letterDirPath = os.path.join(filmDirPath, letter)
	if not os.path.exists(letterDirPath):
		os.makedirs(letterDirPath)

# Create new player instance
player = Player("Main Player")


def getFilmByTitle(title):
	for filmData in films_data:
		if filmData['title'] == title:
			return filmData
	return None


# Get film info from film_data.py
filmInfo = getFilmByTitle('The Mummy')
duration = 152

if filmInfo:
	# "Play" film
	player.Play(filmInfo['trailer'], duration)
	print(f"Video exist: {player.isPlaying}")  # Print true if video exits

	# Create Film class instance
	film = Film(
		filmInfo['title'],
		filmInfo['rating'],
		filmInfo['year'],
		filmInfo['trailer']
	)

	# Print film info
	film.printDetails()

	# Print film file location
	print(film.getFilmAddress())
else:
	print("Film not found.")
