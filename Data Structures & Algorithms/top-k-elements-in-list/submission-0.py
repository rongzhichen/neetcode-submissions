class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save  = {}
        for i in range(len(nums)):
            if nums[i] not in save:
                save[nums[i]] = 1
            else:
                save[nums[i]]+=1
        sol = []
        for i in range(k):
            ans_key = max(save, key = save.get)
            sol.append(ans_key)
            save[ans_key] = -1
        return(sol)
            
        