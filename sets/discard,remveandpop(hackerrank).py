'''sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4
Explanation

After completing these  operations on the set, we get set([4]). Hence, the sum is 4 .'''

n = int(input())
s = set(map(int, input().split()))
d={"remove":s.remove ,"discard":s.discard,"pop":s.pop}
for i in range(int(input())):
    c=input().split()
    d[c[0]](int(c[1])) if(len(c)>1) else  d[c[0]]()
print(sum(s))