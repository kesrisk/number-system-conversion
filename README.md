The Class Convert can convert

1- from Binary to Decimal
  - Method binary2decimal() will return the result directly

2- from Decimal to Binary
   - Method decimal2binary() will return the result directly
   
More methods can be added to this class such as Hexadecimal to binary, binary to octal, etc


``Creation of object``

con = Convert()

print(con.binary2decimal(111000), end = " ")

print(con.binary2decimal(10000), end = " ")

print(con.binary2decimal(100), end = " ")

print(con.decimal2binary(56), end = " ")

print(con.decimal2binary(6), end = " ")

print(con.decimal2binary(16), end = " ")

``Result would be``

56 16 4 111000 110 10000
