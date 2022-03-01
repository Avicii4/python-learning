class Solution:
    def find_LUS_length(self, a: str, b: str) -> int:
        """
        若两个串完全一样，则没有独特的子串，返回-1；
        除此以外，较长的串本身是独特的子串，因为较短的串不可能包含
        """
        if a == b:
            return -1
        return max(len(a), len(b))
