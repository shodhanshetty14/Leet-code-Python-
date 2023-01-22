class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=1
        while(i<n):
            i=i*2
        return i==n

bot = Solution()
print(bot.isPowerOfTwo(1))
print(bot.isPowerOfTwo(16))
print(bot.isPowerOfTwo(5))
print(bot.isPowerOfTwo(3))