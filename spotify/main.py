import spotipy
import json
import os
import random
from spotipy import util

# Auth

playlist_retrieved = '1ofx1iXeCqb5gPuEWSanfc'
playlist_goal = '0iYFyrLsby2E0QBBPs2xWi'

username = 'manoloesparta'
scope = 'playlist-modify-private'

try:
	token = util.prompt_for_user_token(username, scope)
except:
	os.remove(f'.cache-{username}')
	token = util.prompt_for_user_token(username, scope)

Spotify = spotipy.Spotify(auth=token)

# Remove current songs

results = Spotify.user_playlist_tracks(username, playlist_goal)
tracks = results['items']

removed = []

for i in tracks:
	removed.append(i['track']['id'])

Spotify.user_playlist_remove_all_occurrences_of_tracks(username, playlist_goal, removed)

# Get Songs 

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

all_tracks_uri = []

for album in range(len(albums_uri)):

	set_list = Spotify.album_tracks(albums_uri[album])

	for track in set_list['items']:
		all_tracks_uri.append(track['id'])

	print('ALBUM:',albums_name[album],'LOADED')
	
	
# Choose random songs

all_tracks_uri = random.sample(all_tracks_uri, len(all_tracks_uri))

chosen = []
random_num = []

for i in range(100):

	choice = random.randint(0, len(all_tracks_uri))

	while choice in random_num:
		choice = random.randint(0, len(all_tracks_uri))

	random_num.append(choice)
	chosen.append(all_tracks_uri[choice])

# Add songs to playlist

Spotify.user_playlist_add_tracks(username, playlist_goal, chosen)
print('Done')
