# A linked list is a sequence of data structures, which are connected together via links. Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked is empty")
            return
        # itr = current node, itr.next = next node of current node
        itr = self.head
        llstr = ''
        while itr is not None:
            llstr += str(itr.data) + '---->'
            itr = itr.next

        print(llstr)

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def count_nodes(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter

    def remove_node(self, index):
        if index < 0 or index > self.count_nodes():
            raise Exception(" Out of bound index")

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            counter += 1

    def insert_value_at(self, index, data):
        if index < 0 or index > self.count_nodes():
            raise Exception(" Out of bound index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_values(["vadapav", "samosa", "chutney", "dosa", "chowmin"])
    llist.print()
    llist.count_nodes()
    print("Total nodes = ", llist.count_nodes())
