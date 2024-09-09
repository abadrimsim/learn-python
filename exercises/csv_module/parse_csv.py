import csv
import re


class UserData:
    def __init__(self, id, username, email, first_name, last_name):
        self.id = id
        self.username = username
        self.email = email
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    def get_all_users(filename):
        with open(filename, 'r') as uploaded_csv:
            csv_reader = csv.DictReader(uploaded_csv, delimiter=';')

            print("\n\nHere's a complete list of all the users:\n")

            for line in csv_reader:
                print(line)

    def get_user_by_username(filename, username):
        with open(filename, 'r') as uploaded_csv:
            csv_reader = csv.DictReader(uploaded_csv, delimiter=';')

            found_user = list(filter(
                lambda user: user['username'] == username, csv_reader))

            if (len(found_user) == 0):
                print(f'\n\nNo user found for {username}.')
            else:
                print("\n\nFound user:\n")

                for user in found_user:
                    print('Data: ', user)

    def add_new_user(self, filename):
        with open(filename, 'a', newline='') as uploaded_csv:
            fieldnames = ['id', 'username', 'email', 'first_name', 'last_name']
            csv_writer = csv.DictWriter(
                uploaded_csv, fieldnames=fieldnames, delimiter=';')

            csv_writer.writerow({
                'id': self.id,
                'username': self.username,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name
            })

        with open(filename, 'r') as uploaded_csv:
            csv_reader = csv.DictReader(uploaded_csv, delimiter=';')

            print("\n\nSuccessfully added new user!\n")

            for line in csv_reader:
                print(line)
                
    def id_validator(filename):        
        def id_exists(user_id):
            with open(filename, 'r') as uploaded_csv:
                csv_reader = csv.DictReader(uploaded_csv, delimiter=';')
                return any(item['id'] == user_id for item in csv_reader)

        user_id = input('\n\nID: ')

        while id_exists(user_id):
            print('ID already exists! Please enter a new ID.\n')
            user_id = input('ID: ')

        return user_id

    def email_validator():
        email_input = input('Email: ')

        def is_valid_email(email):
            is_valid = True if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) else False
            return is_valid

        while not is_valid_email(email_input):
            print('Email is not valid!\n')
            email_input = input('Email: ')
        else:
            return email_input
