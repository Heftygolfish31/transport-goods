# IMPORT #
from easygui import *

def exitProgram(window):
    if window == None:
        quit()

def login(password):
    # Have you inputed the right password? (as specified in the function parameter)
    access = False
    while access == False:
        locked = passwordbox(msg="Authentication Required", title="Authenticate")
        # If the input from the msg is equal to the correct password, proceed.
        if locked == password:
            access = True
        # Else stop.
        else:
            exitProgram(locked)

def delivery():
    
    places = ["Cardiff", "Bridgend", "Port Talbort", "Swansea"]

    while True:
        floc = choicebox(msg="Enter your location", title="Location", choices=places)
        exitProgram(floc)
        tloc = choicebox(msg="Enter the destination", title="Destination", choices=places)
        exitProgram(tloc)

        if floc == tloc:
            msg1 = msgbox(msg="You have entered the same place twice! There is nowhere to travel to.")
            exitProgram(msg1)
        elif floc == places[0] and tloc == places[1] or floc == places[1] and tloc == places[0]:
            mileage = 20
        elif floc == places[0] and tloc == places[2] or floc == places[2] and tloc == places[0]:
            mileage = 33
        elif floc == places[0] and tloc == places[3] or floc == places[3] and tloc == places[0]:
            mileage = 40
        elif floc == places[1] and tloc == places[2] or floc == places[2] and tloc == places[1]:
            mileage = 15
        elif floc == places[1] and tloc == places[3] or floc == places[3] and tloc == places[1]:
            mileage = 24
        elif floc == places[2] and tloc == places[3] or floc == places[3] and tloc == places[2]:
            mileage = 9
        else:
            msgbox("Congrats you broke it... dumbass")
        
        msg = f"Your parcel will be:\n\n\nSent from {floc}\n\nTo {tloc}.\n\n\nYour parcel is travelling {str(mileage)} miles.\n\n\n\t\t\t\tAre these correct?"
        title = "Parcel transfer"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        
        if accurate == 0:
            delivery()
        else:
            wherenwhen(floc, tloc, mileage)

def wherenwhen(floc, tloc, mileage):
    msg = "Choose your parcel size:"
    title  = "Parcel Size"
    sizes = ["Small", "Medium", "Large"]
    magnitude = buttonbox(msg, title, sizes)
    exitProgram(magnitude)

    msg = "When do you want your parcel delivered?"
    title = "Delivery Time"
    when = ["Next day before 1pm", "Next day", "Normal delivery"]
    time = buttonbox(msg, title, when)
    exitProgram(time)

    if magnitude == sizes[0] and time == when[0]:
        price = "20.70"
    elif magnitude == sizes[1] and time == when[0]:
        price = "24.18"
    elif magnitude == sizes[2] and time == when[0]:
        price = "30.96"
    elif magnitude == sizes[0] and time == when[1]:
        price = "17.70"
    elif magnitude == sizes[1] and time == when[1]:
        price = "21.12"
    elif magnitude == sizes[2] and time == when[1]:
        price = "27.96"
    elif magnitude == sizes[0] and time == when[2]:
        price = "13.14"
    elif magnitude == sizes[1] and time == when[2]:
        price = "16.62"
    elif magnitude == sizes[2] and time == when[2]:
        price = "23.40"

    msg = f"Your parcel is:\n\n\nIt's size type is: {str(magnitude)}\n\nThe price will be: £{price}\n\n\n\t\t\t\tAre these correct?"
    title = "Parcel transfer"
    choice = ["Yes", "No"]
    accurate = boolbox(msg, title, choice)

    if accurate == 0:
        wherenwhen()
    else:
        credit(floc, tloc, mileage, magnitude, time, price)

# Handles card details and loops if you don't input the right details.
def credit(floc, tloc, mileage, magnitude, time, price):
    while True:
        # IDEA: is having both variables named 'msg' a bad idea?
        msg = "Enter credentials"
        title = "Credentials"
        fieldNames = ["Name", "Email", "Card Number", "Expration Date", "Security Code"]
        fieldValues = list(multenterbox(msg, title, fieldNames))
        exitProgram(fieldValues)

        # Handels inputed values into discriptive variables.
        name, email, card, expire, secure = fieldValues[0:5]
        fieldOut = [name, email, card, expire, secure]

        i = 0
        error = False
        for x in fieldOut:
            if x == "":
                msgbox(f"{fieldNames[i]} is a required field")
                error = True
            else:
                print(f"{fieldNames[i]} OKAY")

            i += 1

        if error == False:
            invoice(fieldOut, floc, tloc, mileage, magnitude, time, price)

def invoice(fieldOut, floc, tloc, mileage, magnitude, time, price):
    while True:
        # Actual invoice display
        # IDEA: link to .txt file if specs allow it.
        msg = f"INVOICE:\n\n\tBilled to:\t\t\t{fieldOut[0]}\n\tContact information:\t\t\t{fieldOut[1]}\n\tCard details:\t\t\t{fieldOut[2]}\
                \n\t\t\t{fieldOut[3]}\n\t\t\t{fieldOut[4]}\n\n\tSent from:\t\t\t{floc}\n\tTo:\t\t\t{tloc}\n\tDistance:\t\t\t{mileage} miles\
                \n\n\tSize:\t\t\t{magnitude}\n\tDelivery time:\t\t\t{time}\n\tPrice:\t\t\t£{str(price)}\n\n\n\t\t\tAre these credit details correct?"
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
    delivery()
# CATCHING EXCEPTIONS #
# TypeError to catch canceling an action with inputs
except TypeError:
    # Non essential - DEBUG
    print("Operation Cancled")

