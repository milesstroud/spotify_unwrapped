from music_functions import *


results = sp.current_user_recently_played(limit=50, after=None, before=None)
#
songs_lyrics = ['song_name','artist']
songs_lyrics = dict.fromkeys(songs_lyrics,None)
#
#
recent_tunes = pd.DataFrame(columns=['artist','song_name'])
tune_metrics = pd.DataFrame(columns=audio_features)
for item in results['items']:
    print(item)
    songs_lyrics['artist'] = item['track']['album']['artists'][0]['name']
    songs_lyrics['song_name'] = item['track']['name']
    id = item['track']['id']
    songs_lyrics['id'] = id
    metrics = audio_Features(id)
    metrics['timestamp'] = timestamp_cleaner(item['played_at'])
    songs_lyrics['lyrics'] = None
    try:
        title = item['track']['name']
        title = re.sub("\(.*\)", "", title)
        title = re.sub("- Live","",title)
        lyrics = lyrics_search(title,item['track']['album']['artists'][0]['name'])
        songs_lyrics['lyrics'] = lyrics_cleaner(lyrics)
    except AttributeError as error:
        print(error)
    tune_metrics = tune_metrics.append(metrics,ignore_index=True)
    recent_tunes = recent_tunes.append(songs_lyrics, ignore_index=True)



recent_tunes_complete = pd.merge(recent_tunes,tune_metrics, on='id')
#Will need to sort by datetime DESC
recent_tunes_complete = recent_tunes_complete.sort_values("timestamp",ascending=False)

#Writing the CSV that will store the data locally (one time)
# recent_tunes_complete.to_csv("Recent_Tunes.csv")

#Adding today's data to the existing CSV

#We want to only add data that is not already in the .CSV. To do this, we'll use the timestamp
#Will want to loop through each new row, pull its timestamp, and confirm it's newer than the last timestamp in existing
#data. By the end, have a dict/dataframe of entirely new additions and append that one to existing records.


existing_data = pd.read_csv("Recent_Tunes.csv")
existing_data = existing_data.sort_values("timestamp",ascending=False)
latest_pull = existing_data['timestamp'][0]
recent_tunes_complete['timestamp'] = pd.to_datetime(recent_tunes_complete['timestamp'])
recent_tunes_complete = recent_tunes_complete.loc[recent_tunes_complete['timestamp'] > latest_pull]

# recent_tunes_complete.to_csv("Recent_Tunes.csv",header=False,mode='a')
