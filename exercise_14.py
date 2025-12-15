height_list=[]
heights=input("enter heights seperated by space:")
height_list=heights.split()
count=0
for height in height_list:
    count+=1
print(count)
for i in range(count):
    height_list[i]=int(height_list[i])
print(height_list)
total=0
for person in height_list:
    total+=person
print(total)
avg_height=total/count
print(round(avg_height))
  
