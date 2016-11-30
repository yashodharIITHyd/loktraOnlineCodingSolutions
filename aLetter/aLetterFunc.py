from itertools import combinations
def aLetterFunc(arr,n,k):
    c1=combinations(arr,k)
    count=0
    count2=0
    while 1:
        try:
            v1=list(c1.next())
            if 'a' in v1:
                count+=1
        except:
            break
        count2+=1
    return float(count)/count2