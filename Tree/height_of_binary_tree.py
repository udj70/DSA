import insert
import sys
sys.path.append('H:\Python\Queue_LL')
import createQueue
def heightOfBinTreeByLOT(root):
    q=createQueue.Queue()
    count=0
    if not root:
        print('memory error')
        return 0
    else:    
        q.Enqueue(root)
        q.Enqueue(None)

        while(not q.IsEmptyQueue()):
            temp=q.Dequeue()
            #end of a level
            if temp==None:
                if not q.IsEmptyQueue():
                    q.Enqueue(None)
                count=count+1
            else:
                if temp.left is not None:
                    q.Enqueue(temp.left)
                if temp.right is not None:
                    q.Enqueue(temp.right)
    return count                    



root=insert.insert(1,2,3)
count=heightOfBinTreeByLOT(root)
print(count)


