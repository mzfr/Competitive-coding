# BST Insertion

__URL__:: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

## Solution

The solution for this is simple. We know that if the value is greater than the root node then it goes in the right subtree else it goes in the left subtree.

so we just use this along with the while loop to do the insertion.

##

It only have the main/core logic of the problem. If you want the full code merge my code along with the code given on hackerrank.

```python
def insert(self, val):
    if self.root is None:
        self.root = Node(val)

    root = self.root
    
    while True:
        # Going Right
        if val > root.info:
            if root.right:
                root = root.right
            else:
                root.right = Node(val)
                break
        # Going left
        elif val < root.info:
            if root.left:
                root = root.left
            else:
                root.left = Node(val)
                break
        else:
            break
```
