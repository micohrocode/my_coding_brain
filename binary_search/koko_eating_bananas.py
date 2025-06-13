class Solution:
    def minHarvestRate(self, apples, h):
        # find time take for each rate
        def time_taken(rate):
            time = 0
            for i in range(len(apples)):
                time+= (apples[i] + rate - 1) // rate
            return time

        # rates of eating, 1 to max of apples on one tree
        left, right = 1, max(apples)
        while left < right:
            # find the middle
            mid = (left+right) // 2
            # check if the time taken for that rate is
            # greater than the h given
            if time_taken(mid) > h:
                # check the right side
                left = mid + 1
            else:
                # check the left side
                right = mid

        return left
