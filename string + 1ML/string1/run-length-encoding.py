def run_length_encoding(t):
    s=""
    count=1
    for i in range(1,len(t)):
        if t[i-1]==t[i]:
            count+=1
            if count>9:
                s=s+"{}{}".format(count-1,t[i-1])
                count=1
            elif len(t)-1==i:
                s=s+"{}{}".format(count,t[i-1])
        else:
            s=s+"{}{}".format(count,t[i-1])
            count=1

    return s

if __name__=='__main__':
    t=input()
    print(run_length_encoding(t))


