class Test:

    # class variable
    x= 5
    def __init__(self,a,b):
        # self is instance object 
        self.a=a
        self.b=b
        # print(self)
    
    def show(self):
        print(self.a,self.b)
    @staticmethod
    def f1():
        print("i'm static method")
    
    @classmethod
    def f2(cls):
        # cls is class object
        print("i'm class method and my value = ",cls.x)


t1 = Test(10,20)
t2 = Test(20,30)
t1.show()
t2.show()
t1.f1()
t1.f2()
t2.f1()
t2.f2()
Test(45,56).show()
Test.f2()

