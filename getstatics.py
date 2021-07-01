from math import sqrt

#l = list(map(int,input().split()))

def give_Mean(l):
    return sum(l)/len(l)

def give_Median(l):
    l.sort()
    if len(l)%2==0:
        return (l[len(2)//2] +l[len(2)//2 - 1])/2

    else:
        return l[len(l)//2]

def give_Mode(l):
    l.sort()
    temp = set(l)
    curr = l.count(temp[0])
    ans = temp[0]
    for i in range(1,len(temp)):
        if curr < l.count(temp[i]):
            curr = l.count(temp[i])
            ans = temp[i]
    return ans


def give_SampleVariance(l,m):
    for i in range(len(l)):
        l[i] = (l[i]-m)**2
    print( sum(l)/(len(l)-1))

def give_SampleStandardDeviation(d):
    return sqrt(d)

def give_MeanConfidenceInterval(l):
    pass

def getStatics(l):
    d={}
    d['mean'] = give_Mean(l)
    d['median'] = give_Median(l)
    d['mode'] = give_Mode(l)
    d['sample_variance'] = give_SampleVariance(l,d['mean'])
    d['sample_standard_deviation'] = give_SampleStandardDeviation(d['sample_variance'])
    d['mean_confidence_interval'] = give_MeanConfidenceInterval(l,d['mean'],d['sample_standard_deviation'])

    return d