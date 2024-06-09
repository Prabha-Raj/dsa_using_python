class Recursion:
    def nNaturalNumbers(self,num):
        if num > 0:
            self.nNaturalNumbers(num-1)     # this line for first "N" natural number
            print(num,end=", ")
    def revNNaturalNumbers(self,num):
        if num > 0:
            print(num,end=", ") # this line for first "N" natural number
            self.revNNaturalNumbers(num-1)
    def nOddNumbers(self,num):
        if num > 0:
            self.nOddNumbers(num-1)
            print((2*num-1),end=", ") # this line for first "N" odd number
            # if num%2 == 1:           # this line for first "only" odd number
            #     print(num,end=", ") 
    def revNOddNumbers(self,num):
        if num > 0:
            print((2*num-1),end=", ") # this line for first "N" odd number
            # if num%2 == 1:        # this line for first "only" odd number
            #     print(num,end=", ")
            self.revNOddNumbers(num-1)
    def nEvenNumbers(self,num):
        if num > 0:
            self.nEvenNumbers(num-1)
            print((2*num),end=", ") # this line for first "N" even number
            # self.nEvenNumbers()
            # if num%2 == 0:    # this line for first 'only' even number
            #     print(num,end=", ") 
    def revNEvenNumbers(self,num):
        if num > 0:
            print((2*num),end=", ")  # this line for first "N" even number
            # if num%2 == 0:        # this line for first 'only' even number
            #     print(num,end=", ")
            self.revNEvenNumbers(num-1)
    def sumOfFirstNNumver(self,num):
        if num == 0:
            return 1
        return num+self.sumOfFirstNNumver(num-1)
    
    def sumOfFirstNOddNumver(self,num):
        if num == 1:
            return 1
        return (2*num-1)+self.sumOfFirstNOddNumver(num-1)
    def sumOfFirstNEvenNumver(self,num):
        if num == 0:
            return 0
        return (2*num)+self.sumOfFirstNEvenNumver(num-1)
    def factorial(self,num):
        if num == 1:
            return 1
        return num*self.factorial(num-1)
    def sumOfSquaresOfNumber(self,num):
        if num == 1:
           return 1
        return num*num + self.sumOfSquaresOfNumber(num-1)    # this line for first "N" natural number
    

recursion = Recursion()
print("Natural Numbers :")
recursion.nNaturalNumbers(10)
print("\nRevers of Natural Numbers :")
recursion.revNNaturalNumbers(10) 
print("\nOdd Number :")
recursion.nOddNumbers(10)
print("\nOdd Number In Reverce order:")
recursion.revNOddNumbers(10)
print("\nEven Number :")
recursion.nEvenNumbers(10)
print("\nEven Number In Reverce order:")
recursion.revNEvenNumbers(10)
result = recursion.sumOfFirstNNumver(10)
print("\nSum of First N Natural Numbers : ",result)
result1 = recursion.sumOfFirstNOddNumver(10)
print("Sum of First N Odd Natural Number :",result1)
result2 = recursion.sumOfFirstNEvenNumver(10)
print("Sum of First N Even Natural Number :",result2)
fact = recursion.factorial(5)
print("Factorial of a Number :",fact)
# recursion.sumOfSquaresOfNumber(3)
result3 = recursion.sumOfSquaresOfNumber(5)
print("Sum of squares of N Even Natural Number :",result3)
