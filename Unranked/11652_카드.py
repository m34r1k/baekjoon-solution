n = int(input())
cards = []

for i in range(n):
    card = int(input())
    if card != cards[n][0]:
        cards.append([card, 0])
    elif card == cards[i][0]:
        cards[i][0] += 1 #[[1, 3], [2, 2]]
cards.sort(key=lambda x: (x[0], x[1]))