'''Given a list of numbers, determine when the best time is to buy and sell a stock '''

def when_to_buy(stock_prices):
    if len(stock_prices) == 0:
        return 0

    if len(stock_prices) == 1:
        return stock_prices[0]

    price_to_buy = stock_prices[0]
    profit = 0

    for i in stock_prices:
        if i < price_to_buy:
            price_to_buy = i

        profit = max(profit, i - price_to_buy)

    return profit

# print(when_to_buy([23,12,11,10]))


def products(lst):
    output = []
    product = 1

    for i in lst:
        output.append(product)
        product *= i
    
    product = 1

    for i, num in enumerate(lst[::-1]):
        output[len(lst) -1 -i] *= product
        product *= num
    
    return output

print(products([1,2,3,4, 5]))

def overlap(r1, r2):
    x_overlap, w_overlap  = calc_overlap(r1['x'], r1['w'], r2['x'], r2['w'])
    y_overlap, h_overlap  = calc_overlap(r1['y'], r1['h'], r2['y'], r2['h'])

    if not w_overlap or not h_overlap:
        return None
    else:
        return True


def calc_overlap(coord1, dim1, coord2, dim2):
    greater = max(coord1, coord2)
    lower = min(coord1+dim1, coord2+dim2)

    if greater >= lower:
        return (None, None)

    overlap = lower - greater

    return (greater, overlap)