class Solution:
    def findComplement(self, num: int):
        bn=list(bin(num)[2:]);
        print(bn);
        for index,bit in enumerate(bn):
            if(bit=='0'):
                bn[index]='1';
            else:
                bn[index] = '0';
        return(int(''.join(bn),2))

print(Solution().findComplement(5));

