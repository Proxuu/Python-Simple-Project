def suma_dzielnikow(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
        return suma == n

podanaliczba = int(input("Wprowadź liczbę: "))

if suma_dzielnikow(podanaliczba):
    print(f"Podana liczba ({podanaliczba}) jest liczbą doskonałą")
else:
    print(f"Podana liczba ({podanaliczba}) nie jest liczbą doskonałą")
