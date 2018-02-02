#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: taxi_sim.py
@time: 18/1/29 10:16
"""

import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    '''
    Tests of taxi_process::
    >>> taxi = taxi_process(ident = 13, trips = 3, start_time = 0)
    >>> next(taxi)
    Event(time=0, proc=13, action='Leave garage')
    >>> taxi.send(_.time + 7)
    Event(time=7, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 23)
    Event(time=30, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 5)
    Event(time=35, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 48)
    Event(time=83, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 1)
    Event(time=84, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 10)
    Event(time=94, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 1)
    Event(time=95, proc=13, action='going home')
    >>> taxi.send(_.time + 1)
    Traceback (most recent call last):
    ...
    StopIteration
    '''
    time = yield Event(start_time, ident, 'Leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')


class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi: {}{}  {}'.format(proc_id, proc_id * '   ', current_event))
            action_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = action_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def compute_duration(previous_action):
    if previous_action in ['Leave garage', 'drop off passenger']:
        iterval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        iterval = TRIP_DURATION
    elif previous_action == 'going home':
        iterval = 1
    else:
        raise ValueError('Unknown previous_action:{}'.format(previous_action))
    return int(random.expovariate(1 / iterval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    if seed is not None:
        random.seed(seed)
    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                        default=DEFAULT_END_TIME,
                        help='simulation end time; default = {}'.format(DEFAULT_END_TIME))
    parser.add_argument('-t', '--taxis', type=int,
                        default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = {}'.format(DEFAULT_NUMBER_OF_TAXIS))
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)