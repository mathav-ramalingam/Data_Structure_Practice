# 1) Design a food ordering system where your python program will run two threads,
#     Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#     Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it.This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def place_order(self,items):
        for item in items:
            print("Placing order for:",item)
            self.buffer.append(item)
            time.sleep(0.5)

    def server_order(self):
        time.sleep(1)
        while self.buffer:
            item = self.buffer.popleft()
            print("Now serving: ",item)
            time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    obj = Queue()
    t1 = threading.Thread(target = obj.place_order, args=(orders,))
    t2 = threading.Thread(target = obj.server_order)

    t1.start()
    t2.start()

