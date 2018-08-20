def string_similarity(s):
    counter=len(s)
    sLength=len(s)
    i=1
    j=0
    while i<sLength:
        while j<sLength-i:
            if(s[j]!=s[i+j]):
                break
            j+=1
            counter+=1
        i+=1
        j=0
    return counter


print(string_similarity("ababaaabbaba"))