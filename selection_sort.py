# created a python file directly from github
a= [5,32,1,6,4]
n= len(a)
for i in range(0,n):
    small=i
    for j in range(i+1,n):
        if a[small] > a[j]:
            small = j
    a[i],a[small] = a[small],a[i]

print(a)