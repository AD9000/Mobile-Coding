from order import Order
from Inventory import Inventory
from Food import Food

from Food import ingredients
from Food import patties_type 
from Food import Buns_type

from Food import MainFood_type 
from Food import Sides_and_Drinks

from Food import MainFood
from Food import Main_size

from Food import Other_type
from Food import sides_size

from Errors import Errors

class OnlineOrderingSystem():
    def __init__(self):
        self._prepared = []
        self._ordered = []
        self._order_list = []
        self._inventory = Inventory()
        self._orderId = 0

    @property
    def inventory(self):
        return self._inventory
    
    @property
    def getOrdered(self):
        return self._ordered

    @property
    def getPrepared(self):
        return self._prepared

    @property
    def getOrderList(self):
        return self._order_list

    @property
    def getOrderId(self):
        return self._orderId

    # Add to prepared List
    def updatePrepared(self, orderId):
        self._prepared.append(orderId)

    # Remove from ordered List
    def updateOrdered(self, orderId):
        self._ordered.remove(orderId)

    def checkOrderErrors(self, main_type, bun_type, patty_type, ingredients, Main_size, main_q, Other_type, sides_size, side_q):
        errors = Errors(main_type, bun_type, patty_type, ingredients, Main_size, main_q, Other_type, sides_size, side_q, self._inventory)
        err = errors.check()
        if (self.checkErrors(err)):
            return 'Failed to place order.'
        
    def staffMainErrors(self, main_type, main_size, main_q):
        errors = Errors(main_type, None, None, None, main_size, main_q, None, None, None, None)
        err = errors.staffCheckMain()
        if self.checkErrors(err):
            return 'Failed to update main.'
    
    def staffSideErrors(self, side, side_size, side_q):
        errors = Errors(None, None, None, None, None, None, side, side_size, side_q, None)
        err = errors.staffCheckSides()
        if self.checkErrors(err):
            return 'Failed to update sides.'

    # Check if there are any errors...
    def checkErrors(self, errors):
        # If there are no errors:
        if not errors:
            return False
        
        # Otherwise return them...
        else:
            return errors

    # Refactor Opportunity: Let placeOrder method only accept Food objects instead of all the data.
    # Function to order food.
    # Sides are optional...
    # If no parameters are passed, default to None
    def placeOrder(self, main_type = None, bun_type = None, patty_type = None, ingredients = None, Main_size = None, Other_type = None, sides_size = None, main_q = 1, side_q = 1):
        # Create an order for the customer...
        ord = Order(self._orderId)

        # Check if order can be placed...
        err = self.checkOrderErrors(main_type, bun_type, patty_type, ingredients, Main_size, main_q, Other_type, sides_size, side_q)
        if err is not None:
            return err
               
        # Place an order...
        ord.Order_Main_type_food(main_type, bun_type, patty_type, ingredients,Main_size, main_q)
        ord.Order_Other_type_food(Other_type, sides_size, main_q)

        # Checkout and calculate the price...
        ord.Checkout()

        # Confirm the order!
        print(ord.confirm())

        self._order_list.append(ord)

        # Successful order!: Increment order id
        self._ordered.append(self._orderId)
        self._orderId += 1

        # Update the inventory in preparation for the next order...
        self._inventory.updateInventory(main_type, Main_size, main_q, Other_type, sides_size, side_q)


    # Refactor Opportunity: Placing an order again can be done by calling placeOrder again. perhaps an id field would work
    def Order_More(self, ord, main_type, bun_type, patty_type, ingredients, Main_size,Other_type, sides_size):
        # Place an order...
        ord.Order_Main_type_food(main_type, bun_type, patty_type, ingredients,Main_size)
        ord.Order_Other_type_food(Other_type, sides_size)
        ord.confirm()
        self._order_list.append(ord)
    
    # Check status of an order. Anybody can do this.
    def checkStatus(self, orderId):
        if (orderId in self._ordered):
            return 'Order being prepared...'
        elif (orderId in self._prepared):
            return 'Order Ready!'
        else:
            return 'Invalid Order Id!!'

    # Parse the form and get the errors:
    def parse(self, form):
        err = self.checkOrderErrors(form.get('main_type'), form.get('bun_type'), form.get('patty_type'), form.get('ingredients'), form.get('main_size'), form.get('main_q'), form.get('sides'), form.get('side_q'), self._inventory)
        if err:
            return err
