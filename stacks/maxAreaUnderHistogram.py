def MAH(arr):
  
  left=[-1]*len(arr)
  right=[len(arr)]*len(arr)
  i=len(arr)-1
  stack=[len(arr)]
  while(i>=0):
    if stack[-1]==len(arr):
      right[i]=stack[-1]
      stack.append(i)
    else:
      while(len(stack)>1 and arr[i]<=arr[stack[-1]]):
        stack.pop()
      right[i]=stack[-1]
      stack.append(i) 
    i-=1   
  stack=[-1]
  i=0
  while(i<len(arr)):
    if stack[-1]==-1:
      left[i]=stack[-1]
      stack.append(i)
    else:
      while(len(stack)>1 and arr[i]<=arr[stack[-1]]):
        stack.pop()
      left[i]=stack[-1]
      stack.append(i)
    i+=1    
  print(left,right)  

  # we can build left and right and left stack in single interation
  
  right=[len(arr)]*len(arr)
  left=[-1]*len(arr)

  stack=[len(arr)]
  for index in range(len(arr)-1,-1,-1):
      if stack[-1]==len(arr):
        right[index]=len(arr)
      else:
        while(len(stack)>1 and arr[index]<=arr[stack[-1]]):
          pop_index=stack.pop()
          # this line is only change, and two loops are reduced to one
          # if current current element and poped element is equal, so current index cannot be nexl smaller in left for popindex
          if arr[index]!=arr[pop_index]: # if not equal then update left array and popindex
            left[pop_index]=index

        right[index]=stack[-1]
      stack.append(index)

  print(left,right)


  
  

  width=[]
  for i in range(len(arr)):
    width.append(right[i]-left[i]-1)
  area=[]  
  for i in range(len(arr)):
    area.append(arr[i]*width[i])
  return max(area)  

  
arr=[1,5,1]
print(MAH(arr))  



