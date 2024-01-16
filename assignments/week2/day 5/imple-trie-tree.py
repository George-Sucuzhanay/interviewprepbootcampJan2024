class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Trie:

    def __init__(self): # constructor
        self.root = TrieNode()
        

    def insert(self, word: str) -> None: # O(logn)
        # 1) both traverse exisiting prefix tree 
        # 2) while also traversing our word string to see if there is a prefix
        # already existing in our prefix tree
        curr = self.root
           
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_word = True

    def search(self, word: str) -> bool: # O(n)
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.end_word
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True       
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)