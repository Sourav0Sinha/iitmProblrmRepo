def consolidate(students):
    consol = {}
    
    for i in students:
        for j in i:
            if not(j in consol.keys()):
                consol[j]=1
            else:
                consol[j]+=1
                
    return consol

def popular(consol):
    maximum =[0,""]
    for k in consol.keys():
        if consol[k] > maximum[0]:
            maximum[0]=consol[k]
            maximum[1]=k
            
    return maximum[1]