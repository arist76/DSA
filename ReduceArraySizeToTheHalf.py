class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr)/2
        arr_count  = Counter(arr)
        summation = 0
        counter = 0
        for i in arr_count.most_common():
            summation += i[1]
            counter += 1
            if summation >= half:
                break
            else:
                continue
        return counter
