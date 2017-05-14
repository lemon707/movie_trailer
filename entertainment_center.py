import media, fresh_tomatoes

pride_and_prejudice = media.Movie("Pride and Prejudice", "Jane Austen's perennially popular story of the game of love.", "http://img.moviepostershop.com/pride-and-prejudice-movie-poster-2005-1010451320.jpg", "https://www.youtube.com/watch?v=7Afx8MGg00g")
a_beautiful_mind = media.Movie("A Beautiful Mind", "American biographical drama film based on the life of John Nash, a Nobel Laureate in Economics.", "http://img.moviepostershop.com/a-beautiful-mind-movie-poster-2001-1010190915.jpg", "https://www.youtube.com/watch?v=YWwAOutgWBQ")
inception = media.Movie("Inception", "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.", "http://img.moviepostershop.com/inception-movie-poster-2010-1020547300.jpg", "https://www.youtube.com/watch?v=d3A3-zSOBT4")
interstellar = media.Movie("Interstellar", "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", "http://img.moviepostershop.com/interstellar-movie-poster-2014-1010771206.jpg", "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# pride_and_prejudice.show_trailer()
# a_beautiful_mind.show_trailer()
# inception.show_trailer()
# interstellar.show_trailer()

movies_list = [pride_and_prejudice,a_beautiful_mind,inception,interstellar]
fresh_tomatoes.open_movies_page(movies_list)