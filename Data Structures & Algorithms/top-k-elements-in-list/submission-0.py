class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_freq = {}

        for n in nums:
            if n in nums_freq:
                nums_freq[n] += 1
            else:
                nums_freq[n] = 1

        freq_sort = sorted(nums_freq.items(), key= lambda pair: pair[1], reverse=True )
        res = []

        for pair in freq_sort[:k]:
            res.append(pair[0])
        return res
            
