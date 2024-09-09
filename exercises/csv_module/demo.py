import sys
from parse_csv import *


def main():
    filename = "usersdata.csv"

    user_input = input(
        '\n\n******************\n\nPlease select an action:\n\n\nL - List all users\nF - Find user by username\nC - Create new user\n\n')

    while user_input.lower() not in ['l', 'f', 'c']:
        print('\n\nPlease select a valid input.')
        return main()
    else:
        if user_input.lower() == 'l':
            UserData.get_all_users(filename)
        elif user_input.lower() == 'f':
            username_input = input('\n\nPlease enter username:\n\n')
            UserData.get_user_by_username(filename, username_input)
        elif user_input.lower() == 'c':
            NewUser = UserData(
                UserData.id_validator(filename),
                input('Username: '),
                UserData.email_validator(),
                input('First name: '),
                input('Last name: '),
            )
            
            NewUser.add_new_user(filename)

    sys.exit("\n\nEnd~ 👋\n\n")


if __name__ == "__main__":
    main()
