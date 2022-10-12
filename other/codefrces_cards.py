'''
When Serezha was three years old, he was given a set of cards with letters for his birthday. They were arranged into words in the way which formed the boy's mother favorite number in binary notation. Serezha started playing with them immediately and shuffled them because he wasn't yet able to read. His father decided to rearrange them. Help him restore the original number, on condition that it was the maximum possible one.

Input
The first line contains a single integer n (1⩽n⩽105) — the length of the string. The second line contains a string consisting of English lowercase letters: 'z', 'e', 'r', 'o' and 'n'.

It is guaranteed that it is possible to rearrange the letters in such a way that they form a sequence of words, each being either "zero" which corresponds to the digit 0 or "one" which corresponds to the digit 1.

Output
Print the maximum possible number in binary notation. Print binary digits separated by a space. The leading zeroes are allowed.

Examples
inputCopy
4
ezor
outputCopy
0 
inputCopy
10
nznooeeoer
outputCopy
1 1 0 
Note
In the first example, the correct initial ordering is "zero".

In the second example, the correct initial ordering is "oneonezero".
'''
n,s=int(input()),input()
a={'z':0,'e':0,'r':0,'o':0,'n':0}
for i in s:
        a[i]+=1
res=str(1)*a['n'] + str(0)*a['z']
print(res)