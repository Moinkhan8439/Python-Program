'''TASK
You are given a set A  and  number of other sets. These  number of sets have to perform some specific mutation operations on set A .

Your task is to execute those operations and print the sum of elements from set A.
Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output

38
Explanation

After the first operation, (intersection_update operation), we get:
set 

After the second operation, (update operation), we get:
set 

After the third operation, (symmetric_difference_update operation), we get:
set 

After the fourth operation, ( difference_update operation), we get:
set 

The sum of elements in set A after these operations is 38 .'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
a=set(map(int,input().split()))
print(a)
d={'intersection_update':a.intersection_update,'update':a.update,'symmetric_difference_update':a.symmetric_difference_update,'difference_update':a.difference_update}
for i in range(int(input())):
    c=input().strip().split()
    k=set(map(int,input().split()))
    print(c,k)
    d[c[0]](k)
    print(a)
print(sum(a))
