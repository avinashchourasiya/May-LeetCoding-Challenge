# from collections import Counter;
# class Solution:
#     def majorityElement(self, nums):
#         d=dict();
#         old_max=0;
#         new_max=0;
#         key=0
#         for index,number in enumerate(nums):
#             if(number in d):
#                 d[number]+=1;
#             else:
#                 d[number]=1;
#
#             if(d[number] > old_max):
#                 key=number;
#                 old_max=d[number];
#         print(d);
#         print(key)
#
# Solution().majorityElement([3,3,4]);


from collections import Counter;
counts= {'george' : 16, 'amber' : 19};
print(counts)
print(max(counts.keys(), key=counts.get));
# print(key=counts.get);

