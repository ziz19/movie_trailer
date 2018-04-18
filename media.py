class Movie():
    '''This class stores movie related information

    Args:
        movie_title (str): Title of the movie
        poster_image (str): URL of the poster image
        trailer (str): URL of the trailer

    Attributes:
        title (str): Title of the movie
        poster_image_url (str): URL of the poster image
        trailer_youtube_url (str): URL of the trailer

    '''
    
    def __init__(self, movie_title, poster_image,
                 trailer):       
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

