t=[2,3,5]
# 2,3,,6,7

"""
2,3,5
8

2,3,6,7
7

"""
target=8

l=[]
for i in t:
    temp=[]
    temp.append(i)
    no=target//i
    temp = temp*no
    l.append(temp)
    print(temp)
print(l)


ans=[]
c=0
while len(l):
    exp1 = l.pop(0)
    exp = exp1.copy()
    #print(exp)
    c+=1
    s=sum(exp)
    print("sum is : ",s)
    if s==target:
        print("appended as it is  : ",exp)
        ans.append(exp)
        print("as it is ans: ",ans)
        print()
    
    if exp:
        while True:
            try:
                te=exp.pop(0)
            except IndexError as e:
                break
            #s=s-te
            if c<len(t):
                exp.append(t[c])
                print("exp is : ",exp)
                #s=s+t[c]
            if sum(exp)>target:
                break
            
            elif sum(exp)==target:
                ans.append(exp)
                print(ans," this is ans")
                print("sadlfkj",exp)
                
    

print(ans)





"""
target=8

l=[]
for i in t:
    temp=[]
    temp.append(i)
    no=target//i
    temp = temp*no
    l.append(temp)
    print(temp)
print(l)


ans=[]
c=0
while len(l):
    exp = l.pop(0)
    #print(exp)
    c+=1
    s=sum(exp)
    print("sum is : ",s)
    if s==target:
        print("appended as it is  : ",exp)
        ans.append(exp)
        print("as it is ans: ",ans)
        print()
    exp=[exp[0]]*len(exp)
    if exp:
        while True:
            try:
                te=exp.pop(0)
            except IndexError as e:
                break
            #s=s-te
            if c<len(t):
                exp.append(t[c])
                print("exp is : ",exp)
                #s=s+t[c]
            if sum(exp)>target:
                break
            
            elif sum(exp)==target:
                ans.append(exp)
                print(ans," this is ans")
                print("sadlfkj",exp)
                exp=[]
                
    

print(ans)



"""


"""
target=8

l=[]
for i in t:
    temp=[]
    temp.append(i)
    no=target//i
    temp = temp*no
    l.append(temp)
    print(temp)
print(l)

stack=[]
ans=[]
c=0
while len(l):
    exp = l.pop(0)
    #print(exp)
    c+=1
    s=sum(exp)
    print("sum is : ",s)
    if s==target:
        print("appended as it is  : ",exp)
        ans.append(exp)
        print("as it is ans: ",ans)
        print()
    exp=[exp[0]]*len(exp)
    if exp:
        pre=exp[0]
        te=-1
        while True:
            if te==pre:
                break
            try:
                te=exp.pop(0)
                
            except IndexError as e:
                break
            #s=s-te
            if c<len(t):
                exp.append(t[c])
                print("exp is : ",exp)
                #s=s+t[c]
            
                #break
            
            elif sum(exp)==target:
                stack.append(exp)
                ans.append(exp)
                print(ans," this is ans")
                print("sadlfkj",exp)
                exp=[]
            if sum(exp)>target:
                pre = exp[0]
                print(pre," ", te)
                    
    

print(ans)
print(stack)


"""