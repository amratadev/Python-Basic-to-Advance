def greet(name,dept):
    print(f"Hi,{name}")
    print(f"Are you from {dept} department?")
greet("Jenny","CS") #Positional Arguments

def greet(name,dept):
    print(f"Hi,{name}")
    print(f"Are you from {dept} department?")
greet(dept="CS",name="Jenny")#Keyword Argument

def greet(name,dept):
    print(f"Hi,{name}")
    print(f"Are you from {dept} department?")
greet("Jenny",dept="CS")#mixed positional and keyword arguments 
#- All positional arguments must come before keyword arguments.

def greet(name,subject,dept="CS"):
    print(f"Hi,{name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")
greet("Jenny","Python","ME")#Override Default Arguments DEPT

#default argument should be provided after the non default argument

def add(*numbers):#Arbitrary /Variable Length Arguments
  c=0
  for i in numbers:
    c=c+i
  print(f"sum is {c}.")
add(5,8,8)
add(1,10,20,80,5)
