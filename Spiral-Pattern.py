n,m=map(int,input().split()) # input for row and column length
l=[]
for i in range(n):
    t=list(map(int,input().split()))   #input column values per row
    l.append(t)                        #each row gets appended to the list

left=0;upper=0;right=m-1;lower=n-1
while(left<=right and lower>=upper):
    i=left
    while(i<=right and lower>=upper):
        print(l[upper][i],end=" ")
        i+=1
    upper+=1
    i=upper
    while(i<=lower and left<=right):
        print(l[i][right],end=" ")
        i+=1
    right-=1
    i=right
    while(i>=left and lower>=upper):
        print(l[lower][i],end=" ")
        i-=1
    lower-=1
    i=lower    
    while(i>=upper and left<=right):
        print(l[i][left],end=" ")
        i-=1
    left+=1
    
