range(10)    #generator

list(range(10))    #lista

(x * x for x in range(10))

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0] # bierze liczby od 10 podzielne  zbez reszty

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)] #list_comprehension

{x for x in range(10)}  # tutaj bedzie zbior juz

{x // 2 for x in range(10)}  #set comprehension

{x: x * x for x in range(10) if x % 2 == 0} #dictionary comprehension



#.#Stworzyć *list comprehension* na podstawie jednej listy z liczbami całkowitymi, ale z elementami o 6 większymi

[x+6 for x in range (10)]

#. Stworzyć *list comprehension* tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis - np. `[(1, "1"), (2, "2")]`

a = [(x, str(x)) for x in range(10)]
print(a)


# stworzyć list comprehension nazw pojazdów cięższych niż 5000
#  - Nazwy podać dużymi literami (*uppercase*)


dane = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
        "Motorcycle": 110}
[x.upper() for x in dane.keys() if dane[x] > 5000]


