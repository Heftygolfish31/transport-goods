# IMPORT #
from easygui import *

def login(password):
    # Have you inputed the right password? (as specified in the function parameter)
    access = False
    while access == False:
        locked = passwordbox(msg="Authentication Required", title="Authenticate")
        # If the input from the msg is equal to the correct password, proceed.
        if locked == password:
            print("Complete")
            access = True
        # Else loop again.
        else:
            access = False


# Handles card details and loops if you don't input the right details.
def credit():
    while True:
        # IDEA: is having both variables named 'msg' a bad idea?
        msg = "Enter credentials"
        title = "Credentials"
        fieldNames = ["Name", "Email", "Card Number", "Expration Date", "Security Code"]
        fieldValues = list(multenterbox(msg, title, fieldNames))
        
        # Idea: What the fuqe is this?!
        # Handels inputed values into discriptive variables.
        global fieldOut
        name, email, card, expire, secure = fieldValues[0:5]
        fieldOut = [name, email, card, expire, secure]

        i = 0
        for x in fieldOut:
            if fieldOut[i] == "":
                msgbox(f"{fieldNames[i]} is a required field")
                i += 1
            else:
                i += 1

        # Non essential - DEBUG
        print('\n'.join(fieldValues))

        # Actual invoice display
        # IDEA: link to .txt file if specs allow it.
        msg = f"INVOICE:\n\nBilled to:\t\t\t{fieldOut[0]}\nContact information:\t\t\t{fieldOut[1]}\nCard number:\t\t\t{fieldOut[2]}\n\t\t\t{fieldOut[3]}\n\t\t\t{fieldOut[4]}"
        title = "Invoice"
        accurate = ynbox(msg, title)
        
        # If details verified by user, proceed.
        if accurate == True:
            break
        # Else loop back again.
        else:
            continue
        

# RUN FUNCS #
# remove for examination
login("test")

try:
    credit()

# CATCHING EXCEPTIONS #
# TypeError to catch canceling an action
except TypeError:
    # Non essential - DEBUG
    print("Operation Cancled")

