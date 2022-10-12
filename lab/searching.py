a=list(map(int,input().split()))
n=int(input("enter the element to be searched"))
flag=True
for i in range(len(a)):
    if arr[i] == n:
        print(f'present at index {i}')
        flag=False
if(flag):
    print("Not Found")


