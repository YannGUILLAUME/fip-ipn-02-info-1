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

#Incrémentation du prix avec la taille

def prix(Borne):
    total = 0

    if cocktail._sizeof == TypeSize.Small:
            total += cocktail._selectedCocktail.price
    elif cocktail._sizeof == TypeSize.Medium:
        total += cocktail._selectedCocktail.price + 0.5
    elif cocktail._sizeof == TypeSize.Large:
            total += cocktail._selectedCocktail.price + 1
    else: 
        print("inconnu")
    
    return total


encore = "bonjour"
nouvelle = 0
while nouvelle != 1:
    while encore != "non":

        # Ecran d'acceuil

        print("Voici la liste des cocktails : \n")
        print("1 - ",the_boost.name," :",the_boost._ingredients," prix :",the_boost.price,"$")
        print("2 - ",the_detox.name," :",the_detox._ingredients," prix :",the_detox.price,"$")
        print("3 - ",the_fresh.name," :",the_fresh._ingredients," prix :",the_fresh.price,"$")
        print("4 - ",the_fusion.name," :",the_fusion._ingredients," prix :",the_fusion.price,"$")
        #print(cocktail._listCocktail,"\n")

        # Choisir un cocktail

        choix_cocktail = int(input("Choisisser un cocktail : "))
        if choix_cocktail == 1:
            cocktail._selectedCocktail = the_boost
        elif choix_cocktail == 2:
            cocktail._selectedCocktail = the_detox
        elif choix_cocktail == 3:
            cocktail._selectedCocktail = the_fresh
        elif choix_cocktail == 4:
            cocktail._selectedCocktail = the_fusion
        else:
            choix_cocktail = int(input("Choisisser un cocktail : "))

        print("\n*Vous avez choisit",cocktail._selectedCocktail.name, "pour ",cocktail._selectedCocktail.price,"$*\n")

        # Choix de la taille

        print("Quelle taille souhaitez vous ? : 1-Small  2-Medium  -3Large")

        choix_taille = int(input())

        if choix_taille == 1:
            cocktail._sizeof = Size._type.Small
        elif choix_taille == 2:
            cocktail._sizeof = Size._type.Medium
        elif choix_taille == 3:
            cocktail._sizeof = Size._type.Large

        print("\n*Vous avez choisit : ",cocktail._sizeof.name,"*")

        cocktail._selectedCocktail.price = prix(cocktail)
        #print("Price : ",cocktail._selectedCocktail.price)


        #Choix du nombre de cocktails identiques

        print("\nCombien en voulez vous ?")

        choix_nombre = int(input())

        cocktail._numberofCocktails = choix_nombre

        print("\n",cocktail._numberofCocktails," pour ",cocktail._selectedCocktail.price * cocktail._numberofCocktails,"$")
        ordernumber = 0
        
        commande.totalPrice = commande.totalPrice + (cocktail._selectedCocktail.price * cocktail._numberofCocktails)
        commande.listecom = commande.listecom + str(cocktail._numberofCocktails) + " " + cocktail._selectedCocktail.name +" pour " + str(cocktail._selectedCocktail.price) +"$\n"

        encore = input("\nSouhaitez-vous autre chose ? (oui ou non) : ")

    print("Récapitulatif : \n",commande._listecommande)
    print("\nCommande numéro :", commande.orderNumber, "Validée, \nCoût Totale : ",commande.totalPrice)

    paiement = 9999
    while paiement != commande.totalPrice or paiement == 0:
        paiement = float(input("Indiquez la somme que vous souhaitez régler ou 0 pour annuler :"))

    if paiement == commande.totalPrice:
        print("Merci d'avoir commander dans notre établissment ! A bientot")
    if paiement == commande.totalPrice:
        print("Paiement annulé")
    
    nouvelle = int(input("\nreommencer ? taper nimporte quel chiffre sauf 1 : "))
    commande._OrderNumber = commande._OrderNumber + 1

