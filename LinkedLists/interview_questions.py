# interview questions linked list
from nose.tools import assert_equal


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a

x = Node(5)
y = Node(6)
z = Node(7)
q = Node(8)
i = Node(10)

x.next_node = y
y.next_node = z
z.next_node = q
q.next_node = i


def check_cycle(node):

    if(node.next_node is None):
        return False

    else:
        pt1 = node
        pt2 = node

        while pt2 is not None and pt2.next_node is not None:
            pt1 = pt1.next_node
            pt2 = pt2.next_node.next_node
            if(pt1.value == pt2.value):
                return True
        return False


def reverse(head):
    if head is None:
        return
    if head.next_node is None:
        return head

    prev_node = head
    current_node = head.next_node

    while current_node.next_node is not None:
        next_node = current_node.next_node
        current_node.next_node = prev_node
        prev_node = current_node
        current_node = next_node

    print(current_node.value)
    return current_node.value


# class CycleTest(object):
#
#     def test(self, sol):
#         assert_equal(sol(x), False)
#         print("ALL TESTS PASSED")
#
#
# t = CycleTest()
# t.test(check_cycle)

# class reverseTest(object):
#
#     def test(self, sol):
#         assert_equal(sol(x), 10)
#         print("ALL TESTS PASSED")
#
#
# t = reverseTest()
# t.test(reverse)


def nth_to_last_node(n, head):
    if head is None:
        return
    if head.next_node is None:
        return head

    linkedListLen = 0
    current_node = head

    while current_node is not None:
        linkedListLen += 1
        current_node = current_node.next_node

    if (n > linkedListLen):
        return

    #start again
    current_node = head

    while n != linkedListLen:
        current_node = current_node.next_node
        n += 1
    return current_node.value

class nthNodeToLastTest(object):

    def test(self, sol):
        assert_equal(sol(6,x), "")
        print("ALL TESTS PASSED FOR NTH NODE")


t = nthNodeToLastTest()
t.test(nth_to_last_node)
