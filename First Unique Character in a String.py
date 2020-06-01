from collections import Counter;
class Solution:
    def firstUniqChar(self, s: str):
        i=-1;
        d=dict(Counter(s));
        # print(d['l']);
        for index,char in enumerate(s):
            if(d[char]==1):
                i=index;
                break;
        return i;
print(Solution().firstUniqChar('ss'));

# o(n^2)
class Solution:
    def firstUniqChar(self, s: str):
        i=-1;
        # d=dict(Counter(s));
        # print(d['l']);
        for index,char in enumerate(s):
            if(s.count(char)==1):
                i=index;
                break;
        return i;
print(Solution().firstUniqChar('AAvv'));