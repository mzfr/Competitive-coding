## Reverse a doubly linked list

__URL__:: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

## Solution

The idea behind reversing a doubly linked list is very simple. There are 3 things in double linked list, previous, a next and data/value.

Now this is what we do:

1) Take two variables, 1 temporary and another one called `current` which basically is a copy of `head`.
2) Look till current is not `None`.
3) Inside loop do the following:
    - Move previous value of current node to temporary location.
    - Point the current previous to the next of the current node.
    - Move data of temp to current next.
    - change the current node to another node.
    - In the end check if temp is null or not
    	- If not then set current head to previous of null
4) Return `head`

***

It's important to check if the temp variable is null or not. To understand why just try to reverse a doubly linked list with single node(even though it doesn't make sense but just try it)

***

__Source code__

```python
def reverse(head):
    temp = None
    current = head
    
    while current:
        temp = current.prev # We hold the previous value
        current.prev = current.next # this way we exchange prev and next
        current.next = temp # change the pointing process
        current = current.prev # move to next node
    if temp:
        head = temp.prev # in case the list was empty or had only one node
    return head
```

This is just the main code, if you want the full source then visit the URL in the starting of this readme.
