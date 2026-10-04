class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return(0)
        while L<=R:
            mid = (L+R)//2
            if nums[mid] == target:
                    return(mid)
            if nums[L] == target:
                    return(L)
            if nums[R] == target:
                    return(R)
            if nums[mid]<nums[L]:
                if nums[mid]<target<nums[R]:
                    L = mid+1
                else:
                    R = mid
            else:
                if nums[L]<=target<nums[mid]:
                    R = mid
                else:
                    L = mid+1
        return(-1)




        