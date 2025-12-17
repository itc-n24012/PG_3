import random

cards = []
for i in range(1,53):
    cards.append(i)

print(cards) #シャッフル前
random.shuffle(cards)
print(cards) #シャッフル後

