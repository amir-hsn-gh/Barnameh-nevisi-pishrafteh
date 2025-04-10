import random

def create_shuffled_deck():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    deck = [f'{rank} {suit}' for suit in suits for rank in ranks]
    
    random.shuffle(deck)
    return deck

def draw_random_card(deck):
    if not deck:
        return None
    return random.choice(deck)

deck = create_shuffled_deck()
random_card = draw_random_card(deck)

print("Karte random:", random_card)