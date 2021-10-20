from Deck import card_deck


import random
player_hand = []
dealer_hand = []
wager = 0
cash_available = 5000
updated_deck = card_deck[:]
x = random.choice(card_deck)
y = random.choice(updated_deck)
dealer_card1 = random.choice(updated_deck)
dealer_card2 = random.choice(updated_deck)
hit_card = random.choice(updated_deck)
hit_or_stay = ""
card = []
player_card_values = []
dealer_card_values = []

def calc_player_card_values(player_hand):
    for card in player_hand:
        if card[-1] == "Ace":
            one_or_11 = int(input("Would you like the value of the Ace to be 1 or 11? "))
            while one_or_11 != 1 and one_or_11 != 11:
                print("Please enter either 1 or 11.")
                one_or_11 = int(input("Would you like the value of the Ace to be 1 or 11? "))
            if one_or_11 == 1:
                player_card_values.append(1)
            elif one_or_11 == 11:
                player_card_values.append(11)
        if card[-1] != "Ace":
            card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
            card_value = card_values.get(card[-1])
            player_card_values.append(card_value)
    filter(None, player_card_values)
    return player_card_values

def calc_dealer_card_values(dealer_hand):
    for card in dealer_hand:
        if card[-1] != "Ace":
            card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
            card[-1] = card_values[card[-1]]
            dealer_card_values.append(card[-1])
        if card[-1] == "Ace":
            if sum(dealer_card_values) <= 10:
                dealer_card_values.append(11)
            else:
                dealer_card_values.append(1)
    filter(None, dealer_card_values)
    return dealer_card_values



def deal_card(card):
    for card in updated_deck:
        if card == x:
            updated_deck.remove(card)
            player_hand.append(card)
            print("Card dealt is: " + str(x))
    return "Player's hand is: " + str(player_hand)

def deal_again(card):
    for card in updated_deck:
        if card == y:
            updated_deck.remove(card)
            player_hand.append(card)
            print("Card dealt is: " + str(y))
    return "Player's new hand is: " + str(player_hand)

# After cards are dealt initially.

def hit(hit_card):
    for card in updated_deck:
        if card == hit_card:
            updated_deck.remove(hit_card)
            player_hand.append(hit_card)
            print("The card " + str(hit_card) + " was dealt to you.")
            print("Player's new hand is: " + str(player_hand))
            break


# Hit or Stay Option
def hit_or_stay_fxn(hit_or_stay, hit_card):
    hit_or_stay = str(input("Hit or stay?: "))
    while hit_or_stay.lower() != "hit" and hit_or_stay.lower() != "stay":
        print("Let's try this again.")
        hit_or_stay = str(input("Hit or stay?: "))
    while hit_or_stay.lower() == "hit":
        hit_card = random.choice(updated_deck)
        hit(hit_card)
        hit_or_stay = str(input("Hit or stay?: "))
        if hit_or_stay.lower() == "hit":
            continue
        else:
            break
    if hit_or_stay.lower() == "stay":
        print("You have chosen to stay.")
    while hit_or_stay.lower() != "hit" and hit_or_stay.lower() != "stay":
        print("All right, one more time.")
        return hit_or_stay_fxn(hit_or_stay, hit_card)

def start_game(card, wager, cash_available):
    start_game = str(input("Would you like to start the game? Please enter yes or no: "))
    while start_game.lower() == "yes":
        wager = int(input("How many dollars would you like to wager for this round? Enter a number between 1 and " + str(cash_available) + ": "))
        if wager > cash_available:
            print("Error. You cannot wager more than your cash available. Let's try again.")
            continue
        print("Good bet. Let's begin.")
        deal_card(x)
        deal_again(y)
        print("Player's hand is currently: " + str(player_hand))
        print(hit_or_stay_fxn(hit_or_stay, hit_card))
        print("Player's Hand is: " + str(player_hand))
        print("The value of your hand is: ")
        calc_player_card_values(player_hand)
        print(sum(player_card_values))
        if sum(player_card_values) > 21:
            print("Player --> BUST. You have lost your wager for this round.")
            cash_available -= wager
            print(cash_available)
            replay = str(input("Play again? Please enter either yes or no: "))
            if replay.lower() == "yes":
                print("LET'S DO THIS!!! Press Ctrl + Shift + R")
            elif replay.lower() == "no":
                print("Very well. Please leave the House.")
                print("GAME OVER")
            while replay.lower() != "yes" and replay.lower() != "no":
                print("Please enter either yes or no.")
                replay = str(input("Play again? Please enter either yes or no: "))
        print("Let's see what the dealer's cards are...")
        dealer1(dealer_card1)
        dealer2(dealer_card2)
        print("The value of the Dealer's hand is: ")
        calc_dealer_card_values(dealer_hand)
        print(sum(dealer_card_values))
        if sum(dealer_card_values) > 21:
            print("Dealer --> BUST.")
            if sum(player_card_values) > 21:
                print("Player BUST too. DRAW.")
            elif sum(player_card_values) <= 21:
                cash_available += wager
                print("You have the best hand. Congratulations! You have won " + str(wager) + " for this round. Your cash available is now: " + str(cash_available))
        elif sum(dealer_card_values) <= 21:
            if sum(player_card_values) <= 21:
                if sum(player_card_values) > sum(dealer_card_values):
                    cash_available += wager
                    print("You have the best hand. Congratulations! You have won " +str(wager) + " for this round. Your cash available is now: " + str(cash_available))
                elif sum(player_card_values) < sum(dealer_card_values):
                    cash_available -= wager
                    print("Dealer has the best hand. House wins. We're taking your money - consider yourself lucky that we're not breaking your legs.")
        elif sum(dealer_card_values) == sum(player_card_values):
            print("This Round is a draw.")
        #next_round = str(input("Would you like to play another round? Please enter yes or no: "))
        #while next_round != "yes" and next_round != "no":
            #print("Please enter either yes or no.")
            #next_round = str(input("Would you like to play another round? Please enter yes or no: "))
        #if next_round == "yes":
            #for card in player_hand:
                #updated_deck.append(card)
                #player_hand.remove(card)
            #for card in dealer_hand:
                #updated_deck.append(card)
                #dealer_hand.remove(card)
            #for value in player_card_values:
                #player_card_values.remove(value)
            #for value in dealer_card_values:
                #dealer_card_values.remove(value)
        #continue
        #if next_round == "no":
            #print("GAME OVER.")
        break


def dealer1(card1):
    for card1 in updated_deck:
        if card1 == dealer_card1:
            updated_deck.remove(card1)
            dealer_hand.append(card1)
            print("Dealer's first card is: " + str(dealer_card1))
def dealer2(card2):
    for card2 in updated_deck:
        if card2 == dealer_card2:
            updated_deck.remove(card2)
            dealer_hand.append(card2)
            print("Dealer's second card is: " + str(dealer_card2))
    return "Dealer's hand is: " + str(dealer_hand)

print(start_game(card, wager, cash_available))


#play_again = str(input("Start the game again? Please enter yes or no: "))
#while play_again.lower() == "yes":
    #continue
#if play_again.lower() == "no":
    #print("Game over.")
#while play_again.lower() != "yes" and play_again.lower() != "no":
    #print("Please enter either yes or no. Let's try this again.")
    #play_again = str(input("Start the game again? Please enter yes or no: "))

