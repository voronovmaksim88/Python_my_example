# prices = [544, 543, 542, 541, 540, 539, 541, 540, 542, 539, 538, 537]
# prices = [7,1,5,3,6,4]
# prices = [7, 6, 4, 3, 1]
# prices = [2, 2, 5]
# prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
prices = [9, 5, 7, 4, 2, 4, 1, 6, 4]

price_sell = 0
price_buy = -1
min_price_buy = 0
if len(prices) >= 3:
    if prices[0] <= prices[1] <= prices[2]:  # рост
        price_sell = prices[2]
        price_buy = prices[0]
        min_price_buy = prices[0]

    if prices[0] <= prices[1] >= prices[2]:  # гора
        price_buy = prices[0]
        min_price_buy = prices[0]
        price_sell = prices[1]

    if prices[0] >= prices[1] <= prices[2]:  # яма
        price_buy = prices[1]
        price_sell = prices[2]
        min_price_buy = prices[1]

profit = 0

if len(prices) == 2:
    if prices[1] > prices[0]:
        profit = prices[1] - prices[0]
else:
    for i in range(0, len(prices) - 2):
        if prices[i] <= prices[i + 1] <= prices[i + 2]:
            print("вверх", end='  ')
            if prices[i + 2] - min_price_buy > profit:
                price_buy = min_price_buy
            if prices[i + 2] - price_buy > profit:
                price_sell = prices[i + 2]

        if prices[i] <= prices[i + 1] >= prices[i + 2]:
            print("гора ", end='  ')
            if prices[i + 1] - prices[i] > profit:
                price_buy = prices[i]
                price_sell = prices[i + 1]

        if prices[i] >= prices[i + 1] <= prices[i + 2]:
            print("яма  ", end='  ')
            if price_buy == -1:  # ещё не определена цена покупки
                price_buy = prices[i + 1]
                min_price_buy = prices[i + 1]
            if prices[i + 1] < min_price_buy:
                min_price_buy = prices[i + 1]
            if prices[i + 2] - price_buy > profit:
                price_sell = prices[i + 2]
            if prices[i + 2] - min_price_buy > profit:
                price_buy = min_price_buy
                price_sell = prices[i + 2]

        if prices[i] >= prices[i + 1] >= prices[i + 2]:
            print("вниз ", end='  ')

        if price_buy != -1:
            profit = price_sell - price_buy
        print(prices[i], prices[i + 1], prices[i + 2], end='  ')
        print("buy", price_buy, end='  ')
        print("sell", price_sell, end='  ')
        print("min_buy", min_price_buy, end='  ')
        print("profit", profit)
