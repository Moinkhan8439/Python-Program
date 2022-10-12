import textwrap
from collections import Counter
def merge_the_tools(string, k):
    for i in textwrap.wrap(string,k):
        temp=""
        for j in i:
            if(j not in temp):
                print(j,end="")
            temp+=j
        print(end="\n")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)