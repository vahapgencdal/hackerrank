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