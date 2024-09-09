import csv


def read_csv(filename):
    with open(filename, 'r') as uploaded_csv:
        csv_reader = csv.reader(uploaded_csv, delimiter=';')

        for line in csv_reader:
            print(line)


def write_csv(filename):
    with open(filename, 'r') as uploaded_csv:
        csv_reader = csv.reader(uploaded_csv, delimiter=';')

        with open('newusers.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)


def main():
    filename = "usersdata.csv"
    user_input = input(
        'Please select an action for the CSV file:\n\n\nr - Read file\nw - Create new CSV file\n\n')

    if user_input.lower() in ['r', 'w']:
        if user_input.lower() == 'r':
            read_csv(filename)
        if user_input.lower() == 'w':
            write_csv(filename)
    else:
        print('Please select a valid input.')
        main()


main()
