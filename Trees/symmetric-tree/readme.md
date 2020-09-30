## Symmetric Tree

__URL__:: https://leetcode.com/problems/symmetric-tree/submissions/

## Solution

we are given a tree we need to tell if its mirror of itself. What we did in our solution is that we recursively check if the left and right elements of the tree are equal or not. Now the time complexity for this would be `O(n)` and the space complexity will be `O(h)`, here `h` is the height of the tree. We need `O(h)` because this is a recursive approach and we need to fill stack.

***

My code doesn't contain the complete code i.e there isn't code for making a new Node.

```python
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

```
It only have the main/core logic of the problem.
