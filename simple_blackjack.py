import random

# Very simple core of the game which doesn't have too good of a logic yet and probably not the correct rules either. Many things to add on top of styling it a little

# Functions for the game

def draw_card(hand, deck):
    print("")
    print("Drawing you 1 more card!")
    
    hand.append(random.choice(deck))
    check_winner(deck, hand, dealer)


def calculate_winner(hand, dealer):
    if sum(hand) > sum(dealer):
        print("You win!")
    elif sum(hand) < sum(dealer):
        print("You lose, dealer wins!")
    else:
        print("It's a draw!")


def next_round(hand, deck):
    answer = input("If you want to draw another card type `y`, If you want to stand type `n`: ")
    if answer == "y":
        draw_card(hand, deck)
    elif answer == "n":
        calculate_winner(hand, dealer)
    else:
        print("Did not recognize input, try again.")
        next_round(hand, deck)



def game_start(deck):
    for times in range(2):
        hand.append(random.choice(deck))
        dealer.append(random.choice(deck))
    print("You have now both drawn 2 cards!")
    check_winner(deck, hand, dealer)

def check_winner(deck, hand, dealer):
    print("Your hand has", hand, "which equals to", sum(hand))
    print("Dealer has", dealer, "which equals to", sum(dealer))
    if sum(dealer) == 21:
        print("Dealer wins!")
    elif sum(dealer) > 21:
        print("Dealer loses, you win!")
    elif sum(hand) > 21:
        print("You lose!")
    else:
        next_round(hand, deck)



# Welcome message and a short explanation about the simplified rules for this game
print("""Welcome to blackjack! Here are the rules:

        Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
         At the start of each round you are given 2 cards and you can decide wether you stand or pick another card. Pretty simple!""")


# This is the main deck for the game that contains every single card
# They don't have any suites yet

deck = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

hand = []
dealer = []


game_start(deck)
