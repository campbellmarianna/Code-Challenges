class Trie:

    # [root:[[t, a, b], [i, r]], [{t:[h, n, y]}, {a:[[n, s, w, e,r], [y]]}], {b:[y, e]},]
    def __init__(self):
        """
        Initialize your data structure here.
        """


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

# Attempt Number 1


class TrieNode:
    # Trie node class
    def __init__(self):
        self. children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()

    def getNode(self):

        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        if not self.root.children:
            return False
        for char in prefix:
            char_not_found = True
            # for child in node.children:
            length = len(prefix)
            for level in range(length):
                index = self._charToIndex(prefix[level])
                # if child.char == char:
                if node.children[index] == char:
                    char_not_found = False
                    node = node.children[index]
                    break
            if char_not_found:
                return False
        return True

# Final Attempt:


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                start[i] = {}
            start = start[i]
        start['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                return False
            start = start[i]
        return '$' in start

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start = self.root
        for i in prefix:
            if i not in start:
                return False
            start = start[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
