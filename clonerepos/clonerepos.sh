REPOS=(stuff logicnet albums.py playlist.py artist.py chat monstertask)
URL=https://github.com/manoloesparta/

for single in "${REPOS[@]}"
do
	git clone $URL$single 
done

echo Done!
