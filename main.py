#Create the Classes Programs and Data
import re
from dataclasses import dataclass
import datetime as dt
import sqlite3
from .Modules import databaseManagement as dm



@dataclass
class _ProgramBase:
    name: str


@dataclass
#frozen means read-only, so no modifying the data
class Program(_ProgramBase):

    #sort_index: int = field(init=False, repr = False)

    def time_monitoring(self):
        timestamp = str(dt.datetime.now())
        timestamp_pattern = r"(?P<Date>((-)*([0-9]{2,4})){3}) (?P<Time>((:)*([0-9]{2})){3})"
        match = re.match(timestamp_pattern, timestamp)
        #in case of an update changing the format of the dates
        if not match:
            print("""ERROR
                    It has not been matched
                    CHECK main.py, timestamp_pattern""")
        date = match.group("Date")
        time = match.group("Time")
        print(f"Program: {self.name} Initialized at {time} on {date}")



if __name__ == '__main__':
    VSCode = dm.DataBase("VSCode", "Age", "Place_of_Birth")
    print(VSCode)
    VSCode.time_monitoring()
    
    VSCode.create_table()
    VSCode.get_data()
    VSCode.get_all()
