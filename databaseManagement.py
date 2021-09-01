import sqlite3
from beautifultable import BeautifulTable
from dataclasses import dataclass, field
#NOTES:
  #SQLITE3:
    #cannot create table without columns
    #cannot change name or delete column in sqlite3
    # cannot use ? to include table names or table columns, just Values
    # can use (and will use) string formatting to do such tasks


  #BEAUTIFULTABLE:
    #table = BeautifulTable()
    #table.rows.append(["value1", value2,])     adding values to it
    #table.rows.header([1, 2, 3,])      indexing the table
    #table.columns.header(["column1", "column2", ])     adding column names


# FUTURE CHANGES:
#     CREATE A CLASS OBJECT FOR EACH PROGRAM NAME AND RESTRUCTURE THE PROGRAM IN AN OOP


#TO CREATE AN ACTUAL DATABASE
#con = sqlite3.connect("programs-database.db")


#MAYBE I SHOULD ALSO ADD TO THIS MODULE THE _PROGRAM AND PROGRAM CLASSES FROM MAIN.PY



@dataclass
class _DataBase:
    db: str = field(init = False)
    con: sqlite3.Connection = field(init = False)
    cur: sqlite3.cur = field(init = False)
    def __post_init__(self):
        self.db = ":memory:"
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()

@dataclass
class DataBase(_DataBase, Program):
    def create_table(self, *columns): 
        for column in columns:
            self.cur.execute(f"CREATE TABLE {self.name} ({column})") if column == columns[0] else self.cur.execute(f"ALTER TABLE {self.name} ADD {column}")

    #temporary function to have some actual display
    def gen_data(self, *columns):
        a,b = columns
        for i in range(10):
            self.cur.execute(f"""INSERT INTO {self.name} ({a}, {b}) VALUES (?, ?);""", (i, i))

    #don't know what this does
    def iterate_through_args():
        for i in range(5):
            yield(i, )

    def show_table(self):
        table = BeautifulTable()
        self.cur.execute(f"SELECT * FROM {self.name};")
        result = self.cur.fetchall()
        print(result)

        #adding rows to BeautifulTable
        for row in result:
            temp = []
            for value in row:
                temp.append(value)
            table.rows.append(temp)
        
        print(table)





#--------------------- THINGS


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