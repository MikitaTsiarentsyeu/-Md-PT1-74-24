import time

start_time = 0
is_started = False

def start():
    global start_time
    global is_started
    is_started = True
    start_time = time.time()

def finish():
    global is_started
    global start_time
    if is_started:
        finish_time = time.time()
        result = finish_time - start_time
        is_started = False
        start_time = 0
        return result


class Time_it:

    start_time = 0
    is_started = False

    def start(self):
        self.is_started = True
        self.start_time = time.time()

    def finish(self):
        if self.is_started:
            result = time.time() - self.start_time
            self.is_started = False
            self.start_time = 0
            return result
