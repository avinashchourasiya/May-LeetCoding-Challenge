class Solution:
    def findMaxLength(self, nums):
        d={0:-1};
        d2=dict();
        c=0
        val=0
        m=0
        for index,num in enumerate(nums):
            if(num==0):c-=1;
            else:c+=1;
            if(c in d):
                val=index-d[c]
                m=max(m,val);

                # print(d2[c])
            else:
                d[c]=index
        #     if(c in d2):
        #         d2[c].append(index)
        #     else:
        #         d2[c] = [index]
        # print(d2)
        print(m)

Solution().findMaxLength([0,1,0,1,0,1,0]);