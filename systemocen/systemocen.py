liczba_przedmiotow = int(input('Ile przedmiotów: '))

oceny = {}

for i in range(liczba_przedmiotow):
    przedmiot = input("Podaj nazwę przedmiotu: ")
    lista_ocen = input(f"Podaj oceny z {przedmiot} (oddzielone spacją): ")

    intlista_ocen = list(map(int, lista_ocen.split()))

    oceny[przedmiot] = intlista_ocen
    



print('\nWYNIKI:')

ogolnasuma = 0
ogolnadlugosc = 0

for przedmiot, lista in oceny.items():

    srednia = sum(lista) / len(lista)

    ogolnasuma += sum(lista)
    ogolnadlugosc += len(lista)

    print(f'{przedmiot:<12} - {lista} - średnia: {round(srednia, 2)} ')

print(f"\n ŚREDNIA OGÓLNA: {round(ogolnasuma/ogolnadlugosc, 2)}")

