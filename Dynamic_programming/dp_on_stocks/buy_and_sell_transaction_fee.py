# task- Given stocks prices, find max profit with T fee on each trasaction
# approach 1- recursive- same as dp on stocks 2, just subtract T fee on selling

def max_profit(stocks,i,buy,fee):
    # base case
    if i>=len(stocks):
        return 0
    
    # if buy allowed, either buy or not buy
    if buy:
        return max(-stocks[i] + max_profit(stocks,i+1,0,fee), 0 + max_profit(stocks,i+1,1,fee))
    # if sell allowed , then either sell or not sell 
    else:
        return max(stocks[i] -fee +max_profit(stocks,i+1,1,fee), 0 + max_profit(stocks, i+1,0,fee))
stocks = [10,15,17,20,16,18,22]
fee=3
print(max_profit(stocks, 0, 1,fee))


# optimise it later, simple :)