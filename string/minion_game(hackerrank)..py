def minion_game(string):
    k,s=0,0
    for i in range(len(string)):
        if(string[i] in "aeiou"):
            k+=len(string)-i
            print("try")
        else:
            s+=len(string)-i
    if k>s:
        print(f"Kevin {k}")
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")
    print(k)
if __name__ == '__main__':
    s = input()
    minion_game(s)