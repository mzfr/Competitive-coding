## Cycle Detection

__URL__:: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

## Solution

This is also an easy problem  the only important thing to remember in this is that it's not an array but a linked list. I am saying this because initially I wrote a code where I had a counter and was increasing it's value everytime I'd get a cycle but then I realized that in linked list there will be one cycle.

So the real question is either to send `yes` or `no`.

The solution that I used consumes `O(n)` space, because I made a list of all the visited nodes and if I encounted a visited node again that means there is a cycle so return 1.

```python
def has_cycle(head):
    curr = head
    visited = []
    while curr:
        if curr in visited:
            return 1
        visited.append(curr)
        curr = curr.next
    return 0
```
