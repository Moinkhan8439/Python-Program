'''there are n cartridges and m dollars given to you and yoou have two option either refill the cartridges and get two dollars or give 
one cartridge and perkcost dollar and get one perk rewards .our task to get the maximum perk rewards. '''

cart,dol=int(input("enter the no. of cartridges :")),int(input("enter dollars: "))
rewards=int(input("enter the recycle rewards : "))
perkcost=int(input("enter the perk cost : "))
m=0
if(dol//perkcost >= cart):
        m=cart
else:
    while(cart):
        cart=cart-1
        dol=dol+rewards
        cur=cart if cart <=dol//perkcost else dol//perkcost
        if(cur > m):
            m=cur
        else:
            break
print(m)
        

