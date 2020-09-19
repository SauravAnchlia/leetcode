from collections import Counter


class Solution:
    def isNumber(self, s: str) -> bool:
        import pdb; pdb.set_trace()
        seen_deci, seen_e, seen_digit = False, False, False
        for index, item in enumerate(s.strip()):
            if item in ['-','+']:
                if index > 0 and s.strip()[index - 1] != 'e':
                    return False
            elif item == '.':
                if seen_e or seen_deci:
                    return False
                seen_deci = True
            elif item == 'e':
                if seen_e or not seen_digit:
                    return False
                seen_e = True 
                seen_digit = False
            elif item.isdigit():
                seen_digit = True
            else:
                return False
        return seen_digit

obj = Solution()
print(obj.isNumber(" 005047e+6"))
print(obj.isNumber('2e0'))
