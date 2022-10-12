for _ in range(int(input())):
    s=input()
    stack=list()
    count=0
    m=0
    for i in s:
        if(i=='('):
            stack.append(i);
        elif(i==')'):
            if(len(stack)!=0):
                j=stack.pop()
                if(j=='('):
                    count+=2
                else:
                   m=max(count,m)
                    count=0 
            else:
                m=max(count,m)
                count=0
    m=max(count,m)
    print(m)