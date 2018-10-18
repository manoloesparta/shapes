import spotipy
import spotipy.util as util
import auth
import types

# Auth

token = auth.token
Spotify = spotipy.Spotify(auth=token)

# Get history

result = Spotify.current_user_recently_played(limit=100)
print(result)