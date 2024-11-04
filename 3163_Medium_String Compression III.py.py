class Solution:
    def compressedString(self, word: str) -> str:
        current_char = word[0]
        current_count = 0
        ret = ""
        for i, c in enumerate(word):
            if c == current_char:
                current_count += 1
                if current_count == 9:
                    ret += "9" + c
                    current_count = 0
            else:
                # append prev before updating current
                if current_count > 0:
                    ret += str(current_count) + current_char
                current_char = c
                current_count = 1

        # updating with last round
        if current_count > 0:
            ret += str(current_count) + current_char
        return ret
