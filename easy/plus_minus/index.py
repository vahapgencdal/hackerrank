
def plus_minus(arr) :
    pos_num= neg_num= zero_num= 0
    for ar in arr :
        if(ar<0) :
            neg_num+=1
        elif(ar>0) :
            pos_num+=1
        else:
            zero_num+=1
    print(format(pos_num/len(arr), '.6f'))
    print(format(neg_num/len(arr), '.6f'))
    print(format(zero_num/len(arr),'.6f'))

plus_minus([-4, 3, -9, 0, 4, 1])