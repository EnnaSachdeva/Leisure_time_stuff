class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0
        print(s)
        stack.append(s[0])

        for i in s[1:]:
            if len(stack) > 0:
                if ((stack[-1] == 'R' and i == 'L') or (stack[-1] == 'L' and i == 'R')):
                    stack.pop()
                    if len(stack) == 0:
                        count += 1

                else:
                    stack.append(i)

            else:
                stack.append(i)

        return count



m = Solution()
print(m.balancedStringSplit("RLRRRLLRLL"))