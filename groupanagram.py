
def group_anagram_helper(l):
    temp=[]
    curr = list(l.pop(0))
    curr.sort()
    curr = "".join(curr)
    temp.append(curr)
    for i in l:
        t = list(i)
        t.sort()
        print(t)
        if "".join(t) == curr:
            temp.append(i)
            l.remove(i)

    return temp

def make_group_anagram(l):
    ans = []
    while len(l)!=0:
        ans.append(group_anagram_helper(l))

    return ans


t=make_group_anagram(["yo","act",'flop','tac','foo','cat','oy','olfp'])
print(t)

