import requests
res = requests.get("https://www.gutenberg.org/cache/epub/43493/pg43493.txt")
res.raise_for_status()
playFile = open("Abolicionismo en Puerto Rico.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()