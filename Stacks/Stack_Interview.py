# stacks/queues/deques interview questions

from nose.tools import assert_equal


def balance_check(s):

    if(len(s) == 0):
        return True
    if(len(s) % 2 != 0):
        return False

    opening = set('({[')

    matches = set([('{', '}'), ('(', ')'), ('[', ']')])

    stack = []

    for bracket in s:
        if bracket in opening:
            #only append opening brackets,
            #then pop then one by one to check if it matches.
            #this acts as a stack

            stack.append(bracket)

        else:
            if(len(stack) == 0):
                return False

            else:
                last_open = stack.pop()
                if (last_open, bracket) not in matches:
                    return False
    return True


class BalanceTest(object):

    def test(self, sol):
        assert_equal(sol('{[({})]}'), True)
        assert_equal(sol(''), True)
        assert_equal(sol('{[}'), False)
        assert_equal(sol('{[([)]]}'), False)
        assert_equal(sol('}{'), False)
        print('all test casses passed!!!')


t = BalanceTest()
t.test(balance_check)


class Queue2Stacks(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, ele):
        self.stack1.append(ele)


    def dequeue(self):
        # stack2 is empty

        stack1len = len(self.stack1)
        for i in range(stack1len):
            self.stack2.append(self.stack1.pop())
        ele_popped = self.stack2.pop()
        stack2len = len(self.stack2)

        # put it back to stack1 it was
        for i in range(stack2len):
            self.stack1.append(self.stack2.pop())
        return ele_popped


q = Queue2Stacks()
for i in range(5):
    q.enqueue(i)
print(q.stack1)
print(q.stack2)
for i in range(5):
    print(q.dequeue())
