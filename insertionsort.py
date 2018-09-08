def insertion(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while(i>-1 and a[i]>key):
            a[i+1]=a[i]
            i-=1
        a[i+1]=key
    print(a)
lst=[]
n=int(input('Enter the no. of elements'))
for i in range(n):
    lst.append(int(input()))
insertion(lst)
