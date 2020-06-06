'''
Given a non negative integer `num` , return the number of steps to reduce it to zero. 
If the current nuber is even you have to divide it by 2, otherwise , you have to subtract 1 from it.

Example:
num = 14
Output: 6 

'''


class solution:
    '''
    In this approach, increment the flag depending on divisibility by two.
    '''
    def number_of_steps_naive(self, num: int) -> int:
        flag = 0
        while num != 0:
            if num % 2 == 0:
                num >>= 1
                flag += 1
            else:
                num -= 1
                flag += 1
        return flag

    '''
    Even number in bit example :
        2 -> (10)
        4 -> (100)
        6 -> (110)
    This shows the pattern that that the last place will always be 0.
    So even number '&' 1 will always be 0. Slighly faster than mod of 2.
    '''
    def number_of_steps(self, num: int) -> int:
        count = 0
        if num == 0:
            return 0
        while num:
            if num & 1:
                count += 2
            else:
                count += 1
            num >>= 1
        return count - 1

    '''
    Convert the number to a binary format string.
    Example :
        14 -> 1110
    we subtract by 2 because the string format adds an extra 0.
    secondly, the last step to reduce 1 to 0 i.e 0001 -> 0000
    that's just one step.

    For every 1, we have 2 activity (subtract 1 , divide 2)
    For every 2, we do 1 activity (divide by 2)
    '''
    def number_of_steps_count_string(self, num: int) -> int:
        count = 0
        digit = f'{num:b}'
        count = digit.count('1')*2 + digit.count('0')
        return count - 2

    def number_of_steps_bin(self, num: int) -> int:
        return bin(num).count("1") * 2 + bin(num).count("0") - 2
