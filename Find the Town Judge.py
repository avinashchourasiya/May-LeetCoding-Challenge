
class Solution:
    def findJudge(self, N, trust):
        d=dict();
        tj=-1
        for index,num in enumerate(trust):
            a,b=trust[index];
            if(a in d):
                d[a]+=1;
            else:d[a]=1;
        for i in range(1,N+1):
            if(i not in d):
                tj=i

        print(d);
        print(tj)

N = 3; trust = [[1,2],[2,3]];
Solution().findJudge(N,trust)
