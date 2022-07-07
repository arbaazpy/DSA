# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

def final_prices(prices):
    stack = []
    if prices:
        prices_length = len(prices)
        for index in range(prices_length):
            current_price = prices[index]
            for j in range(index, prices_length):
                if j+1 < prices_length and prices[j+1] <= current_price:
                    current_price = current_price - prices[j+1]
                    break
            stack.append(current_price)
    return stack
    
print()
print(final_prices([8,4,6,2,3]))
print()
print(final_prices([1,2,3,4,5]))
print()
print(final_prices([10,1,1,6]))
print()
print(final_prices([6,8,1,8,1,5,10,10,10]))  # [5,7,0,7,1,5,0,0,10]

