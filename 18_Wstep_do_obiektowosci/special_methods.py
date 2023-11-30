# object.__lt__(self, other)
#
# object.__le__(self, other)
#
# object.__eq__(self, other)
#
# object.__ne__(self, other)
#
# object.__gt__(self, other)
#
# object.__ge__(self, other)
#

# object.__len__
#
# object.__iter__
#
# object.__getslice__(self,i,j)
#
# object.__add__
#
# object.__sub__
#
# object.__mul__

class IntValue:
    def __init__(self, value):
        self.value = value

    # repr() : evaluatable string representation of an object (can "eval()" it, meaning it is a string representation that evaluates to a Python object)
    def __repr__(self):
        return f"IntValue({self.value})"

    def __gt__(self, other):
        return self.value > other.value


a = IntValue(3)
b = IntValue(5)

b > a # b.__gt__(a)

b


class IntValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "IntValue(%d)" % (self.value)

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        return IntValue(self.value + other.value)


a = IntValue(3)
b = IntValue(5)

a + b

a = IntValue(3)
b = 5

a + b # error


class IntValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "IntValue(%d)" % (self.value)

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        if type(other) == type(self):
            value = other.value
        else:
            value = other
        return IntValue(self.value + value)


a = IntValue(3)
b = 5

a + b # ok

b + a # error


class IntValue:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "IntValue(%d)" % (self.value)

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        if type(other) == type(self):
            value = other.value
        else:
            value = other
        return IntValue(self.value + value)

    def __radd__(self, value):
        return IntValue(self.value + value)
#############################################################


a = 3
b = IntValue(5)

a + b

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __len__(self):
        return int(self.length())

    @property
    def r(self):
        return self.length()

    # repr() : evaluatable string representation of an object (can "eval()" it, meaning it is a string representation that evaluates to a Python object)
    # https://docs.python.org/3.11/library/reprlib.html#
    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

p = Point(3,4)
len(p)
p

#############################################################

values = ('9', '10', 'J', 'Q', 'K', 'A')
suits = ('clubs', 'diamonds', 'hearts', 'spades')


class Card(object):
    def __init__(self, value, suit):
        self.value, self.suit = value, suit

    def __repr__(self):
        return "Card('%s','%s')" % (self.value, self.suit)

    def __eq__(self, card):
        return self.value == card.value and self.suit == card.suit




###########
###- Stworzyć klasę `Card` która ma dwa pola - `suit` (wartości np. `club`, `diamond`, `heart`, `spade`), `value` (wartości np. `9`, `10`, `J`, `Q`, `K`, `A`) przeciążyć metodę od obsługi `<` i `>` które oznacza "bicie karty"
 ### - Karta bije kartę jeśli ma ten sam kolor i mocniejszą wartość
 ### - Pik (`spade`) jest atutem - bije inne kolory. Pozostałe kolory nie biją się nawzajem
#####


# Stworzyć klasę Card która ma dwa pola - suit (wartości np. club, diamond, heart, spade), value (wartości np. 9, 10, J, Q, K, A) przeciążyć metodę od obsługi < i > które oznacza "bicie karty"
# Karta bije kartę jeśli ma ten sam kolor i mocniejszą wartość
# Pik (spade) jest atutem - bije inne kolory. Pozostałe kolory nie biją się nawzajem


class Card:
    VALUES = ('9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def czy_bije(self, karta2):
        return self.SUITS.index(self.suit) > self.SUITS.index(karta2.suit) or (
                self.SUITS.index(self.suit) == self.SUITS.index(karta2.suit) and
                self.VALUES.index(self.value) > self.VALUES.index(karta2.value)
        )

    def __repr__(self):
        return f'Card("{self.suit}", "{self.value}")'

    def __str__(self):
        return f'Card("{self.suit}", "{self.value}")'

    def __gt__(self, other):
        return self.czy_bije(other)

    def __lt__(self, other):
        return other.czy_bije(self)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __ge__(self, other):
        return self.czy_bije(other) or self == other



trefl9 = Card("clubs", "9")
spades_ace = Card("spades", "A")
heart_king = Card("hearts", "K")

spades_ace > trefl9
spades_ace.__gt__(trefl9)


spades_ace < trefl9


spades_ace.czy_bije(trefl9)
trefl9.czy_bije(spades_ace)

reka = [ spades_ace, heart_king, trefl9]
reka
reka.sort()
reka

str(spades_ace)



# - Stworzyć klasę `FoodItem` z polami `id`, `price` `item` - specjalnymi metodami `__init__` i `__repr__`, stworzyć listę `FoodItem` na podstawie pliku CSV
#

import csv
class FoodItem:

    def __init__(self, id, price,item):
        self.id = int(id)
        self.price = price
        self. item = float(item)

    def __repr__(self):
        return FoodItem("{self.id}", "{self.item}", "{self.price}")


food_list = []

with open(`'`foods.csv) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        food_list.append(FoodItem(id=row['Food ID'], item=row['Food Item'], price=row['Price']))

print(food_list)



