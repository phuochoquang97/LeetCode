import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        components = re.split(r"(?=[+-])", expression)

        def find_common(num, de):
            while num != de:
                if num < de:
                    de = de - num
                else:
                    num = num - de

            return num

        numerator, denominator = 0, 1
        for com in components:
            if com == "":
                continue

            num, de = com.split("/")
            numerator = numerator * int(de) + denominator * int(num)
            denominator = denominator * int(de)

            if numerator == 0:
                denominator = 1
            else:
                common = find_common(abs(numerator), abs(denominator))
                numerator = numerator // common
                denominator = denominator // common

        return str(numerator) + "/" + str(denominator)
