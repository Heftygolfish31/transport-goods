from easygui import *


def login(password):
    access = False
    while access == False:
        locked = passwordbox(msg="Authentication Required", title="Authenticate")
        if locked == password:
            print("Complete")
            access = True
        else:
            access = False

def credit():
    msg = "Enter credentials"
    title = "Credentials"
    fieldNames = ["Name", "Email", "Card Number", "Expration Date", "Security Code"]
    fieldValues = list(multenterbox(msg, title, fieldNames))
    
    global fieldOut
    name, email, card, expire, secure = fieldValues[0:len(fieldValues)]
    fieldOut = [name, email, card, expire, secure]

    print('\n'.join(fieldValues))

# remove for examination
login("test")
credit()
