from songxalbum.auth import auth
from songxalbum.remove import removeSongs
from songxalbum.albums import getAlbums
from songxalbum.selectAlbums import selectAlbums
from songxalbum.selectSongs import selectSongs
from songxalbum.authfb import authfb
from songxalbum.sendMsg import send

playlist_retrieved = '1ofx1iXeCqb5gPuEWSanfc'
playlist_goal = '0iYFyrLsby2E0QBBPs2xWi'

username = 'manoloesparta'
scope = 'playlist-modify-private'

def main():

	Spotify = auth(username, scope)

	removeSongs(Spotify, username, playlist_goal)

	albums = getAlbums(Spotify, username, playlist_retrieved)
	albums = selectAlbums(albums['albums_uri'], albums['albums_name'],albums['albums_artist'])

	tracks = selectSongs(Spotify, albums['albums_selected'], albums['albums_selected_name'], albums['albums_selected_artist'])

	Spotify.user_playlist_add_tracks(username, playlist_goal, tracks['tracks_id'])

	try:
		client = authfb()
		send(client, tracks['tracks_name'])
	except:
		print("Not posible to send message")

if __name__ == '__main__':

	main()