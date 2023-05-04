# task- given stocks, we can make any number of transactions, with one cool down day
# approach 1- recursive, same as dp on stocks 2, just after selling we will got to index+2, despite of index+1
def max_profit(stocks,i,buy):
    # base case
    if i>=len(stocks):
        return 0
    
    # if buy allowed, either buy or not buy
    if buy:
        return max(-stocks[i] + max_profit(stocks,i+1,0), 0 + max_profit(stocks,i+1,1))
    # if sell allowed , then either sell or not sell 
    else:
        return max(stocks[i] + max_profit(stocks,i+2,1), 0 + max_profit(stocks, i+1,0))
stocks = [10,15,17,20,16,18,22]
print(max_profit(stocks, 0, 1))


# optimise it later, simple :)