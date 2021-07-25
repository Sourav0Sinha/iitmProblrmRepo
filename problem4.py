def rowReversed(matrix):
    ans =  []
    for i in range(1,len(matrix)+1):
        ans.append(matrix[len(matrix)-i])
        
    return ans

def colReversed(matrix):
    ans = []
    for i in matrix:
        ans.append(i[-1:-1*(len(i)+1):-1])
        
    return ans

n = int(input())
matrix =[]
for i in range(n):
    
    data = input().split(",")
    matrix.append(data)
    
exp = str(input())

if exp == 'row':
    ans = rowReversed(matrix)
    
else:
    ans = colReversed(matrix)
   
for i in ans:
    for j in range(len(i)-1):
        print("{},".format(int(i[j])),end = "")
    print(int(i[j+1]))
        