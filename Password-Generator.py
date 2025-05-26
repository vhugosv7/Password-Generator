# import modules
import string
import random

#  THIS CODE VERSION WORKS!

# store all characters lists in dictionaries

collection = {"1": list(string.ascii_lowercase),
              "2": list(string.ascii_uppercase),
              "3": list(string.digits),
              "4": list(string.punctuation),
              ",": []}


#  Generating the password according to
#  the user's selections
def pwd_generator(pwd_length, user):
    list_to_choose = []
    for a in user:
        try:
            #  Combining the user's list selected.
            list_to_choose = collection[a] + list_to_choose
        except (KeyError) as key:
            print(f"{key} is not a  valid option.")
        except IndexError:
            print("Invalid option")

    user_pwd = []
    for pwd in range(pwd_length):
        #  Choosing a random character from the combined list.
        random_item = random.choice(list_to_choose)
        #  Append all the characteres.
        user_pwd.append(random_item)
    #  Displaying password and its length.
    print("Password:\n" + "".join(user_pwd))
    print("Password length:\n" + str(len(user_pwd)), "characters")


pwd_length = int(input("Password length (4-64 characters): "))

while True:
    #  Analyze password length
    try:
        if pwd_length > 64:
            print("Maximum number of characters is 64")
            break

        elif pwd_length < 4:
            print("Minimun number of characters is 4")
            break
        else:
            user = input('''
            1.- Lower case.
            2.- Upper case.
            3.- Numbers.
            4.- Symbols.

            *** Which type of value do you want in your password?: ''')
            pwd_generator(pwd_length, user)
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
