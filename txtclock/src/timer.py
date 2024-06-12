import time
import math

class Timer:

    def __init__(self, seconds, msg):
        self.seconds = seconds
        self.msg = msg
        self.start_time = time.time()
        self.end_time = self.start_time + seconds
        self.elapsed_timer_mode = (seconds == 0)


    @property
    def elapsed(self) -> float:
        return time.time() - self.start_time


    @property
    def finished(self) -> bool:
        if self.elapsed_timer_mode:
            return False

        return time.time() >= self.end_time


    @property
    def remaining(self) -> float:
        if self.elapsed_timer_mode:
            return 0

        return time.time() - self.end_time


    @property
    def duration_str(self):
        return Timer.seconds2str(self.seconds)


    @property
    def remaining_str(self):
        _val = self.remaining
        if _val:
            return Timer.seconds2str(math.floor(_val))
        else:
            return "00:00"

    @property
    def elapsed_str(self):
        _val = self.elapsed
        if _val:
            return Timer.seconds2str(math.floor(_val))
        else:
            return "00:00"


    @staticmethod
    def seconds2str(seconds):
        _str = ""
        hours = 0
        minutes = 0

        if seconds < 0:
            _str += "-"
            seconds *= -1

        if seconds > 3600:
            hours = seconds // 3600
            seconds -= hours * 3600
            _str += f"{hours:02}:"

        if seconds > 60:
            minutes = seconds // 60
            seconds -= minutes * 60

        _str += f"{minutes:02}:"
        _str += f"{seconds:02}"

        return _str
