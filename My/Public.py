class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
     # idx
     Ans = self.createTree(nums, 0, len(nums) - 1)
     
     return Ans

    def createTree(self, nums, start, end):
        if(start > end):
            return None
        mid = (start + end) // 2

        temp = TreeNode(nums[mid])
        temp.left = self.createTree(nums, start, mid - 1)
        temp.right = self.createTree(nums, mid + 1, end)

        return temp


tree = Solution()

print(tree.sortedArrayToBST([-10, -3, 0, 5, 9]))

                        
"""
mid_idx를 집어넣고 
mid까지 nums를 넣기
mid이후 nums를 넣기

"""