from fbchat.models import Message

def send(client, tracks_names):

	juampy = environ['JUAMPY_FBID']
	client.send(Message(text=", ".join(tracks_names)), thread_id=juampy, thread_type=ThreadType.USER)