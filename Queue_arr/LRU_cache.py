#task- given cache with certain frame size, calculate last remaining 
#       element in cache after certain insertion of pages
#approach- use queue of frame size hold pages, delete from front and insert at end
#          use set of frame size to hold unique value

def LRU_cache(arr,cache):
    st=set()
    queue=[]
    for a in arr:
        if a not in st:
            if len(queue)==cache:
                least_used=queue.pop(0)
                st.remove(least_used)
        else:
            queue.remove(a)
        queue.append(a)
        st.add(a) 
    return queue
#array of pages
arr=[1,2,3,1,4,5,2,2,1] 
cache=4   
print(LRU_cache(arr,4))        



