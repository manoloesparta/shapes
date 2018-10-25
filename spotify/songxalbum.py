import spotipy
import json
import os
import random
import auth
from spotipy import util
from fbchat import Client
from fbchat.models import *
from os import environ

playlist_retrieved = '1ofx1iXeCqb5gPuEWSanfc'
playlist_goal = '0iYFyrLsby2E0QBBPs2xWi'

# Auth

token = auth.token
username = auth.username
Spotify = spotipy.Spotify(auth=token)

def update():
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
	tracks_names = []
	for i in range(len(albums_selected)):
		set_list = Spotify.album_tracks(albums_selected[i])
		print("ALBUM", albums_selected_names[i], "LOADED")
		mini = random.randint(0, len(set_list['items']) - 1)
		leng = len(set_list)
		tracks_ids.append(set_list['items'][mini]['id'])
		tracks_names.append(set_list['items'][mini]['name'])

	return {'tracks_ids': tracks_ids, 'tracks_names': tracks_names}

def authfb():
	# Auth fb
	email = environ['FB_EMAIL']
	password = environ['FB_PASSWORD']
	client = Client(email, password)

	return client

def send(client, tracks_names):
	# Send message
	juampy = environ['JUAMPY_FBID']
	client.send(Message(text=", ".join(tracks_names)), thread_id=juampy, thread_type=ThreadType.USER)

if __name__ == '__main__':

	tracks = update()

	try:
		client = authfb()
		send(client, tracks['tracks_names'])
	except:
		print("No se le pudo mandar mensaje a Juampy")

	Spotify.user_playlist_add_tracks(username, playlist_goal, tracks['tracks_ids'])
	print('Done')