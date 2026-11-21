
class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie_tree:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]

        node.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        t = Trie_tree()

        for word in wordDict:
            t.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            node = t.root

            for j in range(i, n):
                if s[j] not in node.children:
                    break

                node = node.children[s[j]]

                if node.is_end:
                    dp[j + 1] = True

        return dp[n]
