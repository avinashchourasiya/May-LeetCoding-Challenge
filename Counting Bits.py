class Solution:
    def countBits(self, num: int):
        arr=[];

        for i in range(num+1):
            arr.append(bin(i)[2:].count('1'));
        print(arr)



Solution().countBits(5);

n=int(input());

print(str(n).count('1'));