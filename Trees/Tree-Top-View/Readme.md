## Tree Top View

__URL__:: https://www.hackerrank.com/challenges/tree-top-view/problem

## Solution

For this we make a hashmap/dictionary which stores the data in the following format:

```json
{"dist":[value, level]}
```

Here:
* `dist` - is the vertical distance of nodes from the root.
* `level` - is the level of the node from the root.
* `value` - is the data value of each node.

Now we use this kind of dictionary along with the pre-order parsing of the code to get the top order. Here the vertical distance is used for indexing i.e if we come across a node with the same vertical distance then we check if it's level is higher or lower than current node. If it's lower then we replace it with the higher value.



## Code

```python
def topviewrecur(root, dist, level, hmap):
    """Take preorder and along with that fill in the 
    distance and level
    """
    if root is None:
        return
    
    ## Check the distance and level
    if dist not in hmap:
        hmap[dist] = [root.info, level]
    elif hmap[dist][1] > level:
        hmap[dist] = [root.info, level]
    
    # Similar to Preorder parsing
    # Going to the left subtree
    topviewrecur(root.left, dist-1, level+1, hmap)
    # Going to the right subtree
    topviewrecur(root.right, dist+1, level+1, hmap)
    
    
def topView(root):
    hmap = dict()
    topviewrecur(root, 0, 0, hmap)
    
    for _, V in sorted(hmap.items()):
        print(V[0], end=" ")
    
```
