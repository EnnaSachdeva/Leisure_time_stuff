class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:

            if (element == '(') or (element == '[') or (element == '{'):
                stack.append(element)


            else:
                if(stack[-1] == '(' and element == ')') or (stack[-1] == '{' and element == '}') or (stack[-1] == '[' and element == ']'):
                    stack.pop()

                else:
                    return False


        if (len(stack)==0):
            return True
        else:
            return False

if __name__ == "__main__":
    func = Solution()
    number = func.isValid("()")
    print(number)





