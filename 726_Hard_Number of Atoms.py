class Solution:
    def splitAndCount(self, formula: str):
        # Regex pattern to match elements and counts
        pattern = re.compile(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)")

        # Stack to handle nested groups
        stack = [defaultdict(int)]

        print(pattern.findall(formula))

        for element, count, open_paren, close_paren, multiplier in pattern.findall(
            formula
        ):
            if element:
                count = int(count) if count else 1
                stack[-1][element] += count
            elif open_paren:
                stack.append(defaultdict(int))
            elif close_paren:
                group = stack.pop()
                multiplier = int(multiplier) if multiplier else 1
                for elem, cnt in group.items():
                    stack[-1][elem] += cnt * multiplier

        # The final counts are in the last item of the stack
        return dict(stack.pop())

    def countOfAtoms(self, formula: str) -> str:
        ret = self.splitAndCount(formula)

        ret_str = ""
        for key in sorted(ret):
            ret_str += key
            if ret[key] > 1:
                ret_str += str(ret[key])

        return ret_str
