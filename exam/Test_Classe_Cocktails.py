from argparse import ArgumentTypeError
from enum import Enum
from hashlib import new

# Taille des boissons

class TypeSize(Enum):
    Small = 0
    Medium = 1
    Large = 2

# Class comprennant l'énumération des tailles

class Size():

    _type = TypeSize.Small

    def __init__(self, size):
        self._size = TypeSize

    @property
    def type(self):
        return self._type


# Déclaration des listes d'ingrédients

class Ingredients():
    _ingredient = ["","","",""]

    def __init__(self, ingredient, price):
        self._ingredient = ingredient
        self._price = price

# Définition d'un Cocktails

class Cocktails():
    _name = ""
    _price = 1.5
    _ingredients = Ingredients

    def __init__(self, name, price, ingredients):
        self._name = name
        self._price = price
        self._ingredients = ingredients

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
    
# Définition des listes d'ingrédients différentes

ingredient_the_boost = ["1/2 mango", "2 oranges", "1u. of guajana"]
ingredient_the_fresh = ["3 apples", "1u. of ginger", "1 lemon"]
ingredient_the_fusion = ["1 guava", "1/4 pineapple", "1/2 banana"]
ingredient_the_detox = ["3 carrots", "1 celery stick", "1 beetroot"]

# Définition des cocktails

the_boost =Cocktails("The Boost", 5, ingredient_the_boost)


print (the_boost.name)
print (the_boost.price)
print (the_boost._ingredients)
