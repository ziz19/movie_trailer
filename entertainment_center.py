import media
import fresh_tomatoes


# create movie instances with name, poster URL and trailer URL
school_of_rock = media.Movie('School of Rock',
                             'http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',  # NOQA
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')
iron_man = media.Movie('Iron Man',
                       'https://images-na.ssl-images-amazon.com/images/I/91qvAndeVYL._RI_.jpg',  # NOQA
                       'https://www.youtube.com/watch?v=8hYlB38asDY')
avengers_3 = media.Movie('Avengers 3',
                         'https://cdn.movieweb.com/img.news.tops/NEzqoI3wvsghCD_2_b/Avengers-3-Trailer-Countdown-Release-Date-Infinity-War.jpg',  # NOQA
                         'https://www.youtube.com/watch?v=m2uqb2bt_bs')
movies = [school_of_rock, iron_man, avengers_3]
fresh_tomatoes.open_movies_page(movies)  # create the trailer website
