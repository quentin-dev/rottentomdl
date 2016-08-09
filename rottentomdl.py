import urllib.request
import requests

movieName = str(input("What movie review do you want to download ? "))

url = "https://www.rottentomatoes.com/m/" + movieName

response = urllib.request.urlopen(url)
webContent = str(response.read().decode("utf-8"))

dlname = movieName + ".html"
f = open(dlname, 'w')
f.write(webContent)
f.close

print(dlname + " has been downloaded ! ")

    