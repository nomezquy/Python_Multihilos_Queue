from ast import arg
from asyncio import threads
from datetime import datetime, timedelta
import random
from threading import Thread
import time
import uuid

class OrderManager:
    __orders_processed = 0
    __last_printed_log = datetime.now()         
        
    def _generate_order(self):  
        
        """
            Method for generate the order code to save.
            
            Returns:
                uuid: Order code

        """   
        return  uuid.uuid4()
    
    def _saveOrder(self, sourceStorage, order):
        
        """
            Method for save the order in the storage,
            for the exercise in the Queue

        Args:
            sourceStorage (Object): Objet Queue for append the order.
            order (str): Code of Order to save.
        """
        sourceStorage(order)
        
    def _log(self, message):
        
        """
            Method for generate the log estructure and print

        Args:
            message (str): Text to print in console
        """
        print(f"{datetime.now()} > {message}")
        
    def processOrder(self, dataOrder, removeOrder) -> None:
        """
            Method in charge of simulating the order processing
            by incrementing counter and log printout 

        Args:
            order (Str): order information to be processed
        """
        if(dataOrder != None):            
            id= dataOrder
            if removeOrder():
                self.__orders_processed += 1            
                self._log(message=f"Order { self.__orders_processed}  [{id}] was successfully prosecuted.")
                time.sleep(random.uniform(0, 1))
            
           
    
                
    def Run_process_orders(self, order_source, order_data, order_remove, quantityThread):
        """
            Method for managing the processing of orders
            and the resources allocated to them. 
        
            Args:
            order_source (Funtion): This function indicates if there are pending orders 
            order_data (Funtion): This function provides the information of the order to process
            order_remove (Funtion): This function must be executed to remove the pending order.
            quantityThread (Int): Number of Thread asigned in the process
        """        
        while(order_source()):                       
            for n in range(quantityThread):
                thread = Thread(target=self.processOrder, args=(order_data(), order_remove,)).start()      
                           
        if(order_source() == False):
            self._log(
                            message="All orders were processed"
                        )
                             
            
            
            