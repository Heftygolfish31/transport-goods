# IMPORT #
from easygui import *

def exitProgram(window):
    if window == None:
        quit()

def noAccess():
    accessMsg = msgbox(msg="Password Incorrect", title="Goodbye!", ok_button="Exit")
    exitProgram(accessMsg)

def login(password):
    tries = 3
    correct = False
    # Have you inputed the right password? (as specified in the function parameter)
    while tries != 0:
        loginInput = passwordbox(msg=f"Authentication Required\nTries left: {tries}", title="Authenticate")
        exitProgram(loginInput)
        
        # If the input from the msg is equal to the correct password, proceed.
        if loginInput == password:
            correct = True
            break
        tries-=1

    return correct


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
        msg = f"""
    PARCEL INFO:

        Sent from:          {floc}.
        Sent to:            {tloc}.
        Distance:           {str(mileage)} miles.

                                
                               Are these correct?
"""
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
        msg = f"""
    PARCEL INFO:

        Size Type:          {str(magnitude)}
        Arrival Time:       {time}
        Price:              £{price}

                               Are these correct?
"""
        title = "Parcel transfer"
        choice = ["Yes", "No"]
        accurate = boolbox(msg, title, choice)

        if accurate == True:
            break

    return magnitude, time, price

# Handles card details and loops if you don't input the right details.
def credit():
    while True:
        forbidden = ['?', '/', '\\', '!', ',', ';', ':', '-', ')', '(', '}', '{', '[', ']', '\'', '"', '.', '>', '<', '^', '%', '#', '~', '@', '£', '$', '*', '_', '+', ' ', 'doi', 'pmid', 'scid', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # IDEA: is having both variables named 'msg' a bad idea?
        msg = "Enter credentials"
        title = "Credentials"
        fieldNames = ["Name", "Email", "Card Number", "Expration Date", "CVV"]
        # DEBUG #
        placeholder = ['S Garrett', "quitesadgeese@gmail.com", '1234 1234 1234 1234', '12/12', '123']
        fieldValues = list(multenterbox(msg, title, fieldNames, placeholder))
        exitProgram(fieldValues)

        # Handels inputed values into discriptive variables.
        
        name, email, card, expire, cvv = fieldValues[0:5]
        fieldOut = [name.title(), email, card, expire, cvv]
        error = True


        i = 0
        for field in fieldOut:
            if field == '':
                msgbox(f"{fieldNames[i]} is a required field", "Error")
                error = True
            i += 1

        errorStr = "Error"
        helpStr = "Contact help team at 'quitesadgeese@gmail.com'"
        cvvSplit = cvv.split('/')

        if len(fieldOut[0]) > 25:
            msgbox(f"{fieldNames[0]} isn't formatted properly.\nIt's is too long!\n{helpStr}.", f"{errorStr}")
        
        elif fieldOut[1].find("@") == -1 or fieldOut[1].find(".") == -1:
            msgbox(f"{fieldNames[1]} isn't formatted properly.\nRemember to use a '@' and a '.'.\n{helpStr}.", f"{errorStr}")
        
        elif len(fieldOut[2]) > 23:
            msgbox(f"{fieldNames[2]} //TEST// is too long!\n{helpStr}.", f"{errorStr}")

            '''or int(cvvSplit[0]) > 31 or int(cvvSplit[1]) > 12'''
        elif fieldOut[3].find("/") == -1 or len(fieldOut[3]) != 5:
            msgbox(f"{fieldNames[3]} isn't formatted properly.\nRemember to use a '/' and a valid date.\n{helpStr}.", f"{errorStr}")
        
        elif not fieldOut[4].isdigit():
            msgbox(f"{fieldNames[4]} isn't formatted properly.\n{fieldNames[4]} can only contain numbers.\n{helpStr}.", f"{errorStr}")
        else:
            error = False

        if error == False:
            msg = f"""
    Card Details:
    
        Name:               {fieldOut[0]}
        Email:              {fieldOut[1]}
        Card Number:        {fieldOut[2]}
        Expiration Date:    {fieldOut[3]}
        CVV:                {fieldOut[4]}

                               Are these correct?
"""
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
        msg = f"""
    INVOICE:

        Billed to:              {fieldOut[0]}
        Contact information:    {fieldOut[1]}
        Card details:           {fieldOut[2]}
                                {fieldOut[3]}
                                {fieldOut[4]}

        Sent from:              {floc}
        To:                     {tloc}
        Distance:               {mileage} miles
        Size:                   {magnitude}
        Delivery time:          {time}
        Price:                  £{str(price)}
"""
        title = "Invoice"
        accurate = msgbox(msg, title)
        exitProgram(accurate)
        break

def goodbye(fieldOut):
    msg = f"Goodbye {fieldOut[0]}. Thank you for shopping with us!"
    title = "Thank you!"
    msgbox(msg, title)
    
# RUN FUNCS #

# remove for examination
correct = login("test")
if correct == True:
    floc, tloc, mileage = where()
    magnitude, time, price = carriage(mileage)
    fieldOut = credit()
    invoice(fieldOut, floc, tloc, mileage, magnitude, time, price)
    goodbye(fieldOut)
else:
    noAccess()
