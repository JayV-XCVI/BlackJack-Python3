name = str(input("Enter name here: "))
print("Welcome to the Black Jack table! Please have a seat " + name + ". " + "If you are caught counting cards, you will be dealt with by the House.")

print("There are four seats. Please select a number 1 through 4.")

seat_position = int(input("Please enter a number 1 through 4: "))
def picking_seats(seat_position):
    while seat_position <= 3:
        print("You cannot choose seat number " + str(seat_position) + " because that seat is already taken by another player. Please select another.")
        return picking_seats(seat_position = int(input("Please enter a number 1 through 4: ")))
    if seat_position == 4:
        print("Good choice you may take a seat at seat number " + str(seat_position) + ".")
    else:
        print("You may not choose a number greater than 4.")
        return picking_seats(seat_position=int(input("Please enter a number 1 through 4: ")))
    return print("Now that everyone is situated. Let us proceed.")
picking_seats(seat_position)

from Deck import card_deck
import random

