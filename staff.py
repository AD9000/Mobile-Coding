#from OnlineOrderingSystem import OnlineOrderingSystem

class Staff():
    def __init__(self, sys):
        self._sys = sys

    # Update status of an order
    # The staff must not enter an invalid id.
    def updateStatus(self, orderId):
        if (orderId in self._sys.getOrdered):
            if orderId not in self._sys.getPrepared:
                self._sys.updatePrepared(orderId)
                self._sys.updateOrdered(orderId)
        else:
            return 'Invalid Order Id!!'

    # # A staff can add more to the inventory when they wish.
    # # Either main or sides can be None
    # def updateInventory(self, main_type = None, main_size = None, main_q = None, side = None, side_size = None, side_q = None):
    #     # Hacky way ahahaahhaahhahahahhahaahahahaha
    #     # Pass negative values to the update inventory function to add to inventory!
    #     if (main_type == None or main_size == None or main_q == None) and not (main_type == None and main_size == None and main_q == None):
    #         return 'Invalid Main'

    # Separating the two functions for ease of calling.
    def updateMain(self, main_type, main_size, main_q):
        err = self._sys.staffMainErrors(main_type, main_size, main_q)
        if err is not None:
            return err  

        # Passing negative values!
        main_q = -main_q
        self._sys.inventory.updateInventory(main_type, main_size, main_q, auth = self)

    def updateSides(self, side, side_size, side_q):
        err = self._sys.staffSideErrors(side, side_size, side_q)
        if err is not None:
            return err  

        # Passing negative values!
        side_q = -side_q
        self._sys.inventory.updateInventory(side, side_size, side_q, auth = self)

    def checkStatus(self, orderId):
        return self._sys.checkStatus(orderId)