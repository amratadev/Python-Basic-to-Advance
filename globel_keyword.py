# a=10
# def display():
#     global a
#     a=a+1
#     print(a)
# display()

# def display():
#     a=20
#     def show():
#         global a
#         a=30
#     print(f"value of a before calling show() function is {a}")
#     show()
#     print(f"value of a after calling show() function is {a}")
# display()    

name="Jenny's"
def display():
    global name
    name=name+" Lectures"
print(name)
display()
print(name)