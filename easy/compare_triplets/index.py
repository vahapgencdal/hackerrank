def compare_triplets(list_one, list_sec):
    rates = [0,0]
    i=0
    while(i<len(list_one)):
        if(list_one[i]>list_sec[i]):
            rates[0]=rates[0]+1
        elif(list_one[i]<list_sec[i]):
            rates[1]=rates[1]+1
        i=i+1
    return rates;

print(compare_triplets([17, 28, 30],[99, 16, 8]))