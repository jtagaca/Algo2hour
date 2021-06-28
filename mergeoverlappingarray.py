def mergeOverlappingIntervals(intervals):
    # Write your code here.
    # sorted the intervals here and maded a copy but this did not affect the original interval
	sortedIntervals= sorted(intervals,key=lambda x: x[0])
    output=[]
    currentInterval=(sortedIntervals[0])
    #appended something so that we can use this to compare something
    output.append(currentInterval)


    for nextInterval in sortedIntervals:
        # decomposed the numbers inside the intervals for easy comparison
        prevnum,prevend= currentInterval
        nextnum,nextend=nextInterval
        if prevend>= nextnum:
            # we checked to see if we are overlapping if yes then we find the max of the ends
            #we do not append because we use the else to append it this is just to handle our merges
            currentInterval[1]=max(prevend, nextend)

        else:
            # there was no overlap so we just change the currentInterval to the nextInterval
            # we are setting the currentInterval as the previous number after the loop and we are appending it 
            # for 
            currentInterval=nextInterval
            output.append(currentInterval)



    return output
