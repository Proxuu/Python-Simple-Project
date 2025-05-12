
def main():

    zdanie = input("Wpisz zdanie: ").lower()

    licznik = {}

    for litera in zdanie:
        if litera.isalpha():
            if litera in licznik:
                
                licznik[litera] += 1
            else:
                licznik[litera] = 1

    for litera in sorted(licznik):
        print(f'{litera}: {licznik[litera]}')


main()