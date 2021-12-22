class Solution: 
    def select(self, arr, i):
        least = i
        for each in range(i+1, len(arr)):
            if arr[each] < arr[least]:
                least = each
        return least
    def selectionSort(self, arr,n):
        for every in range(n):
            least = self.select(arr, every)
           
            arr[every], arr[least] = arr[least], arr[every]
            
        return arr