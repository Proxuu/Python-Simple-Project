pierwsze = input("Podaj pierwsze słowo: ").replace(" ", "").lower()
drugie = input("Podaj drugie słowo: ").replace(" ", "").lower()

if sorted(pierwsze) == sorted(drugie):
    print("To są anagramy!")
else:
    print("To NIE są anagramy.")


