"""
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

WARNING: This code works only in the hackerrans editor
cause they had already defined the SinglyLinkedList() function

SOLUTION:

loop on the LL until we reached to the desired position
then we create a new node using the data given to us.

Then we assign the next of the new node to the next
of the current and then we join the current's next to
the node.


current = current-> next
//make a new node
node = SinglyLinkedListNode(data)
// Now set this to current
node->next = current->next
// set current's next to node
current->next = node

return the head for the new LL
"""
def insertNodeAtPosition(head, data, position):
    pos = 0
    current = head

    while pos != position-1:
        current = current.next
        pos += 1
    
    node = SinglyLinkedListNode(data)
    node.next = current.next
    current.next = node
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
