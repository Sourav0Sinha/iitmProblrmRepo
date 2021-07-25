data = input()

li = list(data)

li.sort()



answer = ""
gi = []

for i in li:
    for j in li:
        for k in li:
            answer = i+j+k
            gi.append(answer)
            
for i in gi: print(i)

