'''
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

 

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
'''

# approach- maintin a monotonic stack from right of cars array, now curent car will collide with the car in right if
#           either next car speed is less or collision time of next car with its succesor is more than collision time current car with next car
#           think In opposite way now- I will ignore/skip next car 1.) if speed of next car is more or equal to cuurent car
#                                                                  2.) if next car collision time with its succesor is less than current car collisin with next car
#           In both these cases we will pop car from stack
#           Note- in stack we will maintain three values corresponding to car, [car position, car speed, collsion time with its succesor]

class Solution:
    def getCollisionTimes(self, cars):
        stack=[]
        ans=[]
        for c in cars[::-1]:

            # these are the two cases when we not consider next car for collison
            while(stack and (stack[-1][1]>=c[1] or stack[-1][2]<=(stack[-1][0]-c[0])/(c[1]-stack[-1][1]))):
                stack.pop()
            #print(stack)

            # if stack is empty i.e no car in right with which current car will collide
            if not stack:
                ans.append(-1)
                stack.append([c[0],c[1],float('inf')])

            # else calculate collision time with current car on stack.top
            else:
                collideTime=(stack[-1][0]-c[0])/(c[1]-stack[-1][1])
                stack.append([c[0],c[1],collideTime])
                ans.append(collideTime)
        ans.reverse()
        return ans 
             
cars = [[3,4],[5,4],[6,3],[9,1]]
s=Solution()
print(s.getCollisionTimes(cars))