pizza_size=input("Which size of pizza do you want?")
bill=0
if pizza_size=='S' or pizza_size=='s':
  bill+=100
  print("Small pizza size is 100 Rs.")
elif pizza_size=='M' or pizza_size=='m':
  bill+=200
  print("Medium pizza size is 200 Rs.")
else:
  bill+=300
  print("Large pizza size is 300 Rs.")
add_pepperoni=input("Do you want to add pepperoni(Y/N)?")
if add_pepperoni=='Y'or add_pepperoni=='y':
  if pizza_size=='S'or pizza_size=='s':
    bill+=30
  else:
    bill+=50
extra_cheese=input("Do you want extra cheese(Y/N)")
if extra_cheese=='Y'or extra_cheese=='y':
    bill+=20
print(f"Your final bill is {bill}")
  