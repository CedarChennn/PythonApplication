import unittest

class Test_test1(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        look = set()
        lf = 0
        ml=0
        cl=0
        n=len(s)
        for i in range(s):
            cl+=1
            while(s[i] in look):
                look.remove(s[i])
                lf+=1
                cl-=1
            if(ml<cl):ml=cl
            look.add(s[i])
        return ml

def main():
    print("hy ")
if __name__ == '__main__':
    main()