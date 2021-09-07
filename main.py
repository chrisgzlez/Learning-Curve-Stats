# AUTHOR: CHRISTIAN NOVOA GONZALEZ
# STATE OF THE PROGRAM: FUNCTIONAL IN TERMINAL
# RELEASE VERSION: 1.0

from sqlite3 import OperationalError
from Modules import databaseManagement as dM
# cannot use relative imports in the root folder, then you must use absolute

# possible names of programs
vs_names = ("VSCode", "VS", "vscode", "vs")
chrome_names = ("Chrome", "Google", "chrome", "google")
help_names = ("Help", "help", "h", "show_commands")
quit_names = ("Quit", "Exit", "quit", "exit", "Q", "q", "Break", "break")
error_message = """Error
                    Command {app} Not Found
                    To See a list of commands, use show_commands
                """
help_message = f""" These are the allowed commands
    monitor
    show_tables
    quit
    {vs_names} 
    {chrome_names}
    {help_names}
    {quit_names}
    """


def show_commands() -> None:
    print(help_message)


def switch(value: bool) -> bool:
    if value:
        return False
    else:
        return True


def get_app(action: str) -> (dM.DataBase, str):
    while True:
        app = input(f"What program would you like to {action}? ")
        if app in vs_names:
            mark = vs_names
            if mark not in trackers:
                trackers[mark] = check
            return VSCode, mark

        elif app in chrome_names:
            mark = chrome_names
            if mark not in trackers:
                trackers[mark] = check
            return Chrome, mark

        elif app in help_names:
            show_commands()
        else:
            print(error_message)


if __name__ == '__main__':
    # Declare Variables and Initialize Databases
    try:
        VSCode = dM.DataBase("VSCode")
        Chrome = dM.DataBase("Chrome")
        VSCode.create_table()
        Chrome.create_table()
    except OperationalError:
        pass
    finally:
        trackers = {}
        check = True

        while True:
            function = input("What do you want to do?: ")

            if function in quit_names:
                break

            elif function == "monitor":
                program, id_tracker = get_app(function)
                program.monitor(trackers[id_tracker])
                trackers[id_tracker] = switch(trackers[id_tracker])

            elif function == "show_tables":
                program, _ = get_app(function)
                program.show_table()

            elif function in help_names:
                show_commands()

            else:
                print(error_message)
