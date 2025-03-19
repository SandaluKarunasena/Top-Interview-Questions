class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        newStr=""
        for i in s:
            if i.isdigit():
                newStr+=i
            elif (newStr == '') and (i == "+" or i == "-"):
                newStr+=i
            else:
                break

        if newStr == '' or newStr in '-+':
            return 0

        result = max(-2**31, min(int(newStr), 2**31 - 1))

        return int(result)
