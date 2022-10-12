def hourglass(a):
    n=len(a)
    sums=[]
    for i in range(n-2):
        for j in range(n-2):
            sum=0
            for k in range(3):
                print(a[i][k]," ",a[i+2][k]," ",end="")
                sum+=a[i][k+j]+a[i+2][k+j]
            sum+=a[i+1][j+1]
            sums.append(sum)
            print(a[i+1][j+1])
            print(f"sum={sum} \n")
    return max(sums)


if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    print(hourglass(a))