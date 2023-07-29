import os


class Film:
	def __init__(self, title, imdbRating, year, trailerLink):
		self.title = title
		self.imdbRating = imdbRating
		self.year = year
		self.trailerLink = trailerLink

		# Path to the folder with the letter
		self.storageAddress = os.path.join('./film_player/film_storage',
		                                   title[0].upper(),
		                                   f"{title.replace(' ', '_')}.txt")

		# Create txt file
		self.uploadFile()

	def printDetails(self):
		print(f"Title: {self.title}")
		print(f"IMDb rating: {self.imdbRating}")
		print(f"Year: {self.year}")
		print(f"Trailer link: {self.trailerLink}")

	def uploadFile(self):
		# Create dir if not exist
		os.makedirs(os.path.dirname(self.storageAddress), exist_ok=True)

		# Create file with film data
		with open(self.storageAddress, 'w') as file:
			file.write(f"Title: {self.title}\n")
			file.write(f"IMDb rating: {self.imdbRating}\n")
			file.write(f"Year: {self.year}\n")
			file.write(f"Trailer link: {self.trailerLink}\n")

	def getFilmAddress(self):
		return self.storageAddress
