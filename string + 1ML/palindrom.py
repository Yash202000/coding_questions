def checkPalindrom(t):
    if len(t)==1:
        return True
    else:
        for i in range(len(t)//2):
            if t[i]!=t[-i-1]:
                return False
        return True


if __name__=='__main__':
    print(checkPalindrom("abcdcba"))
