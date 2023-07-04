cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
deck = (cards[y] + ' ' + suits[x] for y in range(len(cards)) for x in range(len(suits)))
deck_iter = iter(deck)
for x in deck_iter:
    print(x)
print('Stop iteration')
