'''
print the no. of distinct countries. 
Sample Input

7
UK
China
USA
France
New Zealand
UK
France 
Sample Output

5
Explanati

UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).

'''

print(len(set([input() for i in range(int(input()))])))