class Solution:
    def countAndSay(self, n: int) -> str:
        def rle_encoding(inp: str) -> str:
            prev = None
            current_count = 0
            ret = ""

            for i in range(len(inp)):
                if prev is None:
                    prev = inp[i]
                    current_count = 1
                    continue

                if inp[i] == prev:
                    current_count += 1
                    continue
                else:
                    ret += str(current_count) + prev
                    current_count = 1
                    prev = inp[i]

            ret += str(current_count) + prev
            return ret

        ret = "1"
        for i in range(1, n):
            ret = rle_encoding(ret)
            # print(f"ret = {ret}")
        return ret
