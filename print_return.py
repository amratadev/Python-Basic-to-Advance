def func1(a,b):
    c=a+b
    print(c)
output1=func1(5,2)
print(output1)

def func2(a,b):
    c=a+b
    return c
output2=func2(3,4)
func1(output2,0)
print(output2)

def func3(x):
    return x+1
def func4(a,b):
    c=a+b
    return c
output3=func4(3,4)
final_output=func3(output3)
print(final_output)