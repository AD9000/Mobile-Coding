from Food import Food
from Food import MainFood
from Food import Main_size
from Food import ingredients
from Food import patties_type 
from Food import Buns_type
from Food import MainFood_type 
from Food import Sides_and_Drinks
from Food import Other_type
from Food import sides_size

class Order():
    def __init__(self, id):
        self._id = id

        # Food list can be mains and sides...
        self._food_list = []
        self._price  = 0 

    #order a food from main type
    def Order_Main_type_food(self,main_type, bun_type, patty_type, ingredients, siz, quantity):
        for i in range(quantity):
            food = MainFood(0,main_type, bun_type, patty_type, ingredients, siz)
            self.add_food(food)

    #order a food from Sides_and_Drinks type
    def Order_Other_type_food(self,Sides1, size1, quantity):
        for i in range(quantity):
            food = Sides_and_Drinks(0,Sides1, size1)
            self.add_food(food)

    '''
    Refactor opportunity: Let all the update inventory code to pass through this method.
    '''
    # Update the inventory...
    def decreaseInventory(self):
        pass
    
    @property
    def id(self):
        return self._id

    @property
    def foodlist(self):
        return self._food_list 
    
    @property
    def price(self):
        return self._price
    
    def Checkout(self):
        TotalP = 0
        for i in self._food_list:
            TotalP += i.calculate_price()
        self._price = TotalP
        return self._price

    def add_food(self,food):
        self._food_list.append(food)

    def confirm(self):
        return f'Order confirmed!!\n' + self.__str__()

    def getFoodList(self):
        st = ''
        for i in self._food_list:
            if isinstance(i, Sides_and_Drinks):
                if (i.Other_type is None or i.sides_size is None):
                    continue
            st += str(i)

        return st

    def __str__(self):
        return f'===================================\n' + \
            f'Order <order_id: {self.id}>\n' + \
            f'Total Cost: ${self._price}\n' + \
            f'-----------Order Summary-----------\n'  + \
            self.getFoodList() + \
            f'-----------------------------------\n' + \
            f'===================================\n'