def add(*numbers):#Arbitrary Positional Arguments
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}.")
add(5,8)
add(1,2,3,4,5)

def add(*numbers,name):
  print(numbers)
  print(name)
add(1,2,name="Jenny")

def add(a,*numbers):
   print(numbers)#1 is assign to a
add(1,2,3)

def info_person(**kwargs):#Arbitrary Keyword argument 
 for key,value in kwargs.items():
    print(key,value)
info_person(name="Ram",age=30,dept="CSE")
info_person(name="Shyam",dept="CSE")

def info_person(*args,**kwargs):#Arbitrary Keyword argument 
 for key,value in kwargs.items():
    print(key,value)
 print(args)
info_person(1,2,name="Ram",age=30,dept="CSE")
info_person(1,2,3,name="Shyam",dept="CSE")