from flask import Flask, render_template, request
import string
import random

#  In the program comments, password is referred to as pwd.
# Change the template folder path, according to your path.
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def pwd_main():
    # Store the length of the pwd required by the user.
    pwd_length = ""
    # Store the user selection.
    user_selected = ""
    # List to append the ped characters.
    user_pwd = []
    # List to display the type of the character in the pwd.
    store = []
    # To display the pwd length in the input result
    pwd_num = ""
    #  pwd length as text
    pwd_length_str = ""

    if request.method == "POST":
        pwd_length = int(request.form['length'])
        user_selected = request.form['selected_pwd_type']
        # This is for testing; it could be omitted.
        print(user_selected, "*User selection*")

        # Dictionaries with leters,digits and punctuation signs.
        # "," and  "" are empty to catch it from the user's selection.
        collection = {
            "1": {"name": "lowercase", "chars": list(string.ascii_lowercase)},
            "2": {"name": "uppercase", "chars": list(string.ascii_uppercase)},
            "3": {"name": "digits",    "chars": list(string.digits)},
            "4": {"name": "symbols",   "chars": list(string.punctuation)},
            ",": {"name": "comma",     "chars": []},
            " ": {"name": "space",     "chars": []}
            }

        list_to_choose = []
        for a in user_selected:
            #  Combining the user's list selected.
            list_to_choose = collection[a]["chars"] + list_to_choose
        for pwd in range(pwd_length):
            #  Choosing a random character from the combined list.
            random_item = random.choice(list_to_choose)
            #  Append the characters choiced.
            user_pwd.append(random_item)
        #  To display password and its length.
        user_pwd = "".join(user_pwd)
        pwd_length_str = f"Password length: {(str(len(user_pwd)))} characters"

        # Type of value in the password.
        low_c = ""
        upp_c = ""
        num_c = ""
        sym_c = ""
        # Checking each password character
        # to see its type.

        for let in user_pwd:
            if let in list(string.ascii_lowercase):
                low_c = "Lower case"
                store.append(low_c)
            elif let in list(string.ascii_uppercase):
                upp_c = "Upper case"
                store.append(upp_c)
            elif let in list(string.digits):
                num_c = "Numbers"
                store.append(num_c)
            elif let in list(string.punctuation):
                sym_c = "Symbols"
                store.append(sym_c)
            else:
                pass
        #  Avoiding repeated types.
        store = list(set(store))
        pwd_num = len(user_pwd)

    return render_template('main.html', user_pwd=user_pwd,
                           pwd_length_str=pwd_length_str, store=store,
                           pwd_num=pwd_num)


if __name__ == '__main__':
    app.run(debug=False)
