import math as m;
class Solution:
    def firstBadVersion(self, n):
        start=0;
        end=n;
        while(start<end):
            mid=m.ceil((start+end)/2);
            if(isBadVersion(version)):
                print(mid);
            else:
                firstBadVersion(n)
