import os
import string

from film_awards import films_awards
from film_titles import films_titles

# Create dir
dirName = 'Harry Potter'
if not os.path.exists(dirName):
	os.makedirs(dirName)

# Create dirs for each movie from film_titles.py
for film in films_titles['results']:
	filmDirPath = os.path.join(dirName, film['title'])
	if not os.path.exists(filmDirPath):
		os.makedirs(filmDirPath)

	# Create dirs from 'A' to 'Z' inside each dir
	for letter in string.ascii_uppercase:
		letterDirPath = os.path.join(filmDirPath, letter)
		if not os.path.exists(letterDirPath):
			os.makedirs(letterDirPath)

# Create list with award dicts
filmsAwardList = []
for filmAward in films_awards:
	for result in filmAward['results']:
		# Extract film title
		title = result['movie']['title']

		awardDict = {
			'type': result['type'],
			'award_name': result['award_name'],
			'award': result['award'],
		}

		# Add award dict to the list of awards for this film
		for film in filmsAwardList:
			if film['title'] == title:
				film['awards'].append(awardDict)
				break
		else:
			filmsAwardList.append({'title': title, 'awards': [awardDict]})

# Sort each list of dicts by 'award_name' key
for filmDict in filmsAwardList:
	filmDict['awards'] = sorted(filmDict['awards'], key=lambda x: x['award_name'])

# Create a txt file for each film in dirs labeled from 'A' to 'Z'
for filmDict in filmsAwardList:
	film = filmDict['title']
	awards = filmDict['awards']
	filmDirPath = os.path.join(dirName, film)

	for award in awards:
		firstAwardLetter = award['award_name'][0].upper()
		letterDirPath = os.path.join(filmDirPath, firstAwardLetter)
		awardFilePath = os.path.join(letterDirPath, f"{award['award_name']}.txt")

		# Add award if they are not in the file
		if os.path.exists(awardFilePath):
			with open(awardFilePath, 'r') as file:
				if award['award'] + '\n' in file.readlines():
					continue

		# Open award file in append mode (or create, if doesn't exist)
		with open(awardFilePath, 'a') as file:
			file.write(award['award'] + '\n')

# Remove empty directories
for root, dirs, _ in os.walk(dirName):
	for checkDir in dirs:
		filmDirPath = os.path.join(root, checkDir)
		if not os.listdir(filmDirPath):
			os.rmdir(filmDirPath)
