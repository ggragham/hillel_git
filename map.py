from film_awards import films_awards
from film_titles import films_titles
from main import main
from spells.marauder_map import MarauderMap

marauder_map = MarauderMap('film_awards.json', films_awards, films_titles)
marauder_map.map_generator(main)
