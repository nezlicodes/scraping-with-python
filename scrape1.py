import urllib.request, urllib.parse, urllib.error


fhand = urllib.request.urlopen("https://www.kherdja.com/")

counts= dict()
for line in fhand:
#    Line is in UTF-8 so we need to decode it first
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)