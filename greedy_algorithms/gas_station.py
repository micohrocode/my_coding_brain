def canCompleteCircuit(gas, cost):
    # not enough total gas to complete
    if sum(gas) < sum(cost):
        return -1
    
    start, fuel = 0,0

    for i in range(len(gas)):
        if fuel + gas[i] - cost[i] < 0:
            # not enough fuel to get to next station
            # start at next station instead
            start, fuel = i+1, 0
        else:
            # can reach next station
            # update fuel total
            fuel += gas[i] - cost[i]
    
    return start