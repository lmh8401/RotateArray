class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len (nums)                    #计算移动位置数 k 比数组nums长度的余数
        for _ in range (k) :                 #数组nums中所有元素向右移动k个位置
            nums.insert (0, nums.pop()) 

