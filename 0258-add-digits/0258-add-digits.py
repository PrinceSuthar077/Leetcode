class Solution:
    def addDigits(self, num):
       
      while num >=10:
         i = num // 10
         j = num % 10
         num = i + j
      return num
