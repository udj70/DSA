#task- implement stack as min stack i.e top of stack should contain minimum element
#approach- with extra space O(n) -> create two stack main and supporting stack(it will hold min at top)
#          without extra space O(1) - > make a varible min,while making push operation if new num is less than min then update min but push 2*new_num-min(corrupted num)
 

#approach 1- TC- O(n), SC- O(n)

def push(stack,supporting_stack,element):
    if len(supporting_stack)==0 or element<=supporting_stack[-1]:
        supporting_stack.append(element)
    stack.append(element)
def pop(stack,supporting_stack):
    if supporting_stack[-1]==stack[-1]:
        supporting_stack.pop()
    stack.pop()
def getMin(supporting_stack):
    return supporting_stack[-1]

stack=[]
supporting_stack=[]
push(stack,supporting_stack,3)    
push(stack,supporting_stack,5)    
push(stack,supporting_stack,7)    
pop(stack,supporting_stack)    
push(stack,supporting_stack,1)    
push(stack,supporting_stack,1)    
pop(stack,supporting_stack)  
pop(stack,supporting_stack)
#print(getMin(supporting_stack))

#approach 2- tc- O(n)
global min_ele
min_ele=float('inf')
stack=[]
def new_push(stack,ele):
    global min_ele
    if len(stack)==0:
        min_ele=ele
        stack.append(ele)
    else:
        if ele<min_ele:
            stack.append(2*ele-min_ele)
            min_ele=ele
        else:
            stack.append(ele)       
def new_pop(stack):
    global min_ele
    if len(stack)==0:
        return
    else:
        if stack[-1]>=min_ele:
            stack.pop()
        else:
            min_ele=2*min_ele-stack[-1]
            stack.pop()
def new_top(stack):
    global  min_ele
    if len(stack)==0:
        return -1
    else:
        if stack[-1]>=min_ele:
            return stack[-1]
        else:
            return min_ele        
new_push(stack,3)    
new_push(stack,5)    
new_push(stack,7)    
new_pop(stack)    
new_push(stack,1)    
new_push(stack,1)    
new_pop(stack)  
new_pop(stack)
print(new_top(stack))
print(min_ele)




