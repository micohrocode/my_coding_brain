def mergeIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    merged = []

    for interval in sortedIntervals:
        # if there is nothing in merged yet
        # or they do not overlap
        if not merged or interval[0] > merged[-1][1]:
            # add the interval
            merged.append(interval)
        else:
            # merge them
            merged[-1][1] = max(interval[1], merged[-1][1])
    
    return merged