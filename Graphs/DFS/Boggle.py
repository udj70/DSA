#given a matrix of character and dictionary of words, 
#task is to find words that can be formed using chars in matrix and words are present in dictionary 
def isword(word,dic):
    for d in dic:
        if word==d:
            return True
    return False
def isafe(i,j,r,c,visited):
    if i<r and i>=0 and j<c and j>=0 and not visited[i][j]:
        return True
    return False    
def findWordUtil(word,visited,boggle,i,j,r,c,dic):
    visited[i][j]=True
    if isword(word+boggle[i][j],dic):

        print(word+boggle[i][j])
    word=word+boggle[i][j]    
    row=[-1,-1,0,1,1,1,0,-1]
    col=[0,1,1,1,0,-1,-1,-1]
    for p in range(8):
        if isafe(i+row[p],j+col[p],r,c,visited):

            findWordUtil(word,visited,boggle,i+row[p],j+col[p],r,c,dic)
    visited[i][j]=False
    word=word[:-1]
def findWord(boggle,dic):
    r=len(boggle)
    c=len(boggle[0])
    visited=[[False for _ in range(c)] for _ in range(r)]
    word=''
    for i in range(r):
        for j in range(c):
            findWordUtil(word,visited,boggle,i,j,r,c,dic) 


boggle=[ [ 'G', 'I', 'Z' ], 
        [ 'U', 'E', 'K' ], 
        [ 'Q', 'S', 'E' ] ]; 
dic=["GEEKS", "FOR", "QUIZ", "GO" ] 
findWord(boggle,dic) 

