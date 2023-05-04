def floodFillUtill(sheet,x,y,new,prev):
    row=len(sheet)
    col=len(sheet[0])
    if x<0 or x >=row or y<0 or y>=col or sheet[x][y]==new or sheet[x][y]!=prev:
        return 
   
    #sheet[x][y]==prev:
    sheet[x][y]=new
    floodFillUtill(sheet,x+1,y,new,prev)
    floodFillUtill(sheet,x,y-1,new,prev)
    floodFillUtill(sheet,x-1,y,new,prev)
    floodFillUtill(sheet,x,y+1,new,prev)    



def floodFill(sheet,x,y,new):
    prev=sheet[x][y]
    floodFillUtill(sheet,x,y,new,prev)
    for s in sheet:
        print(" ".join(list(map(str,s))))



# main code
sheet=[[1, 1, 1, 1, 1, 1, 1, 1],  
          [1, 1, 1, 1, 1, 1, 0, 0],  
          [1, 0, 0, 1, 1, 0, 1, 1],  
          [1, 2, 2, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 2, 2, 0],  
          [1, 1, 1, 1, 1, 2, 1, 1],  
          [1, 1, 1, 1, 1, 2, 2, 1]] 
floodFill(sheet,4,4,3)                  






