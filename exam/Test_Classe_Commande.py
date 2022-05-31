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
the_fresh = Cocktails("The Fresh", 4, ingredient_the_fresh)
the_fusion = Cocktails("The Fusion", 5, ingredient_the_fresh)
the_detox = Cocktails("The Detox", 3.5, ingredient_the_fresh)


# Définition de la classe Borne

class Borne():
    _listCocktail = ["","","",""]
    _selectedCocktail = Cocktails
    _numberofCocktails = 0
    _sizeof = Size

    def __init__(self, listCocktail):
        self._listCocktail =  listCocktail
    
    def show_list_cocktails(self):
        print("Voici la carte de nos differents cocktails : \n\n")
        for Cocktail in self._listCocktail:
            print("- %s : %s" % (Cocktail.name, Cocktail.price))
        return self._listCocktail



cocktail = Borne(["1 :",the_boost.name,"2 :", the_detox.name,"3 :", the_fresh.name,"4 :", the_fusion.name])


# Définition de la class Commande

class commandes():
    _OrderNumber = 0
    _TotalPrice = 0
    _listecommande = ""

    def __init__(self, OrderNumber, TotalPrice):
        self._OrderNumber =  OrderNumber
        self._TotalPrice =  TotalPrice
    @property
    def totalPrice(self):
        return self._TotalPrice

    @totalPrice.setter
    def totalPrice(self, totalPrice):
        self._TotalPrice = totalPrice

    @property
    def orderNumber(self):
        return self._OrderNumber

    @orderNumber.setter
    def orderNumber(self, _OrderNumber):
        self._OrderNumber = _OrderNumber

    @property
    def listecom(self):
        return self._listecommande

    @listecom.setter
    def listecom(self, _listecommande):
        self._listecommande = _listecommande

commande = commandes(0,0)

# Test de get et set les attribut de commande

print ("Valeur de base : ",commande.orderNumber)

commande.orderNumber = 50

print ("\n\nNouvelle Valeur : ",commande.orderNumber)