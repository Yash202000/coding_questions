#use chr() to convert ascii no to char
#use ord() to convert char to ascii no

def encryptbyC(t,k):
    if ord(t)+k>122:
        return chr(97+(ord(t)+k-123))
    return chr(ord(t)+k)

def main():
    t = input()
    k = int(input())
    temp=[]
    for i in t:
        temp.append(encryptbyC(i,k))

    print("".join(temp))
        

if __name__=='__main__':
    main()