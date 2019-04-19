from Food import Food

from Food import ingredients
from Food import patties_type as patty
from Food import Buns_type as bun

from Food import MainFood_type
from Food import Sides_and_Drinks

from Food import MainFood as main
from Food import Main_size

from Food import Other_type
from Food import sides_size

from OnlineOrderingSystem import OnlineOrderingSystem
from staff import Staff

import pytest

@pytest.fixture
def order_fixture():
    system = OnlineOrderingSystem()

    # Since inventory already exists, there is no need to add anything.
    # If needed Inventory can be initialized here at a later stage...
    
    return system

def test_check_status(order_fixture):
    assert(order_fixture.checkStatus(0) == 'Invalid Order Id!!')

# Place a single order.
def test_successful_main_order_simple(order_fixture):
    assert(order_fixture.placeOrder(MainFood_type.Burger, bun.muffin_buns, patty.chicken_patties, [ingredients.tomato], Main_size.Single, Other_type.Fries, sides_size.Small) == None)
    orders = order_fixture.getOrderList
    assert(orders[0].id == 0)
    assert(orders[0].price == 17.5)

# Place successive orders to check.
def test_successful_main_order_complex(order_fixture):

    # Order #1: Full order.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Burger, bun.muffin_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Fries, sides_size.Large) == None)
    orders = order_fixture.getOrderList
    assert(orders[0].id == 0)
    assert(orders[0].price == 25)

    # Order #2: Full order, no sides.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Burger, bun.muffin_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Double) == None)
    orders = order_fixture.getOrderList
    assert(orders[1].id == 1)
    assert(orders[1].price == 18)

    # Order #3: Wrap with coke.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Wrap, bun.muffin_buns, patty.vegetarian, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Double, Other_type.Coke, sides_size.Can) == None)
    orders = order_fixture.getOrderList
    assert(orders[2].id == 2)
    assert(orders[2].price == 20)

# Cannot place order with an invalid main.
def test_unsuccessful_main_order_simple(order_fixture):
    # Order #1: No Main_type.
    # Must not be able to place this order
    assert(order_fixture.placeOrder(None, bun.muffin_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Fries, sides_size.Large) == 'Failed to place order.')


def test_unsuccessful_main_order_Complex(order_fixture):
    # Order #1: No bun_type. Not allowed!!
    # Must not be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Wrap, None, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Fries, sides_size.Large) == 'Failed to place order.')

    # uncomment line to see errors:
    #raise AssertionError

    # Order #2: Side size exists but no side exists.
    # Must not be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Wrap, bun.sesame_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, None, sides_size.Large) == 'Failed to place order.')

    # uncomment line to see errors:
    #raise AssertionError

    # Order #3: Side exists but no side size exists.
    # Must not be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Wrap, bun.sesame_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Coke, None) == 'Failed to place order.')

    # uncomment line to see errors:
    #raise AssertionError

    # Order #4: Invalid ingredient.
    # Must not be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Wrap, bun.sesame_buns, patty.beef, [patty.chicken_patties, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Coke, sides_size.Bottle) == 'Failed to place order.')

    # uncomment line to see errors:
    #raise AssertionError

    # After all the unsuccessful orders, the orderId must not have changed.
    assert(order_fixture.getOrderId == 0)


def test_staff_update_orders(order_fixture):
    # Test what happens if the staff updates the orders...
    # Note: Only staff that has an account in the System can do this (ideally)
    
    # Order #1: Full order.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Burger, bun.muffin_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Fries, sides_size.Large) == None)
    orders = order_fixture.getOrderList
    assert(orders[0].id == 0)
    assert(orders[0].price == 25)

    # Status of this order should be being prepared. (Say this is the customer checking the status)
    assert(order_fixture.checkStatus(0) == 'Order being prepared...')
    
    # Create a staff object to change status:
    # Staff FOR THIS SYSTEM ONLY.
    s = Staff(order_fixture)
    assert(s.checkStatus(0) == 'Order being prepared...')
    
    # Update the status: Prepared!
    s.updateStatus(0)

    # Staff checks this.
    assert(s.checkStatus(0) == 'Order Ready!')

    # Customer checks this.
    assert(order_fixture.checkStatus(0) == 'Order Ready!')

    # Invalid checking...
    assert(s.checkStatus(1) == 'Invalid Order Id!!')
    assert(order_fixture.checkStatus(1) == 'Invalid Order Id!!')


    # Same with multiple orders...

    # Order #1: Full order.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Burger, bun.muffin_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Single, Other_type.Fries, sides_size.Large) == None)
    orders = order_fixture.getOrderList
    assert(orders[1].id == 1)
    assert(orders[1].price == 25)

    # Order #2: Full order, no sides.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Burger, bun.muffin_buns, patty.beef, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Double) == None)
    orders = order_fixture.getOrderList
    assert(orders[2].id == 2)
    assert(orders[2].price == 18)

    # Order #3: Wrap with coke.
    # Must be able to place this order
    assert(order_fixture.placeOrder(MainFood_type.Wrap, bun.muffin_buns, patty.vegetarian, [ingredients.tomato, ingredients.swiss_cheese, ingredients.tomato_sauce], Main_size.Double, Other_type.Coke, sides_size.Bottle) == None)
    orders = order_fixture.getOrderList
    assert(orders[3].id == 3)
    assert(orders[3].price == 22)

    # Status of this order should be being prepared. (Say this is the customer checking the status)
    assert(order_fixture.checkStatus(1) == 'Order being prepared...')
    assert(order_fixture.checkStatus(2) == 'Order being prepared...')
    assert(order_fixture.checkStatus(3) == 'Order being prepared...')
    
    # Create a staff object to change status:
    # Staff FOR THIS SYSTEM ONLY.
    s = Staff(order_fixture)
    assert(s.checkStatus(1) == 'Order being prepared...')
    assert(s.checkStatus(2) == 'Order being prepared...')
    assert(s.checkStatus(3) == 'Order being prepared...')
    
    # Update the status: Prepared!
    s.updateStatus(1)
    s.updateStatus(2)

    # Staff checks this.
    assert(s.checkStatus(1) == 'Order Ready!')
    assert(s.checkStatus(2) == 'Order Ready!')
    assert(s.checkStatus(3) == 'Order being prepared...')

    # Customer checks this.
    assert(order_fixture.checkStatus(1) == 'Order Ready!')
    assert(order_fixture.checkStatus(2) == 'Order Ready!')
    assert(order_fixture.checkStatus(3) == 'Order being prepared...')

    # Invalid checking...
    assert(s.checkStatus(5) == 'Invalid Order Id!!')
    assert(order_fixture.checkStatus(-1) == 'Invalid Order Id!!')

    # Updating status of invalid id:
    assert(s.updateStatus(100) == 'Invalid Order Id!!')
    