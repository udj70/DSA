# task- given stocks prices,  we are allowed to do at most two transactions , (replace 2 with k for k trasaction)

# approach 1- recursive
def max_profit(stocks,i,buy,k):
    # base case
    # here k is number of transaction
    if k==0:
        return 0
    if i==len(stocks):
        return 0
    
    # if buy allowed, either buy or not buy
    if buy:
        return max(-stocks[i] + max_profit(stocks,i+1,0,k), 0 + max_profit(stocks,i+1,1,k))
    # if sell allowed , then either sell or not sell 
    else:
        return max(stocks[i] + max_profit(stocks,i+1,1,k-1), 0 + max_profit(stocks, i+1,0,k))

stocks = [10,15,17,20,16,18,22]
print(max_profit(stocks, 0, 1,2))

# recursive + memo

def max_profit_memo(stocks,i,buy,k,dp):
     # base case
    # here k is number of transaction
    if k==0:
        return 0
    if i==len(stocks):
        return 0

    if dp[len(stocks)-1][buy][k]!=-1:
        return dp[i][buy][k]
    
    # if buy allowed, either buy or not buy
    if buy:
        dp[i][buy][k] = max(-stocks[i] + max_profit_memo(stocks,i+1,0,k,dp), 0 + max_profit_memo(stocks,i+1,1,k,dp))
    # if sell allowed , then either sell or not sell 
    else:
        dp[i][buy][k] = max(stocks[i] + max_profit_memo(stocks,i+1,1,k-1,dp), 0 + max_profit_memo(stocks, i+1,0,k,dp))

    return dp[i][buy][k]
stocks = [10,15,17,20,16,18,22]
dp=[[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(stocks))]
print(max_profit_memo(stocks, 0, 1,2,dp))

# tabulation

def max_profit_tab(stocks):
    dp=[[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(stocks)+1)]

    # base is zeros, already intialised with zero

    # right changing variable in reverse order

    for i in range(len(stocks)-1,-1,-1):
        for buy in range(2):
            # because k==0 is 0, so no need to compute it
            for k in range(1,3):
                # if buy allowed, either buy or not buy
                if buy:
                    dp[i][buy][k] = max(-stocks[i] + dp[i+1][0][k], 0 + dp[i+1][1][k])
                # if sell allowed , then either sell or not sell 
                else:
                    dp[i][buy][k] = max(stocks[i] + dp[i+1][1][k-1], 0 + dp[i+1][0][k])

    return dp[0][1][2]
stocks = [10,15,17,20,16,18,22]

print(max_profit_tab(stocks))

# space opt

def max_profit_opt(stocks):
    curr=[[0 for _ in range(3)] for _ in range(2)]
    next=[[0 for _ in range(3)] for _ in range(2)]

    # base is zeros, already intialised with zero

    # right changing variable in reverse order

    for i in range(len(stocks)-1,-1,-1):
        for buy in range(2):
            # because k==0 is 0, so no need to compute it
            for k in range(1,3):
                # if buy allowed, either buy or not buy
                if buy:
                    curr[buy][k] = max(-stocks[i] + next[0][k], 0 + next[1][k])
                # if sell allowed , then either sell or not sell 
                else:
                    curr[buy][k] = max(stocks[i] + next[1][k-1], 0 + next[0][k])
        next=curr[:]
    return next[1][2]
stocks = [10,15,17,20,16,18,22]
print(max_profit_opt(stocks))


# another optimised approach recursive-
def max_profit_best(stocks,i,transaction,k):
    if i == len(stocks) or transaction == 2*k:
        return 0
    # buy
    if transaction % 2==0:
        return max(-stocks[i]+max_profit_best(stocks,i+1,transaction+1,k), 0 + max_profit_best(stocks,i+1,transaction,k))
    else:
        return max(stocks[i]+max_profit_best(stocks,i+1,transaction+1,k), 0 + max_profit_best(stocks,i+1,transaction,k))

stocks = [10,15,17,20,16,18,22]
print(max_profit_best(stocks,0,0,2))

# another optimised approach recursive+memo-
def max_profit_best_memo(stocks,i,transaction,k,dp):
    if i == len(stocks) or transaction == 2*k:
        return 0
    if dp[i][transaction]!=-1:
        return dp[i][transaction]

    # buy
    if transaction % 2==0:
        dp[i][transaction] = max(-stocks[i]+max_profit_best_memo(stocks,i+1,transaction+1,k,dp), 0 + max_profit_best_memo(stocks,i+1,transaction,k,dp))
    #sell
    else:
        dp[i][transaction] = max(stocks[i]+max_profit_best_memo(stocks,i+1,transaction+1,k,dp), 0 + max_profit_best_memo(stocks,i+1,transaction,k,dp))
    return dp[i][transaction]
stocks = [10,15,17,20,16,18,22]
k=2
dp = [[-1 for _ in range(2*k+1)] for _ in range(len(stocks))]
print(max_profit_best_memo(stocks,0,0,k,dp))

# right tabulation
# space optimise it