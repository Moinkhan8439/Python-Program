'''

'''



class Solution:
    def minimumSum(self, num: int) -> int:
        s=str(num)
        x=sorted(list(s))
        s=''.join(x)
        m=num
        if (int(s[0:2])+int(s[2:]) <= m):
            m=int(s[0:2])+int(s[2:])

        if(int(s[0:3])+int(s[3]) < m):
            m=int(s[0:3])+int(s[3])
            
        if int(s[0]+s[2]) + int(s[1]+s[3]) < m:
            m=int(s[0]+s[2]) + int(s[1]+s[3])
            
        return m

l=int(input())
x=Solution.minimumSum(Solution,l)
print(x)     



