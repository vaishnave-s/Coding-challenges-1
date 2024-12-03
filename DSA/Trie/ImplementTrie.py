# Root
#  ├── a
#  │   ├── p
#  │   │   ├── p
#  │   │   │   ├── l
#  │   │   │   │   ├── e (end)   # apple
#  │   │   │   ├── e (end)       # appe
#  │   │
#  │   ├── s
#  │       ├── l
#  │           ├── e
#  │               ├── e
#  │                   ├── p (end)   # asleep
#  │
#  ├── b
#  │   ├── a
#  │       ├── t (end)           # bat
#  │       ├── n
#  │           ├── a (end)       # bana
#  │
#  ├── c
#      ├── a
#          ├── t (end)           # cat

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEndOfWord =True
    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current=current.children[char]
        return current.isEndOfWord
        



    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
                

    def wordAsString(self)->str:
        current=self.root.children
        word=""
        while True:
            letter = list(current.keys())[0]
            word = word+letter
            if current[letter].isEndOfWord:
                break
            current = current[letter].children
        return word

# word="jhell"
# # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# a=obj.wordAsString()
# print(a)
