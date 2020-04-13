#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading
import time

items_on_notepad = 0
pencil = threading.Lock()


def shopper():
    global items_on_notepad
    name = threading.current_thread().getName()
    items_to_add = 0
    while items_on_notepad <= 20:
        if items_to_add and pencil.acquire(blocking=False):  # Add item(s) to shared items_on_notepad
            items_on_notepad += items_to_add
            print(name, 'added', items_to_add, 'item(s) to the notepad')
            items_to_add = 0
            time.sleep(0.3)  # Time spent writing
            pencil.release()
        else:  # Look for other things to buy
            time.sleep(0.1)
            items_to_add += 1
            print(name, 'found something else to buy')


if __name__ == "__main__":

    barron = threading.Thread(target=shopper, name='Barron')
    olivia = threading.Thread(target=shopper, name='Olivia')

    start_time = time.perf_counter()

    barron.start()
    olivia.start()

    barron.join()
    olivia.join()

    elapsed_time = time.perf_counter() - start_time
    print('Elapsed time: {:.2f} seconds'.format(elapsed_time))
