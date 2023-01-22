class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        array = set()
        for i in arr:
            for x in arr:
                if x-i == difference:
                    array.add(i)
                    array.add(x)
                    print(x,i)
        print(array)
        if len(array) == 0:
            return 1
        return len(array)


bot = Solution()
print(bot.longestSubsequence([1,2,3,4], 1))
print(bot.longestSubsequence([1,5,7,8,5,3,4,2,1], -2))