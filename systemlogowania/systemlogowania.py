uzytkownicy = {}

def rejestracja():

    login = input("Podaj nowy login: ")

    if login in uzytkownicy:
        print("Taki login już istnieje. Spróbuj ponownie")
        return
    
    haslo = input("Podaj nowe haslo: ")

    uzytkownicy[login] = {"haslo": haslo, "logowania": 0}
    print("Zarejestrowano pomyśllnie")

def logowanie():

    login = input("Podaj login: ")

    if login in uzytkownicy:
        haslo = input("Podaj hasło: ")

        if haslo == uzytkownicy[login]['haslo']:

            uzytkownicy[login]["logowania"] += 1
            panel_uzytkownika(login)
        else:
            print("haslo jest niepoprawne")
    else:
        print("Taki login nie istnieje! Spróbuj ponownie.")
        return
    


def panel_uzytkownika(login):


    while True:

        print(f"\n--- PANEL UŻYTKOWNIKA: {login} ---")
        print('[1] Pokaż liczbę logowań')
        print('[2] Zmień hasło')
        print('[3] Wyloguj się')

        wybor = input("> ")

        if wybor == "1":
            print(f'\nLiczba logowań: {uzytkownicy[login]["logowania"]}')
        elif wybor == "2":
            nowe_haslo = input("Wprowadź nowe hasło: ")
            uzytkownicy[login]["haslo"] = nowe_haslo
            print("Hasło zmienione pomyślnie")
        elif wybor == "3":
            print("Dowidzenia!")
            break
        else:
            print("Błąd")

def main():
    
    while True:
        print("\nWitaj w systemie!")
        print("[1] Zaloguj się")
        print("[2] Zarejestruj się")
        print("[3] Zakończ")

        wybor = input("> ")

        if wybor == "1":
            logowanie()
        elif wybor == "2":
            rejestracja()
        elif wybor == "3":
            break
        else:
            print("Błąd")

main()


    