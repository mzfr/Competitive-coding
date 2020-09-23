## Remove duplicates from singly linked list

__URL__:: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

## Solution

This is a very simple problem. We have one linked list which is sorted now the benefit of sorted list is that if there are duplicates then they should be adjacent to each other.

Ex:  A sorted linked list would be

```
1 -> 2 -> 2 -> 3 -> 3 -> 4
```

As we see they are side to side so we just need to now do the following:

1) Loop over the list until we reach the end.
2) Inside the loop:
    - If value of current node is equal to value of next node, then
        - Change the pointer of current->next to currents->next->next
	    - Meaning in above example we see current node (2) and current -> next (2) is same so we just forgets the 3rd node and make the 2nd node point to
	      4th node
    - If the values are different then just increament the node i.e current node to current->next
3) Return the head

***

One thing to remember in this is not to increase the current node if the values were same, because when we are doing `current->next = current->next->next` that means the point is changing automatically.

***

__Code__

```python
def removeDuplicates(head):
    curr = head
    if curr is None:
        return head
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
```

Again if you want the full source then see the question link.
