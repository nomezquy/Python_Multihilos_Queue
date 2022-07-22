class Queue:
    
    def __init__(self) -> None:
        """
            Constructor that inicializes the queue
        """                
        self._orders = []
        
    
    def appendOrder(self, order):
        """
            Method for append orders in the queue.

        Args:
            order (str): order at append in the queue
        """        
        self._orders.append(order)
        
        
    def deleteOrder(self):
        """
            Method for delete the first order in the queue
        """
        if(self._orders != []):                 
            self._orders.pop(0)
            return True    
        
    def firstOrderInformation(self):
        """
            Method for return the info of the next order to process

        Returns:
            Str: Information of the Order
        """
        if(self._orders != []): 
            return self._orders[0]
        
        
    def validateStatus(self):
        """
            Method for validate if the queue have orders pending
        
            Returns:
                Bool: Returns true in case there are pending orders.
        """
        if self._orders != []:
            return True
        else:
            return False
        
        
    def checkQuantity(self):
        """
            Methon for check quantity of orders in the Queue

        Returns:
            Str: Return the number of orders in the Queue
        """
        return str(len(self._orders))

        



        