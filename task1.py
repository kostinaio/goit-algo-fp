

# Реалізація однозв'язного списку

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Функція реверсування однозв'язного списку

def reverse_linked_list(llist):
    prev = None
    current = llist.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    llist.head = prev

# Алгоритм сортування однозв'язного списку методом злиття

def merge_sort_linked_list(llist):
    if llist.head is None or llist.head.next is None:
        return llist

    def get_middle(node):
        if node is None:
            return node
        slow = node
        fast = node
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = sorted_merge(left.next, right)
        else:
            result = right
            result.next = sorted_merge(left, right.next)
        return result

    def merge_sort(node):
        if node is None or node.next is None:
            return node
        middle = get_middle(node)
        next_to_middle = middle.next
        middle.next = None
        left = merge_sort(node)
        right = merge_sort(next_to_middle)
        sorted_list = sorted_merge(left, right)
        return sorted_list

    llist.head = merge_sort(llist.head)
    return llist

# Функція для об'єднання двох відсортованих однозв'язних списків

def merge_two_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Тестування

# Створення списку
llist = LinkedList()
llist.insert_at_end(5)
llist.insert_at_end(3)
llist.insert_at_end(8)
llist.insert_at_end(2)
llist.insert_at_end(4)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Реверсування зв'язного списку
reverse_linked_list(llist)
print("Реверсований зв'язний список:")
llist.print_list()

# Сортування зв'язного списку методом злиття
merge_sort_linked_list(llist)
print("Відсортований зв'язний список:")
llist.print_list()

# Створення двох відсортованих списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

# Об'єднання двох відсортованих списків
merged_list = merge_two_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
