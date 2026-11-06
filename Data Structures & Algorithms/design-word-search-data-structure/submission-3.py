class Trie:
    def __init__(self):
        self.children = {}
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch]= Trie()
            node= node.children[ch]
        node.is_end=True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False

            if ch not in node.children:
                return False

            node = node.children[ch]
            return dfs(node, i+1)

        return dfs(node, 0)
        
