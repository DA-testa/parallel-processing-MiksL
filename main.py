def parallel_processing(n, m, data):
    output = []
    
    currentJobs = [] # Stores a list of the thread index and the time it takes to finish the job (n, t(i))
    
    # Before the loop, initialize the currentJobs list with threads (assign an initial job to each thread)
    for thread in range(n):
        currentJobs.append([thread, 0])
    
    while len(data) > 0:
        for thread in range(n):
            # Find the thread with the shortest time to finish the job (if time is the same,we use the thread with the lowest index, which min will return anyway)
            minTime = min(currentJobs, key=lambda x: x[1])
            # Take the thread out of the currentJobs list and add it to the output list
            removedJob = currentJobs.pop(currentJobs.index(minTime))
            output.append(removedJob)
            
            currentJobs.append([removedJob[0], removedJob[1] + data[0]]) # Add the job to the currentJobs list
            data.pop(0) # Remove the job from the data list
            if len(data) == 0:
                break

    return output

def main():
    # first line - n and m
    userInput = input().split()
    # n - thread count 
    # m - job count
    n = int(userInput[0])
    m = int(userInput[1])

    # second line - data 
    jobInput = input().split()
    # data - contains m integers t(i) - the time it takes any thread to process i-th job
    data = []
    for i in range(m):
        data.append(int(jobInput[i])) # place the data into a list

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0], pair[1])



if __name__ == "__main__":
    main()
