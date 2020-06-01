class Solution:
    def numJewelsInStones(self, J: str, S: str):
        c=0;
        for index,char in enumerate(S):
            if(char in J):
                c+=1
        return c;
        # print(c);
ans=Solution().numJewelsInStones('aA','aAAbbbb');


print(ans);




