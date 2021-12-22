class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(' ')
        sortd = [0 for x in s_list]
        for each in s_list:
            sortd[int(each[-1]) - 1] = each[0:len(each)-1]

        sortd_str = ''
        for every in sortd:
            sortd_str += f' {every}'
        sortd_str = sortd_str.strip()
        return sortd_str
        
