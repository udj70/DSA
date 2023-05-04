# task- Given an array of of integer from 1 to n in which one elemnt is missing and one is repeating find those number
# approach 1- store count of number in hashmap and find check for repeating and missing, TC- O(N) SC- O(N)
# approach 2- calculate sum(array)-sum(1st n numbers)= x-y(here x and y are missing and repeating number)
#                       sum(square of array el)- sum(squares of 1st n numbers)= x^2- y^2 
#             solve these equation and get value of x and y , TC- O(N), SC-O(1), can created create integer overflow coz calculating square

def repeating_and_missing(arr):
    n=len(arr)
    sum_arr=sum(arr)
    sum_1st_n_num= (n*(n+1))//2
    sum_of_squares_arr=sum([a*a for a in arr])
    sum_square_1st_n_num = (n*(n+1)*(2*n+1))//6
    equation1=sum_arr-sum_1st_n_num
    equation2=(sum_of_squares_arr-sum_square_1st_n_num)//equation1
    value1=(equation1+equation2)//2
    value2=equation2-value1
    print(value1,value2)
arr=[1,2,3,4,4]
repeating_and_missing(arr)

#approach 3- XOR method,
# refer striver fo this
# refer pepcoding
# solution in bit manipulation folder