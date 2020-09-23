## Merge two sorted list

__URL__: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

## Solution

In this both of the list are SinglyLinkedList.

The solution would be simple, take another list then traverse the two given list and check if data of first is less then data of second, if yes then insert that node to the new list otherwise insert the other node to that new list.

```python
def mergeLists(head1, head2):
    p = head1
    q = head2
    r = SinglyLinkedListNode(0)
    h = r
    
    while p and q:
        if p.data < q.data:
            r.next = p
            p = p.next
        else:
            r.next = q
            q = q.next
        r = r.next
    
    if p:
        r.next = p
    if q:
        r.next = q
    return h.next
```

Here `SinglyLinkedListNode()` defines a new node. We basically started with one node and continued to add new nodes to it's `next` pointer.
