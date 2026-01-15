def format_name(first,last):
    
 if last=="" and first=="":
    return "enter valid input!"
 else:
    return [first.title(),last.title()]
first=input("Enter first name:\n")
last=input("Enter last name:\n")
result=format_name(first,last)
print(result)
