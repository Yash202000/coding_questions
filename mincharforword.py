def give_min_char_array(l):
    count=0
    stack = []
    for i in l:
        for j in i:
            if j not in stack:
                stack.append(j)
            else:
                if stack.count(j) < i.count(j):
                    stack.append(j)

    return stack

t=give_min_char_array(['this','did','deed','that','them!','a'])
print(t)
