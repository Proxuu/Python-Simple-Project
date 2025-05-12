
wiek = float(input('\nPodaj wiek psa (W ludzkich latach):'))

if wiek <= 2:
    psiwiek = wiek * 10.5
else:
    psiwiek = 21 + (wiek - 2) * 4

print(f'\n\nTwój pies według psich lat ma: {psiwiek}') 