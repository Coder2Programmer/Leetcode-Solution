class TrieNode:
    def __init__(self):
        self.children = dict()
        self.value = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = True
        
    def find(self):
        def dfs(cur, node):
            if node.value:
                folder.append('/' + '/'.join(cur))
                return
            for char in node.children:
                dfs(cur + [char], node.children[char])
        folder = []
        dfs([], self.root)
        return folder


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f.split('/')[1:])
        return trie.find()

