from queue import Queue
from manager import OrderManager
from datetime import datetime
import time

OrderQuantity = 1000
threadQuantity = 4


def _fakeOrders(queue, manager, quantity):
    """Funtion for simulate the receive the fake orders

    Args:
        queue (Object): Queue where fake orders are stored
        manager (Object): Objet that manages the excecution
        quantity (int): Quantity of fake orders to save
    """
    for x in range(quantity):        
        manager._saveOrder(queue.appendOrder, manager._generate_order())
    print(f"{quantity} fake orders generated")


if __name__ == '__main__':
    queue = Queue()
    manager = OrderManager()
    start_time = time.time()
    _fakeOrders(queue, manager, OrderQuantity)
    print(f"Number of pending orders in the queue: {queue.checkQuantity()} orders")
    manager.Run_process_orders(queue.validateStatus, queue.firstOrderInformation, queue.deleteOrder, threadQuantity)
    print(f"Number of pending orders in the queue: {queue.checkQuantity()} orders")
    delay = time.time() - start_time
    print(f"{datetime.now()} > Execution time: {delay} seconds...")
