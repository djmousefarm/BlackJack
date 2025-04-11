
suits = ['spades', 'clubs', 'hearts', 'diamonds']

suit = suits[2]
rank = 'K'
value = 10

print(f"Your card is : {rank} of {suit}")
print(f"Your card value is : {value}")  

suits.append('snakes')


for suit in suits:
    print(suit)