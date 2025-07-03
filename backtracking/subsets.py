def subsets(nums):
    def dfs(index, path):
        if index == len(nums):
            result.append(path[:])
            return
        
        # include in path
        path.append(nums[index])
        dfs(index + 1, path)

        # exclude from path
        path.pop()
        dfs(index + 1, path)

    result = []
    dfs(0, [])

    return result