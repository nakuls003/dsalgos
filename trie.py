class Trie:

    class Node:
        def __init__(self):
            self.children = {}
            self.is_word_end = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, self.Node())
        curr.is_word_end = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_word_end

    def search_prefix(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def delete(self, word):
        self.rec_delete(self.root, word, 0)

    def rec_delete(self, curr, word, index):
        if index == len(word):
            if not curr.is_word_end:
                return False
            curr.is_word_end = False
            return len(curr.children) == 0
        
        if word[index] not in curr.children:
            return False
        can_delete_node = self.rec_delete(curr.children[word[index]], word, index+1)
        if can_delete_node:
            del curr.children[word[index]]
            return len(curr.children) == 0
        return False