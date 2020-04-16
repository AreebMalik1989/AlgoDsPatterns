#!/usr/bin/env python3
""" Threads that waste CPU cycles """

import os
import threading

processors_to_use = 1 if os.cpu_count() == 1 else os.cpu_count() - 1


def cpu_waster():
    """ A simple function that wastes CPU cycles forever """
    while True:
        pass


def display_process_info():
    print('\nProcess ID: ', os.getpid())
    print('Thread count: ', threading.active_count())


# Display information about this process
display_process_info()

print('\nStarting', processors_to_use, 'CPU wasters...')
for i in range(processors_to_use):
    threading.Thread(target=cpu_waster).start()


# Display information about this process
display_process_info()
for thread in threading.enumerate():
    print(thread)
