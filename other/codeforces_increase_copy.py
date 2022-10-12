from math import ceil
n=int(input())
count=0
i=1
minelement=n+n
while(True):
    total_moves=count + ceil((n-i)/i)
    print(f'total moves {total_moves} at i {i} count {count}')
    if(minelement >= total_moves):
        minelement=total_moves
        i+=1
        count+=1
    else:
        break
print(minelement)