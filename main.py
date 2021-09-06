#Create the Classes Programs and Data
from secrets import token_hex

from Modules import databaseManagement as dM
from time import sleep
from random import randint
# cannot use relative imports in the root folder, then you must use absolute

if __name__ == '__main__':
    VSCode = dM.DataBase("VSCode")
    Chrome = dM.DataBase("Chrome")
    VSCode.create_table()
    Chrome.create_table()

    def monitor(*programs: dM.DataBase):
        for program in programs:
            program.start_monitoring()
            sleep(5)
            program.add_data(program.stop_monitoring())
            program.show_table()

    monitor(VSCode, Chrome)