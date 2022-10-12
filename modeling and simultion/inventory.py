import random
import decimal

def minimum(p,q):
    due_d,due_u,stocks,cost=0,0,115,0
    for i in range(180):
        if(i+1==due_d):
            stocks+=q
            due_u=0
        random.seed(i)
        demand=random.randint(1,10)
        if(demand<=stocks):
            stocks-=demand
            cost+=stocks*0.75
        else:
            cost+=18*(demand-stocks)
            stock=0
        if(stocks+due_u <= p):
            due_u=q
            cost+=75
            due_d=i+4
    return cost

if __name__ == "__main__":
    print("please enter the reorder point and quantity in ordered manner for eg: \n reorder points : a b c \n reorder quanity  : x y z")
    x=list(map(int,input("enter reorder point  : \t ").split()))
    y=list(map(int,input("enter reorder quantity : ").split()))
    m=minimum(x[0],y[0])
    count=0
    for i in range(len(x)):
        k=minimum(x[i],y[i])
        if(m > k):
            m=k
            count+=1
    print(f'the best policy is : {count} and the best cost is : {m}')
