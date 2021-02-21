class Solution:
    def twoSum(self, nums, target):
        if len(nums)<=1:
            return None
        res = list(map(lambda x:target-x,nums[:]))
        print(res)
        
        if len(nums)==2:
            # res = list(map(lambda x:target-x,nums[:]))
            if len(res)==2:
                print([0,1])

        if  len(nums)>2: 
            li = [nums.index(i) for i in res if i in nums]
            # li = [[i,nums.index(res[i])] for i in range(len(res)) if res[i]in nums[1:]]

            print(li[::-1])
            # ress = []]]
            

if '__main__'==__name__:
    solution = Solution()
    # solution.twoSum([2,7,11,15],9)
    # solution.twoSum([3,3],6)
    solution.twoSum([3,2,4],6)

    


        # print(1)