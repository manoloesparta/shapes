import spotipy
import json
import os
import random
from spotipy import util
import auth

playlist_retrieved = '1ofx1iXeCqb5gPuEWSanfc'
playlist_goal = '0iYFyrLsby2E0QBBPs2xWi'

# Auth

token = auth.token
username = auth.username
Spotify = spotipy.Spotify(auth=token)

# Remove current songs

results = Spotify.user_playlist_tracks(username, playlist_goal)
tracks = results['items']

removed = []

for i in tracks:
	removed.append(i['track']['id'])

Spotify.user_playlist_remove_all_occurrences_of_tracks(username, playlist_goal, removed)

# Get Albums 

results = Spotify.user_playlist_tracks(username, playlist_retrieved)
tracks = results['items']

while results['next']:

	results = Spotify.next(results)
	tracks.extend(results['items'])

albums_uri = []
albums_name = []

for i in tracks:

	albums_uri.append(i['track']['album']['id'])
	albums_name.append(i['track']['album']['name'])

# Random albums

albums_selected = []
albums_selected_names = []
random_num = []

for i in range(100):
	choice = random.randint(0, len(albums_uri) - 1)

	while choice in random_num:
		choice = random.randint(0, len(albums_uri) - 1)

	random_num.append(choice)
	albums_selected.append(albums_uri[choice])
	albums_selected_names.append(albums_name[choice])

# Song x album

tracks_ids = []

for i in range(len(albums_selected)):

	set_list = Spotify.album_tracks(albums_selected[i])
	print("ALBUM", albums_selected_names[i], "LOADED")
	mini = random.randint(0, len(set_list['items']) - 1)
	leng = len(set_list)
	tracks_ids.append(set_list['items'][mini]['id'])

# Add to playlist

Spotify.user_playlist_add_tracks(username, playlist_goal, tracks_ids)
print('Done')