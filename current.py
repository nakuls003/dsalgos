from math import factorial as f


class Solution:

    def _rec_count(self, n, m):
        if n <= 1:
            return 1 if m == 0 else 0
        ans = 0
        for i in xrange(1, n + 1):
            temp = 0
            x, y = i - 1, n - i
            for h in xrange(m - 2):
                temp += self._rec_count(x, h) * self._rec_count(y, m - 1)
            for h in xrange(m - 2):
                temp += self._rec_count(y, h) * self._rec_count(x, m - 1)
            temp += self._rec_count(x, m - 1) * self._rec_count(y, m - 1)
            ans += temp * (f(x + y) / f(x) / f(y))
        return ans

    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, A, B):
        return self._rec_count(A, B)


if __name__ == '__main__':
    s = Solution()
    print(s.cntPermBST(3, 1))