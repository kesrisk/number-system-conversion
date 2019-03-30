class Convert:
    def __init__(self):
        self.__nb = 0
        self.__nd = 0
        self.__current_nb = 0
        self.__current_nd = 0

    def __d2b(self,n):
        if n == 0:
            return
        r = n%2
        self.__d2b(n//2)
        self.__nb = self.__nb*10 + r

    def __b2d(self, n, p):
        if n == 0:
            return
        r = n%10
        self.__nd += ((2**p) * r)
        return self.__b2d(n//10, p+1)


    def decimal2binary(self, n):
        self.__d2b(n)
        self.__current_nb = self.__nb
        self.__nb = 0
        return self.__current_nb

    def binary2decimal(self, n):
        self.__b2d(n, 0)
        self.__current_nd = self.__nd
        self.__nd = 0
        return self.__current_nd


A = Convert()
print(A.binary2decimal(111000))
print(A.binary2decimal(10000))
print(A.binary2decimal(100))
print(A.decimal2binary(56))
print(A.decimal2binary(6))
print(A.decimal2binary(16))






