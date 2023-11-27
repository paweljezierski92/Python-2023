for i in range(12):
    print(i)

for i in range(3, 12):
    print(i)

for i in range(3, 12, 2):
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")


#Zadanie z for:
##wczytaj przy użyciu `input()` liczbę; wypisz sumę jej cyfr


liczba = input("Podaj liczbe")

suma_liczb = 0
for g in liczba:

    suma_liczb += int(g)

print(f"suma liczby{liczba} wynosi:{suma_liczb}")