N = int(input())

price = int(N * 1.08)
LIST_PRICE = 206
if price < LIST_PRICE:
    print("Yay!")
elif price == LIST_PRICE:
    print("so-so")
else:
    print(":(")
