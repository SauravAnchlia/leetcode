'''
Given a non negative integer `num` , return the number of steps to reduce it to zero. 
If the current nuber is even you have to divide it by 2, otherwise , you have to subtract 1 from it.

Example:
num = 14
Output: 6 

'''

class solution:
    def number_of_steps_naive(self, num: int) -> int:
        flag = 0 
        while num != 0:
            print(num)
            if num%2==0:
                num>>=1
                flag+=1
            else:
                num-=1
                flag+=1
        return flag 


    def number_of_steps(self,num: int) -> int:
        count = 0 
        if num == 0:
            return 0 
        while num:
            print(f'num {num} , count {count}, shift {num>>1}')
            if num&1:
                count+=2
            else:
                count+=1
            num>>=1
        return count -1
        """
        count = 0 
        digit = f'{num:b}'
        count = digit.count('1')*2 + digit.count('0')
        return count å
        """
    def number_of_steps_bin(self,num: int) -> int:
        return bin(num).count("1") * 2 + bin(num).count("0") - 2
        d
obj = solution()
print(obj.number_of_steps(14))