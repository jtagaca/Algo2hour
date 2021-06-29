def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	total=0
	for idx, query in enumerate(queries):
		#represents the right of the array
		remaining=len(queries)-(idx+1)
		total+=query*remaining

	
    return total

