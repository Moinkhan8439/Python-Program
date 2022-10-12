#Declaring a function
def evenodd(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"

if __name__=="__main__":
    n=int(input("enter the number : "))
    res=evenodd(n)          #calling a function
    print(res)
