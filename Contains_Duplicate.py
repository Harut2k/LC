class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for i in nums:
            if(hashtable.get(i)):
                return True
            else:
                hashtable[i]='1'
        return False
