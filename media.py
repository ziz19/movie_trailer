class Movie():
    '''This class stores movie related information'''
    
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        '''movie_title = name of the movie
        poster_image = URL of the poster
        trailer_youtube = URL of the trailer'''
        
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

