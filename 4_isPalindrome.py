class Solution:
    def isPalindrome(self, x):
        if (-2**31)<=x<=2**31-1:
            if x<0:
                return False
            else:
                s = str(x)
                n = len(s)
                res = n//2
                print(res,type(res))
                if n%2==0:
                    sub_1 = s[0:res]
                    sub_2 = s[res::][::-1]
                    if sub_1 == sub_2:
                        return True
                    else:
                        return False
     
                else:
                    sub_1 = s[0:res]
                    print(sub_1)
                    sub_2 = s[(res+1)::][::-1]
                    print(sub_2)
                    if sub_1 == sub_2:
                        return True
                    else:
                        return False

if __name__=="__main__":
    so = Solution()
    res = so.isPalindrome(-122)
    print(res)
 