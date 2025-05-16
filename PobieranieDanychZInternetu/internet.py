import urllib.request

url = "http://data.pr4e.org/intro-short.txt"
response = urllib.request.urlopen(url)

licznik = 0
words = []
for line in response:
    print(line.decode().strip())
    words += line.decode().split()
    licznik += 1

print(f'\n{licznik}')
print(f'\n{words}')