class convert:
    def __init__(self):
        self.nb = 0
        self.nd = 0
        self.current_nb = 0
        self.current_nd = 0

    def d2b(self,n):
        if n == 0:
            return
        r = n%2
        self.d2b(n//2)
        self.nb = self.nb*10 + r

    def b2d(self, n, p):
        if n == 0:
            return
        r = n%10
        self.nd += ((2**p) * r)
        return self.b2d(n//10, p+1)


    def decimal2binary(self, n):
        self.d2b(n)
        self.current_nb = self.nb
        self.nb = 0
        return self.current_nb

    def binary2decimal(self, n):
        self.b2d(n, 0)
        self.current_nd = self.nd
        self.nd = 0
        return self.current_nd


A = convert()
print(A.binary2decimal(111000))
print(A.binary2decimal(10000))
print(A.binary2decimal(100))
print(A.decimal2binary(56))
print(A.decimal2binary(6))
print(A.decimal2binary(16))






