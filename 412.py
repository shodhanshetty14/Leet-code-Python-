class Solution:
    def fizzBuzz(self, n: int):
        
        final_list = []
        for i in range(1, n+1):
            
            if i%3 == 0 and i%5 == 0:
                final_list.append("FizzBuzz")
            elif i%5 == 0:
                final_list.append("Buzz")   
            elif i%3 == 0:
                final_list.append("Fizz")
            else:
                final_list.append(str(i))
                
        return final_list


bot = Solution()
print(bot.fizzBuzz(3))
print(bot.fizzBuzz(5))
print(bot.fizzBuzz(15))