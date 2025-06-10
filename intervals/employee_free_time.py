def employeeFreeTime(schedule):
    flattened = [i for employee in schedule for i in employee]
    intervals = sorted(flattened, key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # if there are none in merged
        # or they are not overlapping, add them
        if not merged or merged[-1][1]<interval[0]:
            merged.append(interval)
        else:
            # else, merge the two
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    free_times = []
    for i in range(1, len(merged)):
        # set the start and end of the free time
        # between the intervals
        start = merged[i - 1][1]
        end = merged[i][0]
        free_times.append([start,end])
    
    return free_times