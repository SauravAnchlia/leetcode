class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0 
        temp = 0 

        INT_MAX = 2**31-1
        INT_MIN = -2**31
        sign = 0 
        x=dividend<0
        y=divisor<0
        print(f"Dividend is less than 0 : {x}")
        print(f"Divisor is less than 0 : {y}")
        print(f'XOR is {x^y}')
        if( (dividend<0) ^ (divisor <0)):
            sign = -1 
        else:
            sign = 1       
        
        dividend = abs(dividend)
        divisor  = abs(divisor)
        print(sign)
        for power in range(31,-1,-1):
            if (temp + (divisor << power) <= dividend):
                temp += divisor<<power
                quotient = quotient | 1<<power 
        result = sign*quotient
        if result > INT_MAX or result<INT_MIN:
            return INT_MAX
        else:
            return result



    def divide_naive(self, dividend: int, divisor: int) -> int:
        quotient = 0 

        INT_MAX = 2**31-1
        INT_MIN = -2**31

        sign = 0
        if ((divisor<0) ^ (dividend<0)):
            sign = -1
        else:
            sign = 1
        divisor = abs(divisor)
        dividend = abs(dividend)

        while dividend>=divisor:
            dividend-=divisor
            quotient+=1

        solution = sign*quotient

        if solution>INT_MAX or solution<INT_MIN:
            return INT_MAX
        else:
            return solution




obj = Solution()
print(obj.divide(65,-7))
