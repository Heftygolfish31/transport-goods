# IMPORT #
from easygui import *

def exitProgram(window):
    if window == None:
        quit()

def login(password):
    # Have you inputed the right password? (as specified in the function parameter)
    while True:
        locked = passwordbox(msg="Authentication Required", title="Authenticate")
        exitProgram(locked)
        # If the input from the msg is equal to the correct password, proceed.
        if locked == password:
            break

def where():
    while True:
        # Places the parcel can be sent or recieved from.
        places = ["Cardiff", "Bridgend", "Port Talbort", "Swansea"]

        # Where the parcel is coming from
        msg = "Enter your location"
        title = "Location"
        choices = places
        flocIndex = indexbox(msg="Enter your location", title="Location", choices=places)
        exitProgram(flocIndex)
        floc = places[flocIndex]
        # Remove the floc from the places list, but keeping its value to be used in the invoice
        places.remove(floc)

        # Where the parcel is recieved from
        msg = "Enter the destination"
        title = "Destination"
        choices = places
        tlocIndex = indexbox(msg, title, choices)
        exitProgram(tlocIndex)
        tloc = places[tlocIndex]

        # Table to avoid additional modules or unnessecarry elif statments
        mileage0 = [20, 33, 40]
        mileage1 = [20, 15, 24]
        mileage2 = [33, 15,  9]
        mileage3 = [40, 24,  9]
        mileages = [mileage0, mileage1, mileage2, mileage3]
        # Request location in the table
        mileage = mileages[flocIndex][tlocIndex]

        # Check the details are correct
        msg = f"Your parcel will be:\n\n\nSent from {floc}\n\nTo {tloc}.\n\n\nYour parcel is travelling {str(mileage)} miles.\n\n\n\t\t\t\tAre these correct?"
        title = "Parcel transfer"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        exitProgram(accurate)

        if accurate == True:
            break

    return floc, tloc, mileage

def carriage(mileage):
    while True:
        msg = "Choose your parcel size:"
        title  = "Parcel Size"
        sizes = ["Small", "Medium", "Large"]
        magIndex = indexbox(msg, title, sizes)
        exitProgram(magIndex)
        magnitude = sizes[magIndex]


        msg = "When do you want your parcel delivered?"
        title = "Delivery Time"
        when = ["Next day before 1pm", "Next day between 8am and 6pm", "Normal delivery (3 - 5 working days)"]
        timeIndex = indexbox(msg, title, when)
        exitProgram(timeIndex)
        time = when[timeIndex]

        # Table to avoid unnececarry elif statments
        # Strings to avoid trailing 0's
        
        prices0 = [20.70, 17.70, 13.14]
        prices1 = [24.18, 21.12, 16.62]
        prices2 = [30.96, 27.96, 23.40]
        prices = [prices0, prices1, prices2]

        price = prices[magIndex][timeIndex]
        
        # If mileage is over 20, charge 50p for the remaining miles.
        if mileage > 20:
            over = mileage - 20
            price = float(price) + (over * 0.50)
        
        # Keeps the decimal places please.
        price = format(price, '.2f')

        # Check your details are correct
        msg = f"Your parcel is:\n\n\nIt's size type is: {str(magnitude)}\n\nIt will arrive: {time}\n\nThe price will be: £{price}\n\n\n\t\t\t\tAre these correct?"
        title = "Parcel transfer"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)

        if accurate == True:
            break

    return magnitude, time, price

# Handles card details and loops if you don't input the right details.
def credit():
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
                pass
            i += 1

        msg = f"Your credit card details are:\n\nName: {fieldOut[0]}\n\nEmail: {fieldOut[1]}\n\nCard Number: {fieldOut[2]}\n\nExpiration Date: {fieldOut[3]}\n\nSecurity Code: {fieldOut[4]}\n\n\n\t\t\t\tAre these correct?"
        title = "Credit Details"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        exitProgram(accurate)

        if accurate == True:
            # Passing
            break

    return fieldOut

def invoice(fieldOut, floc, tloc, mileage, magnitude, time, price):
    while True:
        # Actual invoice display
        # IDEA: link to .txt file if specs allow it.
        msg = f"INVOICE:\n\n\tBilled to:\t\t\t{fieldOut[0]}\n\tContact information:\t\t\t{fieldOut[1]}\n\tCard details:\t\t\t{fieldOut[2]}\
                \n\t\t\t\t{fieldOut[3]}\n\t\t\t\t{fieldOut[4]}\n\n\tSent from:\t\t\t{floc}\n\tTo:\t\t\t{tloc}\n\tDistance:\t\t\t{mileage} miles\
                \n\n\tSize:\t\t\t{magnitude}\n\tDelivery time:\t\t\t{time}\n\tPrice:\t\t\t£{str(price)}"
        title = "Invoice"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)
        
        if accurate == False:
            credit()
        else:
            break

def goodbye(fieldOut):
    msg = f"Goodbye {fieldOut[0]}. Thank you for shopping with us!"
    title = "Thank you!"
    msgbox(msg, title)
    
# RUN FUNCS #

# remove for examination
login("test")
floc, tloc, mileage = where()
magnitude, time, price = carriage(mileage)
fieldOut = credit()
invoice(fieldOut, floc, tloc, mileage, magnitude, time, price)
goodbye(fieldOut)
