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
        # Else stop.
        elif locked == None:
            quit()


# Handles card details and loops if you don't input the right details.
def credit():
    while True:
        # IDEA: is having both variables named 'msg' a bad idea?
        msg = "Enter credentials"
        title = "Credentials"
        fieldNames = ["Name", "Email", "Card Number", "Expration Date", "Security Code"]
        fieldValues = list(multenterbox(msg, title, fieldNames))
        
        if fieldValues == None:
            quit()

        # Handels inputed values into discriptive variables.
        name, email, card, expire, secure = fieldValues[0:5]
        fieldOut = [name, email, card, expire, secure]

        i = 0
        error = False
        for x in fieldOut:
            if x == "":
                msgbox(f"{fieldNames[i]} is a required field")
                error = True
            #elif len(str(x)) > 
            else:
                print(f"{fieldNames[i]} OKAY")

            i += 1

        if error == False:
            invoice(fieldOut)
        
        # Non essential - DEBUG
        print('\n'.join(fieldValues))

def invoice(fieldOut):
    while True:
        # Actual invoice display
        # IDEA: link to .txt file if specs allow it.
        msg = f"INVOICE:\n\nBilled to:\t\t\t{fieldOut[0]}\nContact information:\t\t\t{fieldOut[1]}\nCard details:\t\t\t{fieldOut[2]}\n\t\t\t{fieldOut[3]}\n\t\t\t{fieldOut[4]}"
        title = "Invoice"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        
        if accurate == 0:
            credit()
        else:
            quit()
        

# RUN FUNCS #

try:
    # remove for examination
    login("test")
    credit()

# CATCHING EXCEPTIONS #
# TypeError to catch canceling an action with inputs
except TypeError:
    # Non essential - DEBUG
    print("Operation Cancled")

