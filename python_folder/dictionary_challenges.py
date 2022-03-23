
#! Dictionary Challenges

countries = {"England":"London", #* Key:Value pair is an Item
          "France": "Paris",
          "Germany": "Munich",
          "Spain": "Madrid",
          "Italy": "Rome"  
         }

print(countries.items())

countries.setdefault("Japan", "Tokyo") #* Creates a new key and value.
countries.setdefault("Greece", "Athens") #* Creates a new key and value.

print(countries.items()) #* using .items to print as it displays all of the information. 

# del countries["England"]
#print(countries.items())

languages = {"England":"English", #* Key:Value pair is an Item
          "France": "French",
          "Germany": "German",
          "Spain": "Spanish",
          "Italy": "Italian",
          "Japan": "Japanese",
          "Greece": "Greek"  
         }

countries.update(languages)
print(countries.items())

fav_songs = []

song1 = {"artist": "Childish Gambino",
         "song_name": "Sober",
         "genre": "Neo soul",
         "release_year": "2014"
    }

fav_songs.append(song1)

song2 = {"artist": "Not3s",
         "song_name": "Wanting",
         "genre": "R&B/Soul",
         "release_year": "2019"
    }

fav_songs.append(song2)

song3 = {"artist": "DJ Regard",
         "song_name": "Ride It",
         "genre": "Dance/Electronic",
         "release_year": "2021"
    }       

fav_songs.append(song3)

print (fav_songs)

correction = {"artist": "Tame Impala",
         "song_name": "The Less I Know the Better",
         "genre": "Alternative/Indie",
         "release_year": "2015"
    }
song3.update(correction)

print (fav_songs)