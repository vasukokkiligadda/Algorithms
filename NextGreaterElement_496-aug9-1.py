class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in findNums:
            for j in range(0,len(nums)):
                if i==nums[j]:
                    max=i
                    for k in range(j,len(nums)):
                        if nums[k]>max:
                            max=nums[k]
                            break
                    if max !=i:
                        l.append(max)
                    else:
                        l.append(-1)
        return l
                    
                
        
                
        