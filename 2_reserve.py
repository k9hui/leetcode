class Solution:
    def reverse(self, x):
        if -2**31 <= x <= 2**31 - 1:
            y = str(abs(x))
            re_x = y[::-1]
            if -2**31 <= int(re_x) <= 2**31 - 1:
                if x >= 0:
                    return int(re_x)
                if x < 0:
                    return -int(re_x)
            else:
                return 0
        else:
            return 0


if __name__ == '__main__':
    so = Solution()
    res = so.reverse(1534236469)
    # res = so.reverse(123)
    print(res)
