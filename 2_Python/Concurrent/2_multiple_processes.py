#!/usr/bin/env python3
""" Processes that waste CPU cycles """

import os
import threading
import multiprocessing as mp


def cpu_waster():
    """ A simple function that wastes CPU cycles forever """
    while True:
        pass


def display_process_info():
    print('\nProcess ID: ', os.getpid())
    print('Thread count: ', threading.active_count())


print('Hi! My name is', __name__)
if __name__ == "__main__":

    # Display information about this process
    display_process_info()

    print('\nStarting 2 CPU wasters...')
    for i in range(2):
        mp.Process(target=cpu_waster).start()

    # Display information about this process
    display_process_info()
    for thread in threading.enumerate():
        print(thread)
