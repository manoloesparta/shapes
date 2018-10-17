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

for i in tracks:
	albums_uri.append(i['track']['album']['id'])

all_tracks_uri = []

for album in albums_uri:
	set_list = Spotify.album_tracks(album)
	for track in set_list['items']:
		all_tracks_uri.append(track['id'])

# Choose random songs

chosen = []

for i in range(100):
	choice = random.randint(0, len(all_tracks_uri))
	chosen.append(all_tracks_uri[choice])

# Add songs to playlist

Spotify.user_playlist_add_tracks(username, playlist_goal, chosen)
