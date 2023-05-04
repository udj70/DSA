# task- we are allowed to buy and sell andy number of time
# approach 1- recursive
def max_profit(stocks,i,buy):
    # base case
    if i==len(stocks):
        return 0
    
    # if buy allowed, either buy or not buy
    if buy:
        return max(-stocks[i] + max_profit(stocks,i+1,0), 0 + max_profit(stocks,i+1,1))
    # if sell allowed , then either sell or not sell 
    else:
        return max(stocks[i] + max_profit(stocks,i+1,1), 0 + max_profit(stocks, i+1,0))

stocks = [10,15,17,20,16,18,22]
print(max_profit(stocks, 0, 1))

# recursive + memo

def max_profit_memo(stocks,i,buy,dp):
    # base case
    if i==len(stocks):
        return 0
    if dp[i][buy] !=-1:
        return dp[i][buy]
    # if buy allowed, either buy or not buy
    if buy:
        dp[i][buy] = max(-stocks[i] + max_profit_memo(stocks,i+1,0,dp), 0 + max_profit_memo(stocks,i+1,1,dp))
    # if sell allowed , then either sell or not sell 
    else:
        dp[i][buy] = max(stocks[i] + max_profit_memo(stocks,i+1,1,dp), 0 + max_profit_memo(stocks, i+1,0,dp))
    return dp[i][buy]
stocks = [10,15,17,20,16,18,22]
dp = [[-1 for _ in range(2)] for _ in range(len(stocks))]
print(max_profit_memo(stocks, 0, 1, dp))


# tabulation

def max_profit_tab(stocks):
    dp = [[0 for _ in range(2)] for _ in range(len(stocks)+1)]
    
    for i in range(len(stocks)-1,-1,-1):
       
            dp[i][1] = max(-stocks[i] + dp[i+1][0], 0 + dp[i+1][1])
        # if sell allowed , then either sell or not sell 
        
            dp[i][0] = max(stocks[i] + dp[i+1][1], 0 + dp[i+1][0])
    return dp[0][1]

stocks = [10,15,17,20,16,18,22]

print(max_profit_tab(stocks))

# space optimisation

def max_profit_opt(stocks):
    next = [0 for _ in range(2)]
    curr = [0 for _ in range(2)]
    
    for i in range(len(stocks)-1,-1,-1):
       
            curr[1] = max(-stocks[i] + next[0], 0 + next[1])
        # if sell allowed , then either sell or not sell 
        
            curr[0] = max(stocks[i] + next[1], 0 + next[0])

            next=curr[:]
    return next[1]
stocks = [10,15,17,20,16,18,22]

print(max_profit_opt(stocks))