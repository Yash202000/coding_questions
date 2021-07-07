def reverse(t):
    ptr=False
    if t<0:
        ptr=True
        t=abs(t)

    while True:
        if t%10!=0:
            break
        else:
            t=t//10
    no=0
    while t:
        reminder = t%10
        no = no*10 + reminder
        t//=10

    if -2147483648 < no < 2147483648:
        if ptr:
            return 0-no
        else:
            return no
    else:
        return 0

        