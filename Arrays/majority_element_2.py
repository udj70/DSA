# task- Given array, find majority element those who occurs more than n//3 times
# approach 1- hash map approach
# approach 2- boyce moore algo- here at max two majority element possible, apply same voting approach with 2 count and majority element variable

def majority_element(arr):
    num1=-1
    num2=-1
    count1=0
    count2=0
    n=len(arr)
    for a in arr:
        if a==num1:
            count1+=1
        elif a==num2:
            count2+=1
        elif count1==0:
            count1=1
            num1=a
        elif count2==0:
            count2=1
            num2=a
        else:
            count1-=1
            count2-=1
    count1=0
    count2=0
    for a in arr:
        if a==num1:
            count1+=1
        elif a==num2:
            count2+=1
    ans=[]
    if count1>n//3:
        ans.append(num1)
    if count2>n//3:
        ans.append(num2)
    print(ans)
arr=[1,1,1,2,2,3,3]
majority_element(arr)
