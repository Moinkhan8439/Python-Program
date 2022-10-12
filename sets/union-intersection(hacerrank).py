'''Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

13
Explanation

Roll numbers of students who have at least one subscription:
 and . Roll numbers:  and  are in both sets so they are only counted once.
Hence, the total is  students 13.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
a=set(input().split())
input()
b=set(input().split())
print("union :",len(a.union(b))) #for intersection use intersection(&) in place of union(|)
print("intersection :",len(a&b))
print("difference:",len(a-b))           #adifference(b)
print("symmetric difference:",len(a^b)) #a.symmetric_difference(b)