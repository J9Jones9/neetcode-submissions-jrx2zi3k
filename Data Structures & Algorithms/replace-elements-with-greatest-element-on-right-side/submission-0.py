class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        curGreatest = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = curGreatest
            curGreatest = max(temp, curGreatest)


       
        return arr

