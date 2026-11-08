# --- stopwatch.py ---

import time

class StopWatch:
    def __init__(self, time_interval=0.0):
        self.interval = time_interval
        self.start = 0.0
        self.end = 0.0
        self.elapsed_time = 0.0
        self.ticking = False
        self.alarm = False

    def reset(self):
        self.start = 0.0
        self.end = 0.0
        self.ticking = False
        self.alarm = False
        self.elapsed_time = 0.0

    def set_interval(self, new_interval):
        self.interval = new_interval

    def start_timer(self):
        self.reset()
        if self.ticking == False:
            self.ticking = True
            self.start = time.time()

    def get_elapsed_time(self):
        return self.elapsed_time

    def tick(self):
        if self.ticking:
            # get the current time-stamp
            self.end = time.time()
            # calcualte the elpased time difference
            self.elapsed_time += self.end - self.start
            # the starting position is now set to the ending position.
            self.start = self.end

        # Run this each time, but it will only sound off
        # when elapsed time is larger than the time interval.
        self.trip_alarm()

    def trip_alarm(self):
        if self.elapsed_time > self.interval:
            self.ticking = False
            # Yes! The alarm has tripped!
            self.alarm = True

        return self.alarm
# Copyright © 2026 John C. Partridge and LogosTeach.
# These files are for educational purposes only.
# The copyright and trademark of these files belong to John C. Partridge and LogosTeach.

