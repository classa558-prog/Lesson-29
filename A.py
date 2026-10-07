class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        return self.a < other.a
    def __eq__(self, other):
        return self.a == other.a
a = A(3)
a1 = A(5)
print(a1 > a)
print(a < a1)      
print(a == a1)      
         
      