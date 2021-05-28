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
        flocIndex = indexbox(msg="Enter your location", title="Location", choices=places)
        exitProgram(flocIndex)
        floc = places[flocIndex]

        tlocIndex = indexbox(msg="Enter the destination", title="Destination", choices=places)
        exitProgram(tlocIndex)
        tloc = places[tlocIndex]

        mileage0 = [ 0, 20, 33, 40]
        mileage1 = [20,  0, 15, 24]
        mileage2 = [33, 15,  0,  9]
        mileage3 = [40, 24,  9,  0]
        mileages = [mileage0, mileage1, mileage2, mileage3]

        mileage = mileages[flocIndex][tlocIndex]

        if mileage == 0:
            same = msgbox(msg="You have entered the same place twice! There is nowhere to travel to.")
            exitProgram(same)


        msg = f"Your parcel will be:\n\n\nSent from {floc}\n\nTo {tloc}.\n\n\nYour parcel is travelling {str(mileage)} miles.\n\n\n\t\t\t\tAre these correct?"
        title = "Parcel transfer"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        
        if accurate == False:
            continue
        else:
            wherenwhen(floc, tloc, mileage)

def wherenwhen(floc, tloc, mileage):
    msg = "Choose your parcel size:"
    title  = "Parcel Size"
    sizes = ["Small", "Medium", "Large"]
    magIndex = indexbox(msg, title, sizes)
    exitProgram(magIndex)
    magnitude = sizes[magIndex]


    msg = "When do you want your parcel delivered?"
    title = "Delivery Time"
    when = ["Next day before 1pm", "Next day", "Normal delivery"]
    timeIndex = indexbox(msg, title, when)
    exitProgram(timeIndex)
    time = when[timeIndex]

    prices0 = ["20.70", "17.70", "13.14"]
    prices1 = ["24.18", "21.12", "16.62"]
    prices2 = ["30.96", "27.96", "23.40"]
    prices = [prices0, prices1, prices2]

    price = prices[magIndex][timeIndex]


    msg = f"Your parcel is:\n\n\nIt's size type is: {str(magnitude)}\n\nIt will arrive: {time}\n\nThe price will be: £{price}\n\n\n\t\t\t\tAre these correct?"
    title = "Parcel transfer"
    choice = ["Yes", "No"]
    accurate = boolbox(msg, title, choice)


    if accurate == False:
        wherenwhen(floc, tloc, mileage)
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
                \n\t\t\t\t{fieldOut[3]}\n\t\t\t\t{fieldOut[4]}\n\n\tSent from:\t\t\t{floc}\n\tTo:\t\t\t{tloc}\n\tDistance:\t\t\t{mileage} miles\
                \n\n\tSize:\t\t\t{magnitude}\n\tDelivery time:\t\t\t{time}\n\tPrice:\t\t\t£{str(price)}\n\n\n\t\t\tAre these credit details correct?"
        title = "Invoice"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        
        if accurate == False:
            credit(floc, tloc, mileage, magnitude, time, price)
        else:
            quit()
        

# RUN FUNCS #

# remove for examination
login("test")
delivery()

