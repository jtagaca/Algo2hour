def taskAssignment(k, tasks):
    # Write your code here.
    
    copyTasks=sorted(tasks)
    #get the indices on a map 
    lookUptask=getIndices(tasks)
    pairedTasks=[]
    # we can do this because we know it will always be even otherwise we cannot 
    for i in range(k):
        taskDuration1=copyTasks[i]
        # we find the index using the dictionary on that was returned from the helper function
        
        #this is still a list so we have to pop of only 
        indexOftask1list=lookUptask[taskDuration1]
        indexoftask1=indexOftask1list.pop()

        taskDuration2=copyTasks[len(tasks)-1-i]
        indexOftask2list=lookUptask[taskDuration2]
        indexoftask2=indexOftask2list.pop()
        pairedTasks.append([indexoftask1, indexoftask2])

    return pairedTasks

def getIndices(tasks):
    lookUptask={}

    for idx, taskdur in enumerate(tasks):
        #if the taskduration is already in the dictionary because 
        #dictionary contains a list 
        if taskdur in lookUptask:
            lookUptask[taskdur].append(idx)
        else:
			
            #we create it if it's not in the dictionary creating a list to enable append since there might be 
			# duplicate values on an array
            lookUptask[taskdur]=[idx]
    return lookUptask

