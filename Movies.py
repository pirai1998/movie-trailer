import Fresh_tomatoes

import Movie

# To add each of my favorite movies everytime a new instance are created
sachin = Movie.Movie("sachin",
                     "love story",
                     "http://mimg.sulekha.com/telugu/sachin/images/stills/sachin17.jpg",
                     "https://www.youtube.com/watch?v=3gDvH5ajShQ")
ohm_shanthi_oshana = Movie.Movie("ohm santhi oshana",
                                 "romance",
                                 "http://1.bp.blogspot.com/-E99n1a7j63A/UsaJZntiaVI/AAAAAAAADjE/YnMCljcgMbs/s1600/\
                                 Nazirya+Nazim+in+Om+Shanti+Oshana+Malayalam+Movie+Poster,+Photos,+Wallpapers,+Stills,\
                                 +Cute+Images,+Photos+Gallery,+Pics,+Pictures+Just10media.blogspot.com%5D+(4).jpg",
                                 "https://www.google.co.in/url?sa=t&rct=j&q=\
                                 &esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKE\
                                 wig2qawqMLVAhULu7wKHbpOCrcQtwIIMTAB&url=https%3A%2F%2Fwww\
                                 .youtube.com%2Fwatch%3Fv%3D64sTk1TEcnY&usg=AFQjCNGXLcrQVjUb1Ea\
                                 W7NR2MlDhs_aNDA")
# Here all the movie instance are added to a list
flims = [sachin, ohm_shanthi_oshana]
Fresh_tomatoes.open_movies_page(flims)
