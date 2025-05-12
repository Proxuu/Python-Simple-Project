dane = input("Podaj liczby oddzielone spacją: ")
liczby = list(map(int, dane.split()))

print(liczby)

najwieksza = max(liczby)
najmniejsza = min(liczby)
suma = sum(liczby)
srednia = suma / len(liczby)

parzyste = 0
nieparzyste = 0

for i in liczby:
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'Największa: {najwieksza}')
print(f'Najmniejsza: {najmniejsza}')
print(f'średnia: {round(srednia, 2)}')
print(f'Parzyste: {parzyste}')
print(f'Nieparzyste: {nieparzyste}')