from  spotipy import*
import pandas as pd
import time
#TODO-Check notion for the client id and secret id
auth_manager = SpotifyClientCredentials()

sp=Spotify(auth_manager=auth_manager)

def getTrackFeatures(id):
    
    track_info =sp.track(id)
    track_features = sp.audio_features(id)

    name=track_info['name']
    album=track_info['album']['name']
    artist=track_info['album']['artists'][0]['name']
    release_date=track_info['album']['release_date']
    length=track_info['duration_ms']
    popularity=track_info['popularity']

    acousticness=track_features[0]['acousticness']
    danceability=track_features[0]['danceability']
    energy=track_features[0]['energy']
    instrumentalness=track_features[0]['instrumentalness']
    liveness=track_features[0]['liveness']
    loudness=track_features[0]['loudness']
    speechiness=track_features[0]['speechiness']
    tempo=track_features[0]['tempo']
    time_signature=track_features[0]['time_signature']

    track_data=[name,album,artist,release_date,length,popularity,acousticness,danceability,energy,instrumentalness,liveness,loudness,speechiness,tempo,time_signature]
    return track_data


def getTrackIDs(user,playlist_id):
    tracks_ids=[]
    playlist=sp.user_playlist(user,playlist_id)
    for item in playlist["tracks"]["items"]:
        track=item["track"]
        tracks_ids.append(track["id"])
    return tracks_ids

track_ids=getTrackIDs("spotify","37i9dQZF1E37Dii8ZFiIp2")

track_list=[]
for i in range(len(track_ids)):
    time.sleep(.3)
    track_data=getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    
playlist_selected=pd.DataFrame(track_list,columns=["name","album","artist","release_date","length","popularity","acousticness","danceability","energy","instrumentalness","liveness","loudness","speechiness","tempo","time_signature"])

print(playlist_selected.head(25))


