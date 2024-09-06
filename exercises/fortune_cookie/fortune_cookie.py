import random


def generate_cookie(name):
    messages_dict = {
        1: "You will find a great opportunity soon.",
        2: "You will have a great day today.",
        3: "Get your mind set… confidence will lead you on.",
        4: "A routine task will turn into an enchanting adventure.",
        5: "Experience is the best teacher.",
        6: "You will be happy with your spouse.",
        7: "Expect the unexpected.",
        8: "Stay healthy. Walk a mile.",
        9: "Live this day as if it were your last.",
        10: "Your life will be happy and peaceful.",
    }

    random_num = random.randint(1, 10)
    message = f"\n\n-----------------\n\nHi {name}! 👋 \n\nYour fortune cookie says: '{
        messages_dict[random_num]}'\n\n-----------------\n\n"

    print(message)


user = input('Please enter your name:\n\n')
generate_cookie(user)
