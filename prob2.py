

def product(li):
    if len(li) == 1:
        return li[0]
    else:
        return li[0]*product(li[1:])

def process_line(i):
    f = open("numbers.txt","r")
    
    li = f.readlines()
    
    
    
    flag = not(i >= len(li)) 
    
    if flag:
        q = str(li[i])
        q = q.strip()
        gi = q.split(",")
    
        num = lambda x : int(x)
    
        ans = map(num,gi)
        ans = list(ans)
        N = len(ans)
        S = sum(ans)
        P = product(ans)
        return (N,S,P)
    else:
        return (-1,-1,-1)
    