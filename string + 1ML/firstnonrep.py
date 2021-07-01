t=input()
def firstNonRepChar(t):
    for i in t:
        if t.count(i)==1:
            return t.index(i)

print(firstNonRepChar(t))