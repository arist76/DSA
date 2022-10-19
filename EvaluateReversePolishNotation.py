class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cache = []
        ans = 0
        for token in tokens:
            if token in ["+", "-", "/", "*" ]:
                first = cache.pop()
                second = cache.pop()
                if token == "+":
                    cache.append(second + first)
                if token == "-":
                    cache.append(second - first)
                if token == "*":
                    cache.append(second * first)
                if token == "/":
                    cache.append(int(second/first))
            else:
                cache.append(int(token))        
        return cache[0]
