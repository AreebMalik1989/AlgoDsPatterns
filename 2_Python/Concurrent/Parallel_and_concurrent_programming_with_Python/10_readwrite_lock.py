#!/usr/bin/env python3
""" Several users reading a calendar, but only a few users updating it """

import threading
from readerwriterlock import rwlock

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
marker = rwlock.RWLockFair()


def calendar_reader(id_number):
    global today
    read_marker = marker.gen_rlock()
    name = 'Reader-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        read_marker.acquire()
        print(name, 'sees that today is', WEEKDAYS[today], '-read count:', read_marker.c_rw_lock.v_read_count)
        read_marker.release()


def calender_writer(id_number):
    global today
    writer_marker = marker.gen_wlock()
    name = 'Writer-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        writer_marker.acquire()
        today = (today+1) % 7
        print(name, 'updated data to', WEEKDAYS[today])
        writer_marker.release()


if __name__ == "__main__":

    # Create 10 reader threads
    for i in range(10):
        threading.Thread(target=calendar_reader, args=(i,)).start()

    # ... but only 2 writer threads
    for i in range(2):
        threading.Thread(target=calender_writer, args=(i,)).start()
