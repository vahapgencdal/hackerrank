def staircase(n):
	stChars=""
	spChars=""
	i=0
	while(i<n):
		stChars+='#'
		spChars+=' '
		i+=1
	i=0
	while(i<n):
		print(spChars[int(0):int(n-i-1)]+stChars[int(0):(i+1)])
		i+=1


staircase(129999)


# char[] spChars=new char[n];
        # char[] stChars=new char[n];
        # for(int i=0;i<n;i++){
        #     spChars[i]=' ';
        #     stChars[i]='#';
        # }
        # for(int i=0;i<n;i++){
        #     System.out.println(
        #             String.valueOf(spChars).substring(0,n-i-1)+String.valueOf(stChars).substring(0,i+1));
        # }