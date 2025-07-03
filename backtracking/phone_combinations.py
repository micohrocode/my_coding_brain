def letterCombinations(digits):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def backtrack(path, idx):
        # check if you have met the required length
        # add to result
        if idx == len(digits):
            result.append(path)
            return
        
        # for each letter in the phone number
        # add to the path, increase the index
        for letter in phone[digits[idx]]:
            backtrack(path + letter, idx + 1)

    retult = []
    if digits:
        # start here for recursion
        backtrack("",0)
    return result