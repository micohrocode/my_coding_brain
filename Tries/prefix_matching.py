def prefix(self, word):
    node = self.root
    
    # check that prefix is in the trie
    for char in word:
        if char not in node.children:
            return []
        node = node.children[char]

    result = []
    def dfs(node, current_word):
        # if a full word
        # add to the result
        if node.isEndOfWord:
            result.append(current_word)

        # move to next char for all children
        for char, child_node in node.children.items():
            dfs(child_node, current_word + char)
        
    dfs(node,word)

    return result