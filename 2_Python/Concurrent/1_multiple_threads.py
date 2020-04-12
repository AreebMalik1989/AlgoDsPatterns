#!/usr/bin/env python3
""" Threads that waste CPU cycles """

import os
import threading


def cpu_waster():
    """ A simple function that wastes CPU cycles forever """
    while True:
        pass


def display_process_info():
    print('\nProcess ID: ', os.getpid())
    print('Thread count: ', threading.active_count())


# Display information about this process
display_process_info()

print('\nStarting 2 CPU wasters...')
for i in range(2):
    threading.Thread(target=cpu_waster).start()


# Display information about this process
display_process_info()
for thread in threading.enumerate():
    print(thread)
