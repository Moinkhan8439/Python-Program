def cidrtoIp(s,ran):
    cl=s.split('/')
    x=cl[0].split('.')
    ch=int(int(cl[1])/8)
    cbit=int(int(cl[1])%8)
    if cbit !=0:
        change=255-(2**(8-cbit)-1)
        x[ch]=str(change)
        for i in range(ch+1,len(x)):
            x[i]="0"
    else:
        for i in range(ch,len(x)):
            x[i]="0"
    if(ran=="end"):
        x[3]="255"
    ip=""
    for i in x:
        ip+=i+"."
    return ip[:-1]

def ipToint(s):
    ip=list(map(int,s.split('.')))
    num=256**3 * ip[0]+256**2 * ip[1]+256 * ip[2] +ip[3]
    return num



q=input().split()
r=int(q[0])
n=int(q[1])
reg=[]
for i in range(r): 
    reg.append(input().split())
ip=[]
for j in reg:
    start=cidrtoIp(j[0],"start")
    end=cidrtoIp(j[1],"end")    
    ip.append((ipToint(start),ipToint(end),j[2]))
for i in range(n):
    k=ipToint(input())
    flag=False
    for j in ip:
        if(k >= j[0] and k <= j[1]):
            flag=True
            print(j[2])
    if flag==False:
        print("None")
    
