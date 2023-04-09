from datetime import datetime
from dataclasses import dataclass

@dataclass
class Shift:
    """Class of one shift with attrs """
    def __init__(self, day_of_month: int, shift_start_time: datetime, shift_end_time: datetime, is_weekend: bool):
        self.day_of_month = day_of_month
        self.start_time = shift_start_time
        self.end_time = shift_end_time
        self.is_weekend = is_weekend



