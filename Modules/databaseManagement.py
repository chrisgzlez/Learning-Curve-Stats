import sqlite3
import re
from beautifultable import BeautifulTable
from dataclasses import dataclass, field
import datetime as dt

# NOTES:
  # SQLITE3:
    # cannot create table without columns
    # cannot change name or delete column in sqlite3
    # cannot use ? to include table names or table columns, just Values
    # can use (and will use) string formatting to do such tasks


  # BEAUTIFULTABLE:
    # table = BeautifulTable()
    # table.rows.append(["value1", value2,])     adding values to it
    # table.rows.header([1, 2, 3,])      indexing the table
    # table.columns.header(["column1", "column2", ])     adding column names


# FUTURE CHANGES:
#     CREATE A CLASS OBJECT FOR EACH PROGRAM NAME AND RESTRUCTURE THE PROGRAM IN AN OOP


# TO CREATE AN ACTUAL DATABASE
# con = sqlite3.connect("programs-database.db")


# MAYBE I SHOULD ALSO ADD TO THIS MODULE THE _PROGRAM AND PROGRAM CLASSES FROM MAIN.PY

@dataclass
class _ProgramBase:
    name: str


@dataclass
# frozen means read-only, so no modifying the data
class Program(_ProgramBase):
    time_array = {}
    # sort_index: int = field(init=False, repr = False)

    @staticmethod
    def get_time():
        timestamp = str(dt.datetime.now())
        timestamp_pattern = r"(?P<Date>((-)*([0-9]{2,4})){3}) (?P<Time>((:)*([0-9]{2})){3})"
        match = re.match(timestamp_pattern, timestamp)
        # in case of an update changing the format of the dates
        if not match:
            print("""ERROR
                    It has not been matched
                    CHECK main.py, timestamp_pattern""")
        return match

    def start_monitoring(self):
        match = self.get_time()
        date = match.group("Date")
        time = match.group("Time")
        self.time_array[date] = time
        print(f"Program: {self.name} Initialized at {time} on {date}")

    def stop_monitoring(self) -> tuple:
        for date, time in self.time_array.items():
            return date, time, self.get_time().group("Time")


@dataclass
class _DataBase:
    db: str = field(init=False)
    con: sqlite3.Connection = field(init=False)
    cur: sqlite3.Cursor = field(init=False)

    def __post_init__(self):
        self.db = ":memory:"
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()


@dataclass
class DataBase(_DataBase, Program):

    def create_table(self) -> None:
        self.cur.execute(f"CREATE TABLE {self.name} (DATE, START_TIME, END_TIME)")
        # for column in columns:
        #   self.cur.execute(f"CREATE TABLE {self.name} ({column})") if column == columns[0] \
        #        else self.cur.execute(f"ALTER TABLE {self.name} ADD {column}")

    # add the monitored data to the database
    def add_data(self, timestamps: tuple):
        date, init_time, end_time = timestamps
        self.cur.execute(f"""INSERT INTO {self.name} (DATE, START_TIME, END_TIME) 
            VALUES (?, ?, ?)""", (date, init_time, end_time))

    def gen_data(self, *columns) -> None:
        a, b = columns
        for i in range(10):
            self.cur.execute(f"""INSERT INTO {self.name} ({a}, {b}) VALUES (?, ?);""", (i, i))

    def show_table(self):
        table = BeautifulTable()
        self.cur.execute(f"SELECT * FROM {self.name};")
        result = self.cur.fetchall()
        table.columns.header = ["Date", "Start_Time", "End_Time"]
        # adding rows to BeautifulTable
        for row in result:
            temp = []
            for value in row:
                temp.append(value)
            table.rows.append(temp)

        print(table)





# --------------------- THINGS


# @dataclass
# class _DataBase:
#     db: str = ":memory:"
#     con: sqlite3.Connection = sqlite3.connect(db)
#     cur: sqlite3.Cursor = con.cursor()


# @dataclass
# class DataBase(_DataBase, Program):
#     def create_table(self):
#         self.cur.execute(f"CREATE TABLE {self.name} (a)")

#     def get_data(self):
#         self.cur.execute(f"INSERT INTO {self.name} VALUES (38)")

#     def iterate_through_args():
#         for i in range(5):
#             yield(i, )

#     def get_all(self):
#         self.cur.execute(f"SELECT * FROM {self.name}")
#         result = self.cur.fetchall()
#         for row in result:
#             print(row)
