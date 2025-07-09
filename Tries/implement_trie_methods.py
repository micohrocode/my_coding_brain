def search(self, word):
    node = self.root

    for char in word:
        # next char not found, end
        if char not in node.children:
            return False
    
        # char is in children
        # move to that node
        node = node.children[char]
    
    # check the node is the end of a word
    # if so its there in the trie
    return node.is_end_of_word

def delete(self, word):
    def _delete(node, index):
        if index == len(word):
            if not node.isEndOfWord:
                return False
            # remove end of word
            node.isEndOfWord = False
            # check for children
            # would mean there are other words that need it
            return len(node.children) == 0
        
        # next char is not found
        char = word[index]
        if char not in node.children:
            return False
    
        # check if the chars child must be deleted
        delete_child = _delete(node.children[char], index+1)
        # delete it if needed
        if delete_child:
            del node.children[char]
            return not node.isEndOfWord and len(node.children) == 0
        return False

    if _delete(self.root,0):
        if word and word[0] in self.root.children:
            # delete first character from the roots children
            del self.root.children[word[0]]