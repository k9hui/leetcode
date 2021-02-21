class Solution:
    def reverse(self, x):

        str_x = str(abs(x))
        y = str_x[::-1]

        if 0<x<2**31-1:
            if int(y)<2**31-1:
                print(int(y))
                return int(y)
        elif 0>x>(-2**31):
            if int(y)<2**31-1:
                print(-int(y))
                return -int(y)
        else:
            print(0)
            return 0
if __name__=="__main__":
    so= Solution()
    # so.reverse(-123)
    so.reverse(1534236469)

            

            
