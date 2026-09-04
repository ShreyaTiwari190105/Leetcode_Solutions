class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n 
        
        sum = 0
        product = 1

        while n > 0:
            digit = n % 10
            sum += digit
            product *= digit
            n = n // 10

        divisor = sum + product

        if num % divisor == 0:
            return True

        else:
            return False
