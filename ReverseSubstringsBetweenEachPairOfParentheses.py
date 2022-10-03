class Solution:
    ans = ''
    par_count = 0
    def reverseParentheses(self, s: str) -> str:
        inner = self.findInner(s)
        if inner:
            self.ans = s[0: inner[0]] + s[inner[0] + 1: inner[1] - 1][::-1] + s[inner[1]:]
            return self.reverseParentheses(self.ans)
        
        if self.par_count:
            return self.ans
        else:
            return s

    def findInner(self, inner : str) -> str:
        inner_par = False
        for index, character in enumerate(inner):
            if character == '(':
                self.par_count += 1
                inner_par = [0,0]
                inner_par[0] = index
            elif character == ')':
                inner_par[1] = index + 1
                break

        return inner_par