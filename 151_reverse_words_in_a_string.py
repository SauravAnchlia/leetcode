class Solution:
    def reverse_words(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])