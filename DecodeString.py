class Solution:
    def decodeString(self, s: str) -> str:
        num = self.find_num(s)
        if num >= 0:
            new_str = self.resolve_string(s)
            print(new_str)
            return self.decodeString(new_str)
        else:
          return s
        
    
    
    def resolve_string(self, s: str):
        opening = self.find_opening(s)
        num = self.find_num(s)
        closing = self.find_closing(s)
        full_num = int(s[num:opening])
        
        mult_str = s[opening+1 : closing]
        mult_str = mult_str * full_num
        new_str = s[:num] + mult_str + s[closing+1:]
        return new_str
    
    
    def find_opening(self, s:str):
        return s.find('[')
    
    def find_closing(self, s_from_open: str):
        brack_count = 0
        for i in range(len(s_from_open)):
            c = s_from_open[i]
            if c == '[':
                brack_count += 1
            elif c == ']':
                brack_count -= 1
                if brack_count == 0:
                    return i
    
    def find_num(self, s):
        for i in range(len(s)):
            c = s[i]
            try:
                num = int(c)
                return i
            except ValueError:
                continue
        return -1
