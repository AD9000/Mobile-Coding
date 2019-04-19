from Food import Food
from Food import MainFood
from Food import Main_size
from Food import ingredients as ing
from Food import patties_type as pat
from Food import Buns_type as bun
from Food import MainFood_type as main
from Food import Other_type as other
from Food import Sides_and_Drinks as sides
from Food import sides_size as sides_size

from staff import Staff

NUM = 10
ML = 10000
G = 20000
PACK_SIZE = 3
JUICE_SIZE = 175 #(ml)
FRIES_SIZE = 175 #(g)

# TODO: Inventory update needed. (Only store required values...)
class Inventory():
    def __init__(self):
        #self._Inventory = {main.Burger: NUM, main.Wrap:NUM, bun.sesame_buns:NUM, bun.muffin_buns:NUM, pat.chicken_patties:NUM, pat.vegetarian:NUM, pat.beef:NUM, ing.tomato:NUM, ing.lettuce:NUM, ing.tomato_sauce:NUM, ing.cheddar_cheese:NUM, ing.swiss_cheese:NUM, other.Coke:ML,other.Fanta:ML,other.Sprite:ML,other.Water:ML,other.Fries:G,other.Nuggets:NUM}
        self._Inventory = {main.Burger: NUM, main.Wrap:NUM, other.Coke:[NUM, NUM], other.Fanta:[NUM, NUM], other.Sprite:[NUM, NUM], other.Water:[NUM, NUM], other.Fries:G, other.Nuggets:NUM, other.Juice: ML}

    @property
    def Inventory(self):
        return self._Inventory
    '''
    List versions of all the functions...
        # Implemented as a list for ease of refactoring later...
        def updateMain(self, main, main_size):
            for i in range(len(main)):
                # At this point, we know all ingredients are available...
                self._Inventory[main[i]] -= main_size[i].value

                # Could do an error check here...(For unexpected errors)
            

        def updateSides(self, side, side_size):
            for i in range(len(side)):
                if side[i] is not None:
                    self.Change_Inventory(side[i], side_size[i])

        def updateInventory(self, main, main_size, side, side_size):
            # Update mains
            self.updateMain(main, main_size)

            if side is not None:
                # Sides is a bit tricky as the storage is different.
                print(side)
                self.updateSides(side, side_size)
    '''

    def _updateMain(self, main, main_size, quantity):
        # At this point, we know all ingredients are available...
        self._Inventory[main] -= main_size.value * quantity

        # Could do an error check here...(For unexpected errors)
        

    def _updateSides(self, side, side_size, quantity):
        if side is not None:
            if side == other.Nuggets:
                self._Inventory[side] -= side_size.value * PACK_SIZE * quantity
            elif side == other.Juice:
                self._Inventory[side] -= side_size.value * JUICE_SIZE * quantity
            elif side == other.Fries:
                self._Inventory[side] -= side_size.value * FRIES_SIZE * quantity
            else:
                self._Inventory[side][side_size.value] -= quantity

    # auth is just a Staff object. If it is passed, we can pass negative values to the function
    # and reuse to update inventory.
    def updateInventory(self, main, main_size, main_q, side, side_size, side_q, auth = None):
        if (not isinstance(auth, Staff) and (main_q < 0 or side_q < 0)):
            return OrderingError('Invalid Authorization to add food to inventory...')

        self._updateMain(main, main_size, main_q)
        self._updateSides(side, side_size, side_q)        

    def isAvailable(self, food, size, quantity):
        if food in self._Inventory:
            if food in [other.Coke, other.Fanta, other.Sprite, other.Water]:
                if self._Inventory[food][size.value] > quantity:
                    return True
                return False

            elif self._Inventory[food] - (size.value * quantity) > 0:
                return True

        return False

    @property
    def not_available_food(self):
        Not_available_food = []
        for i in self._Inventory:
            if self._Inventory[i] == 0:
                Not_available_food.append(i)
        return Not_available_food