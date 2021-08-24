#Create the Classes Programs and Data
import re
from dataclasses import dataclass
import datetime as dt
import sqlite3


@dataclass
class _DataBase:
    db: str
    con: sqlite3.Connection
    cur: sqlite3.Cursor
    
    def __post_init__(self):
        self.db = ":memory:"
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.cursor()



@dataclass
class _ProgramBase:
    name: str




@dataclass
#frozen means read-only, so no modifying the data
class Program(_ProgramBase):

    #sort_index: int = field(init=False, repr = False)

    def time_monitoring(self):
        timestamp = str(dt.datetime.now())
        date_pattern = r"(?P<Date>((-)*([0-9]{2,4})){3}) (?P<Time>((:)*([0-9]{2})){3})"
        match = re.match(date_pattern, timestamp)
        #in case of an update changing the format of the dates
        if not match:
            print("""ERROR
                    It has not been matched
                    CHECK classes.py, date_pattern""")
        date = match.group("Date")
        time = match.group("Time")
        print(f"Program: {self.name} Initialized at {time} on {date}")



@dataclass
class DataBase(Program, _DataBase):
    def create_table(self):
        self.cur.execute("CREATE TABLE %s (a)" %self.name)

    def get_data(self):
        self.cur.execute("INSERT INTO %s VALUES (38)" %self.name)

    def iterate_through_args():
        for i in range(5):
            yield(i, )

    def get_all(self):
        self.cur.execute("SELECT * FROM %s" %self.name)
        result = self.cur.fetchall()
        for row in result:
            print(row)






if __name__ == '__main__':
    VSCode = DataBase("VSCode")
    print(VSCode)
    VSCode.time_monitoring()
    
    VSCode.create_table()
    VSCode.get_data()
    VSCode.get_all()
