from easygui import *
import random

def HeadOrTail():
    # Initializing details
    heads = "headPic.png"
    tails = "tailPic.png"
    title = "HeadOrTail"
    button_list = ["Again", "End"]
    text = ""

    # Let Heads be 0 and Tails be 1
    randindex = random.randint(0, 2) # Generates a random choices

    if randindex == 0: # Result is head

        outbox = buttonbox(text, title, image = heads, choices = button_list)


    else: # Result is tail
        outbox = buttonbox(text, title, image = tails, choices = button_list)


    # If user decides for another run
    if(outbox == "Again"):
        HeadOrTail()
    else:
        print("Goodbye:)")

# Main function starts here
HeadOrTail() # Calling function once
