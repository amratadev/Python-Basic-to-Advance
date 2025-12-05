#- Stands for formatted string literal.

name = "Jenny"      # Person's name
age = 30            # Person's age
height = 1.6        # Person's height in meters

# Using string concatenation (need to convert numbers to string with str())
print("My name is " + name + "." + " I am " + str(age) + " Years old." + " My height is " + str(height) + " meter.")

# Using f-string with commas (adds spaces automatically between items)
print(f"My name is ", name, ".", "I am ", age, " Years old.", " My height is ", height, " meter.")

# Proper f-string interpolation (clean and recommended way)
print(f"My name is {name}. I am {age} Years old. My height is {height} meter.")

# Expression inside f-string (father's age is double the person's age)
print(f"My father age is {age*2}")