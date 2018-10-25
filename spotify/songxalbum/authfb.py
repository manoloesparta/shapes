from os import environ
from fbchat import Client

def authfb():

	email = environ['FB_EMAIL']
	password = environ['FB_PASSWORD']
	client = Client(email, password)

	return client