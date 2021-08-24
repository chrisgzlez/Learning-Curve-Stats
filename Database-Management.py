import sqlite3


#con = sqlite3.connect("programs-database.db")
con = sqlite3.connect(":memory:")
cursor = con.cursor()

def create_table(table_name):

    cursor.execute("CREATE TABLE ? (a)", table_name)

def get_data():
    cursor.execute("INSERT INTO numbers VALUES (38)")

def iterate_through_args():
    for i in range(5):
        yield(i, )


def get_all():
    cursor.execute("SELECT * FROM numbers")
    result = cursor.fetchall()
    for row in result:
        print(row)

print(type(con))





