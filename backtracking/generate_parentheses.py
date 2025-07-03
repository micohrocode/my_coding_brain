def generateParentheses(n):
    res = []

    def dfs(s, open, close):
        # met the needed length
        if len(s) == 2*n:
            res.append(s)
            return
        
        if open<n:
            # not enough open parens
            # add one more
            dfs(s+'(', open + 1, close)

        if close < open:
            # not enough closed parens
            # add one more 
            dfs(s+')', open, close + 1)

    dfs('',0,0)
    return res