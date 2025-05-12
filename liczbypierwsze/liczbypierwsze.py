def czy_piewrsza(n):
    if n <= 0:
        return False
    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            return False
    return True

pierwsza = int(input("Wprowadź pierwszą liczbę z przedziału: \n"))
ostatnia = int(input("Wprowadź ostatnią liczbę z przedziału: \n"))

licznik = 0
liczby = []

for num in range(pierwsza, ostatnia + 1):
    if czy_piewrsza(num):
        liczby.append(str(num))
        licznik += 1

print(f"LIczby pierwsze w zakresie {pierwsza} - {ostatnia}: \n{', '.join(liczby)}")
print(f"Znaleziono {licznik} liczb pierwszych")