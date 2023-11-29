import csv

with open('data/foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


# Zadanie 1
#- Stwórz czytnik plików CSV bez użycia modułu CSV
 # - napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
 # - wypisze jego zawartość oddzielając pola tabulacją `\t`

import csv
import os
print(os.getcwd())
tab = '\t'
n=0
with open('data/foods.csv') as csvfile:
    reader = csv.reader(csvfile)
    for string in csvfile:
        print(f'{n:03d} {tab.join(string.strip().split)(",")}')
    n +=1



#1B  zadanie sys.argv
import csv
import os
import sys
print(os.getcwd())
tab = '\t'
n = 0
with open(sys.argv[1]) as csvfile:
    for line in csvfile:
        print(f'{n:03d} {tab.join(line.strip().split(","))}')
        n +=1
















#- Stwórz czytnik plików CSV bez użycia modułu CSV
 # - napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
 # - wypisze jego zawartość jako listę słowników `{klucz:wartosc, klucz:wartosc ... }` z kluczami wziętymi z pierwszej linijki pliku CSV
