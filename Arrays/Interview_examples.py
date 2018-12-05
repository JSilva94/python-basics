# ANAGRAM PROBLEM
import platform
from nose.tools import assert_equal


def anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    d1 = {}
    d2 = {}

    for i in s1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1

    for k in s2:
        if k not in d2:
            d2[k] = 1
        else:
            d2[k] += 1

    if d1 == d2:
        print("TRUE")
        return True
    else:
        print('FALSE')
        return False


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi       man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print('all test casses passed!!!')


t = AnagramTest()
t.test(anagram)


def pair_sum(arr, k):

    #use sets next time!!

    if len(arr) < 2:
        return 0
    new_dic = {}
    pairs_arr=[]
    for i in arr:
        if i not in new_dic:
            new_dic[i]=1;
        else:
            new_dic[i]+=1

    for i in arr:
        if k-i in new_dic: #check if what is needed to sum to k is in new_dic
            if new_dic[k-i] == 1: # only one entry
                del new_dic[k-i]
            else:
                new_dic[k-i] -=1
            if i in new_dic:
                if new_dic[i]==1:
                    del new_dic[i]
                else:
                    new_dic[i]-=1
                pairs_arr.append((i,k-i))

    print(pairs_arr)
    return len(pairs_arr)

class TestPair(object):

    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 11, 14, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('all test casses passed for testpair!!!')


testpair = TestPair()
testpair.test(pair_sum)




#missing number PROBLEM

def finder(arr1,arr2):
    dic={}
    for i in arr2:
        if i not in dic:
            dic[i]=1;
        else:
            dic[i]+=1

    for k in arr1:
        if k in dic:
            dic[k]-=1
            if dic[k] < 0:
                return k
        else:
            return k





class TestFinder(object):

    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('All test cases passed for testFinder !!!!!')


#Run Test
t=TestFinder()
t.test(finder)


#largest continuous sum

def large_cont_sum(arr):
    if(len(arr)==0):
        return 0
    largest = arr[0]
    current_sum = arr[0]
    for sum in arr[1:]:
        current_sum = max(current_sum+sum,sum)

        largest = max(current_sum, largest)

    return largest



class LargeContTest(object):

    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-2,-1,1,10,10,-10,-1]),21)
        assert_equal(sol([1,-1]),1)
        print('All CASES PASSED --- largesum')


#Run Test
t=LargeContTest()
t.test(large_cont_sum)


def rev_word(str):
    arr_split = str.split()

    revstr=""
    for i in arr_split[::-1]:
        revstr += i + " ";
    revstr = revstr[:-1]
    return revstr

class ReverseStringTest(object):

    def test(self,sol):
        assert_equal(sol("hello there my name is jayde"),"jayde is name my there hello")
        assert_equal(sol("abcdef"),"abcdef")
        assert_equal(sol("    hello there "),"there hello")
        assert_equal(sol(""),"")
        print('All CASES PASSED --- reverse')


#Run Test
t=ReverseStringTest()
t.test(rev_word)

def str_comp(letters):
    if len(letters) == 0:
        return ""
    letter = letters[0]
    compressed_str = letter
    count = 1

    if letters == " ":
        return " "
    if len(letters) == 1:
        return letter + "1"

    for i in letters[1:]:
        if i == letter:
            count +=1
        else:
            compressed_str += str(count) + i
            count =1
            letter = i
    return compressed_str + str(count)



class CompressStringTest(object):

    def test(self,sol):
        assert_equal(sol(" ")," ")
        assert_equal(sol(""),"")
        assert_equal(sol("AABBCCDDDDDDDFFFFFF"),"A2B2C2D7F6")
        assert_equal(sol("AAABCCDDDDD"),"A3B1C2D5")
        assert_equal(sol("AAaaB"),"A2a2B1")
        print('All CASES PASSED --- compress')


#Run Test
t=CompressStringTest()
t.test(str_comp)

def unique_char(s):
    dic = {}
    for k in s:
        if k not in dic:
            dic[k]=1
        else:
            return False
    return True


class UniqueStringTest(object):

    def test(self,sol):
        assert_equal(sol(" "),True)
        assert_equal(sol(""),True)
        assert_equal(sol("AABBCCDDDDDDDFFFFFF"),False)
        assert_equal(sol("abcderr"),False)
        assert_equal(sol("abcdfghjt"),True)
        print('All CASES PASSED --- unique')


#Run Test
t=UniqueStringTest()
t.test(unique_char)
