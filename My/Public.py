class Solution(object):
    def reversePairs(self, nums):
        self.Ans = 0
        self.divide(nums, 0, len(nums) - 1)

        return self.Ans
    
    def divide(self, nums, left, right):
        if(left < right):
            mid = (left+right) // 2
            
            self.divide(nums, left, mid)
            self.divide(nums, mid + 1, right)
            self.merge(nums, left + mid, right)

    def merge(self, nums, left, right):
        if(nums[left] > nums[right]):
            if(nums[left] > nums[right] * 2):
                self.Ans += 1
            nums[left], nums[right] = nums[right], nums[left]
        
        


Ex = Solution()
print(Ex.reversePairs([2, 4, 3, 5, 1]))


"""
0 <= i < j < len(nums)

i값이 큰 값일 때, j값의 2배보다 큰 경우가 있다면 RP++
중복을 허용하지 않으므로, Set자료형을 사용한다.

"""