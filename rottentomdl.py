import urllib.request

print("-- Thanks for downloading rottentomdl.py V:0.0.2")
print("-- When searching use _ instead of spaces and lowercase letters")
print("-- i.e. gone_baby_gone ")

pageValidation = False
while pageValidation == False:
    try :
        movieName = str(input("What movie review do you want to download ? "))
        url = "https://www.rottentomatoes.com/m/" + movieName
        response = urllib.request.urlopen(url)
        webContent = str(response.read().decode("utf-8"))
        pageValidation = True
    except Exception:
        pageValidation = False

dlname = movieName + "_rottentomatoes.html"
f = open(dlname, 'w')
f.write(webContent)
f.close

print(dlname + " has been downloaded ! ")

    