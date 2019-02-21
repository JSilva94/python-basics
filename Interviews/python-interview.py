def anagram(s1, s2):
    s1_joined = s1.replace(' ', '')
    s2_joined = s2.replace(' ', '')
    if len(s1_joined) != len(s2_joined):
        return False
    for i in s1_joined:
        if i not in s2_joined:
            return False
        else:
            s2_joined.replace(i, '')
    return True


print(anagram('clint eastwotod', 'old westt action'))


def pair_sum(lst, k):
    dic = {}
    pairs = []
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in lst:
        if i in dic and (k-i) in dic:
            dic[k-i] -= 1
            dic[i] -= 1
            pairs.append((i, k-i))
            if dic[k-i] == 0:
                del dic[k-i]
    print(pairs);
    return len(pairs)


print(pair_sum([1, 3, 4, 6, 2, 8, 2, 0, -2, 4], 4))


def finder(l1, l2):
    max_list = []
    min_list = []
    if len(l1) > len(l2):
        max_list = l1
        min_list = l2
    else:
        max_list = l2
        min_list = l1 
    for i in max_list:
        if i not in min_list:
            return i
        else:
            min_list.remove(i)

def larg_cont_sum(lst):
    largest = lst[0]
    current_total = 0
    for i in lst:
        if current_total < 0 and current_total + i > 0:
            current_total = i
        else:
            current_total +=i
        largest = max(largest, max(current_total, i))
    return largest

print(larg_cont_sum([-2, -3, -1, -6, -5]))

def reversal(s):
    s = s.lstrip().rstrip().split(' ')
    reversed_str = ''
    for i in s[::-1]:
        reversed_str += i + ' '
    return reversed_str
print(reversal(' i dont j jnwoo what im doing'))

def str_compression(s):
    compressed_str = ''
    if len(s) == 0:
        return compressed_str
    current_letter = s[0]
    current_count = 1
    for i in s[1:]:
        if i != current_letter:
            compressed_str += current_letter + str(current_count)
            current_letter = i
            current_count = 1
        else:
            current_count +=1

    compressed_str += current_letter + str(current_count)
    return compressed_str


print(str_compression('AAAABBBBCCCCCccccdd'))

def uni_char(s):
    if len(s) == 0 or len(s) == 1:
        return True
    uni_dic = {}

    for i in s:
        if i in uni_dic:
            return False
        uni_dic[i] = 1

    return True
a = set('abcdee')
print(a)
print(uni_char('abcdee'))


class Queue2Stacks():
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, ele):
        self.in_stack.append(ele)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


q2s = Queue2Stacks()

for i in range(5):
    q2s.enqueue(i)

for i in range(i):
    print(q2s.dequeue())

    
