from random import randint

def selectAlbums(albums_uri, albums_name):

	albums_selected = []
	albums_selected_names = []
	random_num = []

	for i in range(100):
		choice = randint(0, len(albums_uri) - 1)

		while choice in random_num:
			choice = randint(0, len(albums_uri) - 1)

		random_num.append(choice)
		albums_selected.append(albums_uri[choice])
		albums_selected_names.append(albums_name[choice])

	return {'albums_selected':albums_selected, 'albums_selected_name':albums_selected_names}