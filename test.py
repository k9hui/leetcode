class Solution:
    def twoSum(self, nums, target):
        if len(nums)<=1:
            return []
        elif len(nums)==2:
            res = list(map(lambda x:target-x,nums)) #target与nums每一个元素做差，求出差集
            if res == nums:
                return [0,1]
        elif len(nums)>2:
            res = list(map(lambda x:target-x,nums))#target与nums每一个元素做差，求出差集
            same = [i for i in res if i in nums]
            print(same)
            if len(same)==2 and same[0]==same[1]:#如果差集的元素是俩个且俩个元素相同，获取他们的下标
                flag = 0
                lis = []
                for i in range(nums.count(same[0])):
                    sec = flag
                    flag = nums[flag:].index(same[0])
                    lis.append(flag + sec)
                    flag = lis[-1:][0] + 1
                print(lis)
                return lis
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

if __name__=="__main__":
    So = Solution()
    # So.twoSum([2,7,11,15],9)
    # So.twoSum([3,3],6)
    print(So.twoSum([4,2],6))
    # So.twoSum([3,2,3],6)