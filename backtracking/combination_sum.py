def combinationSum(candidates, target):
    def backtrack(start, combo, current_target):
        # if the current target is zero
        # a solution has been found
        # add it
        if current_target == 0:
            result.append(list(combo))
            return
        
        # if not try to add the next number
        for i in range(start, len(candidates)):
            curr = candidates[i]
            # if to big of a number to be added
            # return
            if candidates[i] > current_target:
                return
            
            # if not too big
            # it is added to the combo
            combo.append(curr)
            # move to next current target
            backtrack(i, combo, current_target - curr)
            # target was too big, remove from combo, move to next number
            combo.pop()
        return
    
    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result