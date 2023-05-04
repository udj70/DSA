def issafe(matrix,i,j,r,c,visited):
	if i<r and i>=0 and j<c and j>=0 and matrix[i][j]==1 and not visited[i][j]:
		return True
	return False

def riverSizes(matrix):
    
		r=len(matrix)
		c=len(matrix[0])
		visited=[[False for _ in range(c)] for _ in range(r)]
		ans=[]
		for i in range(r):
			for j in range(c):
				queue=[]
				count=0
				
				if not visited[i][j] and matrix[i][j]==1:
					
					queue.append((i,j))
					visited[i][j]=True
					while(len(queue)):
						count+=1	 
						cell=queue.pop(0)
						p=cell[0]
						q=cell[1]	 
						#visited[p][q]=True	 
						if issafe(matrix,p+1,q,r,c,visited):
							queue.append((p+1,q))
							visited[p+1][q]=True
						if issafe(matrix,p-1,q,r,c,visited):
							queue.append((p-1,q))
							visited[p-1][q]=True
						if issafe(matrix,p,q+1,r,c,visited):
							queue.append((p,q+1))
							visited[p][q+1]=True
						if issafe(matrix,p,q-1,r,c,visited):
							queue.append((p,q-1))
							visited[p][q-1]=True
					ans.append(count)
		return ans				
matrix=[
		[1,1],
		[1,0]
	]		
print(riverSizes(matrix) )  
							
							
