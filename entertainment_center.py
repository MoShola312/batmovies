import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

the_dark_knight =  media.Movie("The Dark Knight", "The greatest superhero of all time faces a new threat",
                               "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                               "https://www.youtube.com/watch?v=EXeTwQWrcwY")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

batman_begins =  media.Movie("Batman Begins", "The orgins of Batman.",
                               "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                               "https://www.youtube.com/watch?v=neY2xVmOfUM")

mask_of_the_phantasm =  media.Movie("Batman: Mask of the Phantasm", "Batman faces old and new threats.",
                               "https://upload.wikimedia.org/wikipedia/en/e/ea/Batman_mask_of_the_phantasm_poster.jpg",
                               "https://www.youtube.com/watch?v=WRw8LeBO2Ls")

red_hood =  media.Movie("Batman: Under the Red Hood", "Dark Knight finds himself being stalked by a mysterious criminal who seems to know all of his secrets.",
                               "https://upload.wikimedia.org/wikipedia/en/4/4c/Batman_under_the_red_hood_poster.jpg",
                               "https://www.youtube.com/watch?v=A2c9MsP3OVs")

the_dark_knight_returns =  media.Movie("The Dark Knight Returns", "The greatest superhero comes out of retirement.",
                               "https://upload.wikimedia.org/wikipedia/en/e/e9/Batman_The_Dark_Knight_Returns_%28film%29.jpg",
                               "https://www.youtube.com/watch?v=_BPjhV28bQM")

flashpoint_paradox =  media.Movie("Justice League: The Flashpoint Paradox", "The Flash traverses time to right a violent, decades-past crime but the ripples of his good intentions prove disastrous",
                               "https://upload.wikimedia.org/wikipedia/en/d/d5/Justice_League_-_The_Flashpoint_Paradox.jpg",
                               "https://www.youtube.com/watch?v=NKx0uU-eCtU")
                             
#the_dark_knight.show_trailer()

movies = [batman_begins, the_dark_knight, mask_of_the_phantasm, red_hood,  the_dark_knight_returns, flashpoint_paradox]

fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
#print(media.Movie.__module__)
