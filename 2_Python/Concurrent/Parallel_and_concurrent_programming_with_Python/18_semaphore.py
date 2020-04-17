#!/usr/bin/env python3
""" Connecting cell phones to a charger """


import random
import threading
import time

charger = threading.Semaphore(2)


def cell_phone():
    name = threading.current_thread().getName()
    with charger:
        print(name, 'is charging...')
        time.sleep(random.uniform(1, 2))
        print(name, 'is done charging!')


if __name__ == "__main__":

    for phone in range(10):
        threading.Thread(target=cell_phone, name='Phone-'+str(phone)).start()
