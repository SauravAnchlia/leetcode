class solution:
    def myatoi(self, str: str) -> int:

        INT_MAX = 2**31-1
        INT_MIN = -2**31

        result = ""
        sign = ""
        str = str.strip()
        if not str:
            return 0
        first_val = str[0]
        if first_val in ['+', '-']:
            sign = first_val
        elif first_val.isnumeric():
            result += first_val
        else:
            return 0

        for char in str[1:]:
            if char.isnumeric():
                result += char
            else:
                break

        if not result:
            return 0
        if sign == '-':
            result = int(result)*-1
        else:
            result = int(result)

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result


obj = solution()
print("ANS {0}".format(obj.myatoi(".12")))


          

          
