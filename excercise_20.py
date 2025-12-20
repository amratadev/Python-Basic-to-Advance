def mul(*numbers):
    c=1
    for i in numbers:
        c=c*i
    print(f"Mul is {c}.")
mul(2,3,-6,8)
mul(2,5,8,9,0,6)