s = "clementiscap"
l=[]
i=0
ans=[]
while i!=len(s):
    temp=''
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp+=s[j]
        else:
            break
    ans.append(temp)
    i+=1
curr=''
for i in ans:
    if len(i)>len(curr):
        curr=i
print(curr)