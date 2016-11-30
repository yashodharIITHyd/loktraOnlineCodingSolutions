t=input()
for _ in range(t):
    n,m=map(int,raw_input().split())
    edgesList=[]
    for _ in range(m):
        edgesList.append(raw_input().strip())
    start=input()
    from pathValuesFunc import pathValuesFunc
    print pathValuesFunc(n,m,edgesList,start)