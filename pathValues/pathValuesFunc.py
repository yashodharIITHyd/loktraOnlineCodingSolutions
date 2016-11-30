def pathValuesFunc(n,m,edgesList,start):
    edges=[['*' for _ in range(n+1)] for _ in range(n+1)]
    for k in range(m):
        n1,n2=map(int,edgesList[k].split())
        edges[n1][n2]=1
        edges[n2][n1]=1
    path=[None]*(n+1)
    visited=[False]*(n+1)
    visited[start]=True
    path[start]=0
    from collections import deque
    q=deque()
    q.append(start)
    while 1:
        count=q.__len__()
        if count==0:
            break
        while count>0:
            parent=q.popleft()
            visited[parent]=True
            for child in range(1,n+1):
                if edges[parent][child]!='*' and visited[child]==False:
                    if path[child]==None:
                        path[child]=path[parent]+1
                    else:
                        path[child]=min(path[child],path[parent]+1)
                    visited[child]=True
                    q.append(child)
            count-=1
    i=1
    res=''
    while i<=n:
        if i==start:
            i+=1
            continue
        else:
            if path[i]==None:
                #print -1,
                res+='-1 '
            else:
                #print path[i]*6,
                res+=str(path[i]*6)+" "
        i+=1
    return res.strip()