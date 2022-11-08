import urllib.request

checker = urllib.request.urlopen("www.google.com").getcode()

print(checker)