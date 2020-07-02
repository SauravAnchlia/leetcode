import re


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # lib_method =  address.replace('.', '[.]')
        # regex_method = re.sub('\.', '[.]', address)
        # str_method =  "[.]".join(address.split("."))
        return "[.]".join(address.split("."))

obj = Solution()
print(obj.defangIPaddr("1.1.1.1"))
