import string


key = string.ascii_uppercase

dictionary = {k:key.index(k)+1 for k in key }



str1 = input()
ans = 0

if len(str1) == 3:
    ans += dictionary[str1[0]]*26*26
    str1 = str1[1:]
    
if len(str1) == 2:
    ans += dictionary[str1[0]]*26
    str1 = str1[1:]
    
if len(str1) == 1:
    ans += dictionary[str1[0]]
    str1 = ""
    
print(ans)