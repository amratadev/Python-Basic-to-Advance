a = 2   # binary: 10
b = 4   # binary: 100
#100=(1*2^2)+(0*2^1)+(0* 2^0)=4+0+0=4

print(a >> 1)   # right shift
print(a << 1)   # left shift
print(a & b)    # AND
print(a | b)    # OR
print(a ^ b)    # XOR
print(~b)