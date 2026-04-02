# Insert at Beginning
=====================
def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node