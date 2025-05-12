def palindrom(tekst):

    samelitery = ''.join(litera for litera in tekst.lower() if litera.isalpha())
    return samelitery == samelitery[::-1]

def main():

    zdanie = input("wprowadź tekst: ")

    if palindrom(zdanie):
        print("To zdanie to palindrom")
    else:
        print("To nie palindrom")

main()