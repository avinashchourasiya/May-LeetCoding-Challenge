class Solution:
    def findAnagrams(self, s: str, p: str):
        l = len(p);
        to=l-1;
        p = ''.join(sorted(p));
        d={p:[]};
        for i in range(0,len(s)-to):
            string=(''.join(sorted(s[i:l+i])))
            if(string in d):
                d[p].append(i);
        print(d[p])




s= "abab"; p= "ab"
Solution().findAnagrams(s,p);