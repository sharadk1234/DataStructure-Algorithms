
from ipywidgets import widgets
from IPython.display import display
## Trie data Structure ##
# To see weather a word exst in a data Structure the simplest way is using a hashMap of all known
# words from the knowledge but it would take O(1) to see if the word exist and the memory size it would
# take wll be O(nm), where n is the numbers of words and m is the length of the word let see how Trie
# can solve the problem Of Memory consumption.
# in basic Trie word "a" and "add" overlaps this is where Trie saves memory instead of having "a"
# "add" in dfferent cells. instead of having "a" and "add" in different cell the character
# treated nodes in a tree

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
# Building a Trie in Python
# Before we start let us reiterate the key components of a Trie or Prefix Tree.
# A trie is a tree-like data structure that stores a dynamic set
# of strings. Tries are commonly used to facilitate operations like
# predictive text or autocomplete features on mobile phones or web search.
# Before we move into the autocomplete function we need to create a working
# trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie,
# like inserting a word or finding the node which represents a prefix.
# The Trie itself containing the root node and insert/ find function
# Trie Itself containing the root node and insert and find functions

from ipywidgets import widgets
from IPython.display import display
# Representing a single node in the Trie
class TrieNode:
    def __init__(self):
        # Intialize this node in the Trie
        self.is_word = False
        self.children ={}
        self.results = {}

    def insert(self, char):
        #Add a chid Node in this Trie
        self.children[char] = TrieNode()


## The Trie itself containing the root Node and insert/ find functions

class Trie:
    def __init__(self):
        # Intialize this Trie(add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to a Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find The Trie node that Represent this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}
        self.results = set()

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        #Recurse function that collects the suffix for
        # all complete words below this point
        results = []
        if self.children:
            for char, node in self.children.items():
                if node.is_word:
                    results.append(suffix + char)
                node.suffixes(suffix + char)
        return list(results)



results=list()
MyTrie = Trie()
wordList = ["ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f,prefix='');
results=[]
interact(f,prefix='tr');
results=[]
interact(f,prefix='f');
results=[]
interact(f,prefix='ant');