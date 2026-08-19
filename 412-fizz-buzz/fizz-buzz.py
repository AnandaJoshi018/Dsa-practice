class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                res = "FizzBuzz"
                ans.append(str(res))
            elif i % 3 == 0:
                res = "Fizz"
                ans.append(str(res))
            elif i % 5 == 0:
                res = "Buzz"
                ans.append(str(res))
            elif i == i:
                res = i
                ans.append(str(res))
        return ans
