#refer pepcoding lectures for reference

# variation 1- one buy and sell allowed. 
# approach - at every day calculate difference between cuurent price minus lowest price in left


#variation 2- any number of buys and sell with no over lapping
# approach  - two pointer, calculate all increasing difference and save it in profit

#variation 3- any number of buys and sells with no overlapping and k fees on each sell
# approach- maintain two states buy_state_price(update if we buy over previous sold_state_price) and
#            sold_state_price(update if we sell over previous buy_state_price) at each day, and return sold_state_price at last




def max_profit(days,fees):
    buy_state_price=-1*days[0]
    sold_state_price=0
    for price in days[1:]:
        new_buy_state_price=0
        if sold_state_price-price>buy_state_price:
            new_buy_state_price=sold_state_price-price
        else:
            new_buy_state_price=buy_state_price

        new_sold_state_price=0
        if buy_state_price+price-fees>sold_state_price:
            new_sold_state_price=buy_state_price+price-fees
        else:
            new_sold_state_price=sold_state_price
        
        sold_state_price=new_sold_state_price
        buy_state_price=new_buy_state_price
    return sold_state_price    

days=[10,15,17,20,16,18,22]
print(max_profit(days,3))

#variation 4- any number of buys and sells with no overlapping buy and sell and one day cooling day in between 
#               i.e next buy came be done after minimum one day gap
# approach -   maintain three states buy_state_price(update if we buy over previous cool_state_price) ,
#            sold_state_price(update if we sell over previous buy_state_price) and cool_state_price(update if old sold state price is more then old cool state) at each day, and return sold_state_price at last

def max_profit_cool(days):
    buy_state_price=-1*days[0]
    sold_state_price=0
    cool_state_price=0
    for price in days[1:]:
        new_buy_state_price=0
        if cool_state_price-price>buy_state_price:
            new_buy_state_price=cool_state_price-price
        else:
            new_buy_state_price=buy_state_price

        new_sold_state_price=0
        if buy_state_price+price>sold_state_price:
            new_sold_state_price=buy_state_price+price
        else:
            new_sold_state_price=sold_state_price
        new_cool_state_price=0
        if sold_state_price>cool_state_price:
            new_cool_state_price=sold_state_price
        else:
            new_cool_state_price=cool_state_price
        sold_state_price=new_sold_state_price
        buy_state_price=new_buy_state_price
        cool_state_price=new_cool_state_price
    return sold_state_price    

days=[10,15,17,20,16,18,22]
print(max_profit_cool(days))

#variation 5- k number of transactions(buy and sells) allowed
# approach - create dp of size (k+1)*(days+1)

def max_profit_dp(days,k):
    dp=[[0 for _ in range(len(days))] for _ in range(k+1)]
    for i in range(k+1):
        for j in range(len(days)):
            #if days is 1 or num of transaction is zero then profit will zero
            if i==0 or j==0:
                dp[i][j]=0
                continue
            mx=dp[i][j-1]
            #profit corresponking to k transactions and j days, max of profits till j-1 days + profit(days[j]-days[j-1]) and k-1 transactions 
            for k in range(j):
                #profit till i-1 transaction for days k
                profit_till_k=dp[i-1][k]
                profit_on_jth_day=days[j]-days[k]
                mx=max(profit_on_jth_day+profit_till_k,mx)
            dp[i][j]=mx
    #print(dp)
    return dp[k][len(days)-1]    
days=[10,20,30]
print(max_profit_dp(days,1))

#alternative approach-- same to above one, one we are saving third loop, by savings some value at each days
#                       TC- O(nk) SC-O(nk)

def max_profit_dp_n2(days,k):
    dp=[[0 for _ in range(len(days))] for _ in range(k+1)]
    for t in range(k+1):
        max_so_far=-float('inf')
        for d in range(len(days)):
            #if days is 1 or num of transaction is zero then profit will zero
            if t==0 or d==0:
                dp[t][d]=0
                max_so_far=max((-1)*days[d]+dp[t-1][d],max_so_far)
                continue
            max_till_today=max(dp[t][d-1],days[d]+max_so_far)
            #profit corresponking to k transactions and j days, max of profits till j-1 days + profit(days[j]-days[j-1]) and k-1 transactions 
            #profit at d day= price[d] + max(-price[x]+dp[t-1][x]) where x=0 to d
            #so we can calculate -price[x]+dp[t-1][x] at every d in max_so_far variable
            # and day d we can directly perform price[d]+max_so_far
           
            #on day d max profit will be
            dp[t][d]=max_till_today

            #update max_so_far for next days
            max_so_far=max((-1)*days[d]+dp[t-1][d],max_so_far)
            # for k in range(j):
            #     #profit till i-1 transaction for days k
            #     profit_till_k=dp[i-1][k]
            #     profit_on_jth_day=days[j]-days[k]
            #     mx=max(profit_on_jth_day+profit_till_k,mx)
            # dp[i][j]=mx
    print(dp)
    return dp[k][len(days)-1]    
days=[10,20,30]
print(max_profit_dp_n2(days,1))


