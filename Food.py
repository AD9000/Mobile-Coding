from abc import ABC
from enum import Enum, unique

class MainFood_type(Enum):
    Burger = 0
    Wrap = 1

    def __str__(self):
        return self.name
 
class Buns_type(Enum):
    sesame_buns = 0
    muffin_buns = 1

    def __str__(self):
        return self.name

class patties_type (Enum):
    chicken_patties = 0
    vegetarian = 1
    beef = 2

    def __str__(self):
        return self.name

class ingredients(Enum):
    tomato = 0
    lettuce = 1
    tomato_sauce = 2
    cheddar_cheese = 3
    swiss_cheese = 4

    def __str__(self):
        return self.name

# Making the size enums actually equal to the size of the order...
class Main_size(Enum):
    Single = 1
    Double = 2

    def __str__(self):
        return self.name

class Food(ABC):

    def __init__(self, price):
        self._price = 0

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f'Food <{self._price}>'

    #@abstractmethod
    def calculate_price(self):
        pass

class MainFood(Food):
    def __init__(self, price, MainFood_type, Buns_type, patties_type, ingredients, size):
        Food.__init__(self, price)
        self._size = size
        self._MainFood_type = MainFood_type
        self._Buns_type = Buns_type
        self._patties_type = patties_type
        self._ingredients = ingredients

    
    def size(self):
        return self._size

    def patties_type(self):
        return self._patties_type

    def Buns_type(self):
        return self._Buns_type

    def MainFood_type(self):
        return self._MainFood_type

    def calculate_price(self):
        Main_price = 0
        if self._Buns_type == Buns_type.muffin_buns:
             Main_price += 8
        if self._Buns_type == Buns_type.sesame_buns:
             Main_price += 8

        if self._patties_type == patties_type.chicken_patties:
             Main_price += 5
        if self._patties_type == patties_type.beef:
             Main_price += 6
        if self._patties_type == patties_type.vegetarian:
             Main_price += 3
        if self.size == Main_size.Double:
             Main_price += 5
        for i in self._ingredients:
            if i == ingredients.tomato:
                Main_price += 1.5
            if i == ingredients.tomato_sauce:
                Main_price += 0.5
            if i == ingredients.cheddar_cheese:
                Main_price += 1.2
            if i == ingredients.lettuce:
                Main_price += 0.7
            if i == ingredients.swiss_cheese:
                Main_price += 2
        return Main_price

    def getStringIngredients(self):
        st = '\n'
        for i in self._ingredients:
            st += str(i) + '\t\n'
        
        # Remove the last '\n'
        return st[:-1]

    def __str__(self):
        return f'-----------MAIN----------\n' + \
                f'Mains: {self._MainFood_type}\n' + \
                f'Buns_type: {self._Buns_type}\n' + \
                f'patties_type: {self._patties_type}\n' + \
                f'ingredients: {self.getStringIngredients()}\n' + \
                f'size: {self._size}\n' + \
                f'-------------------------\n'

class Other_type(Enum):
    Fries = 0
    Coke = 1
    Sprite = 2
    Fanta = 3
    Water = 4
    Nuggets = 5
    Juice = 6
    
    def __str__(self):
        return self.name


class sides_size(Enum):
    # Sizes for the juice and the fries. (and nugget packs)
    Small = 2
    Medium = 3
    Large = 4

    # Sizes for the drinks...
    Can = 0
    Bottle = 1

    def __str__(self):
        return self.name

class Sides_and_Drinks(Food):
    def __init__(self, price, Other_type, sides_size):
        Food.__init__(self,price)
        self._sides_size = sides_size
        self._Other_type = Other_type

    @property
    def sides_size(self):
        return self._sides_size
     
    @property
    def price(self):
        return self._price

    def Other_type(self):
        return self._Other_type
        
    def __str__(self):
        return f'----------SIDES----------\n' + \
               f'Sides: {self._Other_type}\n' + \
               f'size: {self._sides_size}\n' + \
               f'-------------------------\n'

    def calculate_price(self):
        total_price = 0
        if self._sides_size == sides_size.Medium or self._sides_size == sides_size.Can:
            total_price += 2
        elif self._sides_size == sides_size.Large or self._sides_size == sides_size.Bottle:
            total_price += 4
        if self._Other_type == Other_type.Coke:
             total_price += 3
        elif self._Other_type == Other_type.Water:
             total_price += 2
        elif self._Other_type == Other_type.Fanta:
             total_price += 3
        if self._Other_type == Other_type.Fries:
             total_price += 3
        if self._Other_type == Other_type.Nuggets:
             total_price += 5
        return total_price

