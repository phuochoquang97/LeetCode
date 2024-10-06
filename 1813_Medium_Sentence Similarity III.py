class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        case 1: s1 = a b c, s2 = a _ _ _ b c
        case 2: s1 = a b c, s2 = a b c _ _ _
        case 2: s1 = a b c, s2 = _ _ _ a b c
        """
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        n1 = len(s1)
        n2 = len(s2)

        if n1 <= n2:
            l = s2
            s = s1
        else:
            l = s1
            s = s2

        # case 2 and 3
        if s == l[: len(s)] or s == l[len(l) - len(s):]:
            return True

        # case 1 -> O(N)
        for i in range(1, len(s)):
            if s[:i] == l[:i]:  # first match
                if s[i:] == l[(len(l) - len(s[i:])):]:  # check second match
                    return True

        return False
