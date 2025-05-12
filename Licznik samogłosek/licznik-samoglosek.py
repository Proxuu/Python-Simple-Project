
def policz_samogloski(tekst):
    samogloski = set('aeiouyąę')
    return sum(1 for litera in tekst.lower() if litera in samogloski)


def main():
    zdanie = input('Podaja Zdanie: ').strip()

    if not zdanie:
        print('Nie podałeś żadnego zdania.')
        return
    
    liczba = policz_samogloski(zdanie)
    print(f'Liczba samogłosek w Twoim zdaniu: {liczba}')

main()