waga = float(input("Podaj wagę (w kilogramach): "))
wzrost = float(input("Podaj wzrost (w metrach): "))

def calc():
    bmi = waga / wzrost**2
    if bmi < 18.5:
        print(f'BMI: {bmi} - Niedowaga')
    elif bmi >= 18.5 and bmi < 25:
        print(f'BMI: {bmi} - Waga prawidłowa')
    elif bmi >= 25 and bmi < 30:
        print(f'BMI: {bmi} - Nadwaga')
    else:
        print(f'BMI: {bmi} - Otyłość')

calc()



        
