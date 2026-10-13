class Solution(object):
    def fizzBuzz(self, n):
        l = []

        for i in range(1,n+1):
            l.append(i)

        for i in range(len(l)):
            if l[i] % 3 == 0 and l[i] % 5 == 0:
                l[i] = "FizzBuzz"
            elif l[i] % 3 == 0:
                l[i] = "Fizz"
            elif l[i] % 5 == 0:
                l[i] = "Buzz"
        
        for i in range(len(l)):
             l[i] = str(l[i])

        return  l      
