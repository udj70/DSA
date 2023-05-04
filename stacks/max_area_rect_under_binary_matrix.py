#task- given matrix of 0 and 1 , find max size rectangle
#approach- divide matrix among rows and pass each row in MAH function and update max size


import maxAreaUnderHistogram

matrix=[[0,1,1,0],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0]]
m=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]!=0:
            matrix[i][j]+=matrix[i-1][j]
    m=max(m,maxAreaUnderHistogram.MAH(matrix[i]))
print(m)


