n = 5

while n > 0:
    print(n)
    n -= 1

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')

### Zadanie z while

 ### Wypisać wszystkie liczby od `1` do `100` które spełniają warunek z poprzedniego zadania
### - wczytaj przy użyciu `input()` liczbę; wypisz sumę jej cyfr
g = 1
while g < 101:
    print(g)
    g += 1

    print(f'{g} Koniec')



if (g % 2 == 0) and (g %10+1 //10 )%7==0:
    print(g)
else:
    print(f'Zła liczba')



#inny program
i=0
while i<100:
    i+=1
    if i % 2 == 0 and (i % 10 + i // 10) % 7 == 0:
        print(i)
        continue
else:
    print('Koniec')