class Solution:
    def twoSum(self, nums, target):
        if len(nums)<=1:
            return []
        elif len(nums)==2:
            if nums[0]+nums[1]==target:
                return [0,1]
        elif len(nums)>2:
            res = list(map(lambda x:target-x,nums))#target与nums每一个元素做差，求出差集
            same = [i for i in res if i in nums]
            print(same)
            if len(same)==2 and same[0]==same[1]:#如果差集的元素是俩个且俩个元素相同，获取他们的下标
                li = [i for i,x in enumerate(nums) if x == same[0]]
                return li
            # 获取下标
            else:
                for i in same:#如果差集的元素不同，获取他们的下标
                    temp = []
                    n_index = nums.index(i)
                    r_index = res.index(i)
                    if n_index!=r_index:
                        temp.append(r_index)
                        temp.append(n_index)
                        print(temp)
                        return temp

def getindex(nums,target):
    flag = 0
    li=[]
    for index,item in enumerate(nums):
        sec = flag
        flag = nums[flag:].index(target)
        li.append(flag + sec)
        flag = li[-1:][0] + 1
    return li
class Solution1:
    def twoSum1(self, nums, target):
        lst = [i for i,v in enumerate(nums) if target-v in nums[i+1:]]
        if len(lst) == 1:
            lst.append(lst[0]+1+nums[lst[0]+1:].index(target-nums[lst[0]]))
        return lst

if __name__=="__main__":
    # So = Solution()
    # So.twoSum([2,7,11,15],9)
    # So.twoSum([3,3],6)
    # So.twoSum([3,2,4],6)
    # So.twoSum([3,2,3],6)
    li_a = [1,2,3]
    li_b=[2,2]
    same=[2,2]
    index_b = [i for i, x in enumerate(li_b) if x==same[0]]
    print(li_a[-1:][0])
    # if li_a == li_b:
    #     print(True)
            


            
            
        
