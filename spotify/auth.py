import os
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