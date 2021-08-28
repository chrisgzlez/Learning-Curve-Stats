import sqlite3
from beautifultable import BeautifulTable

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
#     CREATE A CLASS OBJECT FOR EACH PROGRAM NAME AND REESTRUCTURE THE PROGRAM IN AN OOP


#TO CREATE AN ACTUAL DATABASE
#con = sqlite3.connect("programs-database.db")
con = sqlite3.connect(":memory:")
cursor = con.cursor()

def create_table(table_name, *columns):
    global table1 
    table1 = []


    for column in columns:

        if table1 == []:
            cursor.execute(f"CREATE TABLE {table_name} ({column})")
            #cursor.execute(f"CREATE TABLE {table_name} {column}") if table1 == [] else cursor.execute("ALTER TABLE Person ADD ?", (column, ))
        else:
            cursor.execute(f"ALTER TABLE {table_name} ADD {column}")
        table1.append(column)
    

def gen_data(table_name, *columns):
    a,b = columns
    for i in range(10):
        cursor.execute(f"""INSERT INTO {table_name} ({a}, {b}) VALUES (?, ?);""", (i, i))

def iterate_through_args():
    for i in range(5):
        yield(i, )


def get_all(table_name):
    table = BeautifulTable()
    cursor.execute(f"SELECT * FROM {table_name};")
    result = cursor.fetchall()
    print(result)

    #adding rows to BeautifulTable
    for row in result:
        temp = []
        for value in row:
            temp.append(value)
        table.rows.append(temp)
    
    print(table)
    


if __name__ == "__main__":
    create_table("Person","Age", "Fav_Num")
    gen_data("Person", "Age", "Fav_Num")
    get_all("Person")
    print("It all went smoothly")





