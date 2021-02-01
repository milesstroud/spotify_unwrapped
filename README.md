# Spotify UNwrapped


This is a project I will be embarking on throughout 2021  (...at least, from February 2021 onward) that I've dubbed Spotify UNwrapped. The purpose is to, at the end of the year, give not just a cursory (or "wrapped") look at my year-in-audio, but a detailed, data-driven look instead :) Of course, all credit is due to Spotify's annual Spotify Wrapped and the Spotify API for the idea.


## Summary


This is purely for fun! I'm curious if I'll be able to look back at my year and see noticeable trends in my audio listening habits. To do this, I will be accessing the Spotify API for my user data as well as audio features of each song. I will also be accessing the Lyrics Genius API to gather lyrics for each song I listen to so I can carry out sentiment analysis at the end of the year! The bulk of the work for this project will occur once the year ends, barring any data collection snags during the year. 


I'll see you all in 2022!

## Code

[Functions and Imports](https://github.com/milesstroud/spotify_unwrapped/blob/main/imports/music_functions.py)
  - Contains the necessary functions and imports, separated for cleanliness
 
 [Spotify Unwrapped (C)](https://github.com/milesstroud/spotify_unwrapped/blob/main/collection_and_analysis/spotify_unwrapped_c.py)
  - *Data Collection Script* This script makes calls to the Lyrics Genius and Spotify APIs using the lyricsgenius and Spotipy packages. Data collected is stored locally in a .csv file (though, I suggest you store this in multiple places if possible). This is the lifeblood of my future analysis :-) I will run this script 2X a day, 6 hours apart to hopefully catch as much of my audio-consumption as possible. The data will still be "sampled" in a sense, however.



## Authors

* **Miles Stroud** - (https://github.com/milesstroud)

## References

* **lyricsgenius** - (https://pypi.org/project/lyricsgenius/)
* **Spotipy** - (https://spotipy.readthedocs.io/en/2.16.1/)


