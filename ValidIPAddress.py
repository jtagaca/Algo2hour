def validIPAddresses(string):
    # Write your code here.
	# is this an ip which has a len of 4 is this ip valid?
	#
	# if there are 4 then we need to not have an index error
	finalresult = []
	result = ["", "", "", ""]
	if len(string) < 4:
		return []

	for i in range(1, len(string)):
		result[0] = string[:i]
		if not validIP(result[0]):
			continue
        # the min will keep the code in error from index out of range. 
		for ii in range(i+1, min(len(string), i+4)):
			result[1] = string[i:ii]
			if not validIP(result[1]):
				continue
			for iii in range(ii+1, min(len(string), ii+4)):
				result[2] = string[ii:iii]
				result[3] = string[iii:]
				if validIP(result[2]) and validIP(result[3]):
					finalstring = ".".join(result)
					finalresult.append(finalstring)



def validIP(string):
	strToNum=int(string)
	if strToNum >255:
		return False
	return len(string)==len(str(strToNum))


string ="97430"

validIPAddresses(string)
