class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        ss = n*(n+1)//2
        s = sum(A)
        ss2 = n*(n+1)*(2*n+1)//6
        s2 = sum(n**2 for n in A)
        if s > ss:
            y = ((s2-ss2) - (s-ss)**2)//(2*(s-ss))
            x = (s - ss) + y
            return [x, y]
        else:
            y = ((ss2-s2) + (ss-s)**2)//(2*(ss-s))
            x = y - (ss - s)
            return [x, y]



if __name__ == '__main__':
    s = Solution()
    s.repeatedNumber([1, 2, 2, 3])
