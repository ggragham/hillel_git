import csv
import json
import os

from film_data import films_data
from film_genres import ganres

# Cast string to dict
genresDict = json.loads(ganres)
print(f"{type(genresDict)=}")

# Create dir
dirName = 'dz13'
if not os.path.exists(dirName):
	os.makedirs(dirName)

# Create dirs and CSV files with headers for each genre from genresDict
fieldNames = ['title', 'year', 'rating', 'type', 'genres']
csvFiles = {}
for genre in genresDict['results']:
	genreDirPath = os.path.join(dirName, genre['genre'])
	if not os.path.exists(genreDirPath):
		os.makedirs(genreDirPath)

	# Create a CSV file with headers
	csvFile = open(os.path.join(genreDirPath, 'movies.csv'), 'w', newline='')
	writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
	writer.writeheader()
	csvFiles[genre['genre']] = csvFile

# Add films to the corresponding genre CSV files
for film in films_data:
	genres = [gen['genre'] for gen in film['gen']]
	for genre in genres:
		if genre in csvFiles:
			writer = csv.DictWriter(csvFiles[genre], fieldnames=fieldNames)
			row = {'title': film['title'], 'year': film['year'], 'rating': film['rating'], 'type': film['type'],
			       'genres': ';'.join(genres)}
			writer.writerow(row)

# Close all CSV files
for csvFile in csvFiles.values():
	csvFile.close()
