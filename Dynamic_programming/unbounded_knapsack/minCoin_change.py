# minimum coins required for given change

# approach 1- recursive

from sympy import Float


def minCoins(coins,i,target):
    if i==0:
        if target%coins[i]==0:
            return target//coins[i]
        else:
            return float('inf')

    if coins[i]<=target:
        return min(1 + minCoins(coins,i,target-coins[i]), 0 + minCoins(coins,i-1,target))
    else:
        return 0 + minCoins(coins,i-1,target)

coins=[1,3,5] 
print(minCoins(coins,len(coins)-1,7))


# other way- old code
# m is size of coins array (number of  
# different coins) 
def minCoins(coins, m, V): 
      
    # table[i] will be storing the minimum  
    # number of coins required for i value.  
    # So table[V] will have result 
    table = [0 for i in range(V + 1)] 
  
    # Base case (If given value V is 0) 
    table[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, V + 1): 
        table[i] = float('inf')
        
    # Compute minimum coins required  
    # for all values from 1 to V 
    for i in range(1, V + 1): 
          
        # Go through all coins smaller than i 
        for j in range(m): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != float('inf') and 
                    sub_res + 1 < table[i]): 
                    table[i] = sub_res + 1
    return table[V] 
coins = [1,3,5] 
m = len(coins) 
V = 7
print("Minimum coins required is ",  minCoins(coins, m, V))   

# greedy way- Not correct
# o(n) Solution # it will fail for few cases, so incorrect (case [9,6,5,1], target-11)

def minCoinsSimple(coins,target):
    coins.sort()
    ans=0
    for i in range(len(coins)-1,-1,-1):
        ans+=target//coins[i]
        target=target%coins[i]
    return ans
print("min coins required simple O(n)",minCoinsSimple([9,6,5,1],11))