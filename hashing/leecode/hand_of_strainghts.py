'''
846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

'''

# approach- place all number in heap, pick the smallest one, chech W consecutive number can be formed by it or not and 
# then pick next smallest use instances are left in hash map and create consecutive subsequnce 

from collections import defaultdict
from heapq import heappop, heapify
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        if l % W:
            return False
        if W == 1:
            return True
        
	# first we count the numbers
        cnt = defaultdict(int)
        for i in hand:
            cnt[i] += 1
	# then we build the minimum heap
        heapify(hand)
				
        for i in range(l // W):    
	    # first we find the starting number of current group
            start = heappop(hand)  
            while cnt[start] == 0:  # if the number is no loner available
                start = heappop(hand)  # we pop again
            
	    # Now we find the all other numbers in the group
            for i in range(W):  
                cnt[start] -= 1  # decrease its counts
                if cnt[start] < 0:  # the number is not available
                    return False
                start += 1
        return True