# Insert at End
===============
def insert_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node

    temp = head
    while temp.next:
