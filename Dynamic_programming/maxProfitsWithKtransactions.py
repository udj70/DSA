#HARD PROBLEM


#TC-O(nk)
#SC-O(n^2)
def maxProfitWithKTransactions(prices, k):
	
    if not len(prices):
        return 0
    profits=[[0 for _ in range(len(prices))] for _ in range(k+1)]
    for t in range(1,k+1):
        maxThusFar=float('-inf')
        for d in range(1,len(prices)):
            maxThusFar=max(maxThusFar,profits[t-1][d-1]-prices[d-1])
            profits[t][d]=max(maxThusFar+prices[d],profits[t][d-1])
    return profits[-1][-1]	

#TC-O(nk)
#Sc-O(n)
def maxProfitWithKTransactionsOptimised(prices,k):
        if not len(prices):
            return 0	
        odd=[0 for _ in range(len(prices))]
        even=[0 for _ in range(len(prices))]
        
        for t in range(1,k+1):
            maxThusFar=float('-inf')
            if t%2==1:
                current=odd
                previous=even
            else:
                current=even
                previous=odd
                
            for d in range(1,len(prices)):
                
                maxThusFar=max(maxThusFar,previous[d-1]-prices[d-1])
                current[d]=max(maxThusFar+prices[d],current[d-1])
        return current[-1]
            
                