from bisect import bisect_right

def job_scheduling(starts, ends, profits):
    jobs = sorted(zip(starts, ends, profits), key = lambda x: x[1])

    dp = [0] * (len(jobs)+1)

    for i in range(1,len(dp)+1):
        start, end, profit = jobs[i-1]

        # number of jobs to finish before start of current job
        num_jobs = bisect_right(jobs, start, key=lambda x: x[1])

        dp[i] = max(dp[i-1], dp[num_jobs] + profit)

    return dp[-1]