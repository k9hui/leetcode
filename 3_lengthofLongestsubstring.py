class Solution:
    def lengthOfLongestSubstring(self, s):
        del_count = set()
        n = len(s)
        k,ans = 0,0
        for i in range(n):
            if i != 0:
                del_count.remove(s[i-1])
            while k<n and s[k] not in del_count:
                del_count.add(s[k])
                k+=1
            ans = max(ans,k-i)
        return ans
                


class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}#abbcc
        i, ans = 0, 0
        #i表示与当前位置距离最大的下标
        for j, v in enumerate(s):
            if v in st:#当有重复元素得时候，更新i
                i = max(st[v], i)#这里i表示目前为止，相同v下标的最大值+1，比如abcba,当j=4(第二个a)的时候，i应该是第一个b的下标+1
            ans = max(ans, j-i+1)#max(之前的最大值,当前最大值)
            st[v] = j+1#记录当前值对应得value为下标加一，便于i的计算
        return ans#abbaacc

if __name__ == "__main__":
    so = Solution()
    len_s = so.lengthOfLongestSubstring('abbaacc')
    print(len_s)


v = 'aaaabbbcccccddddeeeeee'
'abcdefd'