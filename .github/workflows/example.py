import random

# Set up the deck of cards
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]

# Function to get the value of a card
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

# Shuffle the deck
random.shuffle(deck)

# Deal initial cards
player_cards = [deck.pop(), deck.pop()]
dealer_cards = [deck.pop(), deck.pop()]

# Calculate scores
player_score = card_value(player_cards[0]) + card_value(player_cards[1])
dealer_score = card_value(dealer_cards[0]) + card_value(dealer_cards[1])

# Print initial hands
print(f"Your cards: {player_cards}, current score: {player_score}")
print(f"Dealer's first card: {dealer_cards[0]}")

# Determine the winner
if player_score == 21 or dealer_score == 21:
    print("Blackjack! You win!")
elif player_score > 21:
    print("Busted! You lose.")
else:
    while dealer_score < 17:
        dealer_cards.append(deck.pop())
        dealer_score += card_value(dealer_cards[-1])
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}")
    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    else:
        print("Dealer wins!")

# Note: Run the program again to shuffle the cards and play another round.
