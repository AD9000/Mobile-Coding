from Food import Food
from Food import MainFood
from Food import Main_size
from Food import ingredients
from Food import patties_type as patty
from Food import Buns_type as bun
from Food import MainFood_type as main
from Food import Sides_and_Drinks
from Food import Other_type
from Food import sides_size

#from Inventory import Inventory

class OrderingError(Exception):
    def _init_(self,message):
        self.message = message
        
    def _str_(self):
        return self.message

class Errors():
    def __init__(self, main_type, bun_type, patty_type, ingredients, Mainsize, main_q, other, sides, side_q, inventory):
        self._main_type = main_type
        self._bun_type = bun_type
        self._patty_type = patty_type
        self._ingredients = ingredients
        self._msize = Mainsize
        self._mq = main_q
        self._other = other
        self._sides = sides
        self._sq = side_q
        self._inventory = inventory

    # Checks for any None parameters...
    def checkExistence(self, errors):
        if (not isinstance(self._main_type, main)):
            errors['main_type'] = OrderingError('Invalid Main Type')
        
        if (not isinstance(self._bun_type, bun)):
            errors['bun_type'] = OrderingError('Invalid Bun Type')
            
        if (not isinstance(self._patty_type, patty)):
            errors['patty_type'] = OrderingError('Invalid Patty Type')
            
        if (not isinstance(self._msize, Main_size)):
            errors['main_size'] = OrderingError('Invalid Main Size')
        
        if self._ingredients is None:
            errors['ingredients'] = OrderingError('No ingredient specicfied')
        else:
            for i in self._ingredients:
                if (not isinstance(i, ingredients)):
                    errors['ingredient'] = OrderingError('Invalid Ingredient:' + str(i))
                    break

        # Since sides are optional, use special conditions to check for sides...
        if (self._other is not None and not isinstance(self._other, Other_type)):
            errors['side_none'] = OrderingError('Side does not exist')

        if (self._sides is not None and not isinstance(self._sides, sides_size)):
            errors['side_size_none'] = OrderingError('Invalid sides Size')
        
        # At this point, other_type and sides_size pass the two tests
        # But since they are one unit...
        if (self._other is not None and self._sides is None):
            errors['side_size_spec'] = OrderingError('Sides size not specified.')

        if (self._other is None and self._sides is not None):
            errors['side_spec'] = OrderingError('No side specified for the size mentioned.')

        # Check if the sizes match. Only Drinks can have the can/bottle sizes.
        if self._other is not None and self._sides is not None:
            if (self._other in [Other_type.Coke, Other_type.Fanta, Other_type.Sprite, Other_type.Water]):
                if self._sides not in [sides_size.Bottle, sides_size.Can]:
                    # Invalid pair!
                    errors['size_mismatch'] = OrderingError('Invalid sides Size')
            else:
                if self._sides not in [sides_size.Large, sides_size.Medium, sides_size.Small]:
                    # Invalid pair!
                    errors['size_mismatch'] = OrderingError('Invalid sides Size')
        return errors
        
    # Check for the errors
    def check(self):
        errors = {}

        # Check if parameters are valid... 
        # All these cannot be None.    
        errors = self.checkExistence(errors)

        # If any of the parameters were None, there is no need to
        # check for any further errors...
        if errors:
            return errors

        # If all the parameters exist, check if there are sufficient ingredients in the inventory...
        # Just checking for mains and sides...according to the acceptance criteria. Could check all of them
        if not self._inventory.isAvailable(self._main_type, self._msize, self._mq):
            errors['main_stock'] = OrderingError(str(self._main_type) + ' is out of stock')
        
        if (self._other is not None and self._sides is not None) and not self._inventory.isAvailable(self._other, self._sides, self._sq):
            errors['side_stock'] = OrderingError(str(self._other) + ' is out of stock')

        #Further thoughts on errors: Check for the unit (How?)

        return errors

    # Check for any errors caused by passing in the staff object.
    def staffCheckMain(self):
        errors = {}

        if (self._main_type == None or self._msize == None or self._mq == None) and not (self._main_type == None and self._msize == None and self._mq == None):
            errors['main_combi'] = OrderingError('Invalid Main, size and quantity combination')
            return errors

        # After this if any one is None, all are None
        if self._main_type is not None:
            if not isinstance(self._main_type, main):
                errors['main_type'] = OrderingError('Invalid Main')
            if not isinstance(self._msize, Main_size):
                errors['main_size'] = OrderingError('Invalid main size')
            if not isinstance(self._mq, int):
                errors['main_q'] = OrderingError('Quantity must be a number')

        return errors

    def staffCheckSides(self):
        errors = {}
        if (self._other == None or self._sides == None or self._sq == None) and not (self._other == None and self._sides == None and self._sq == None):
            errors['side_combi'] = OrderingError('Invalid side, size and quantity combination')
            return errors

        # After this if any one is None, all are None
        if self._other is not None:
            if not isinstance(self._other, Other_type):
                errors['side_type'] = OrderingError('Invalid Side')
            if not isinstance(self._sides, sides_size):
                errors['side_size'] = OrderingError('Invalid side size')
            if not isinstance(self._mq, int):
                errors['side_q'] = OrderingError('Quantity must be a number')

        return errors
