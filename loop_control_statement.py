count=1
while count<=10:
    print(count)
    count+=1
    if count==5:
        break
else:
    print("Hi")
print("out from block")

for i in range(1,10):
    print(i)
    i+=1
    if i==3:
        break
else:
    print("Hi")
print("Out from block")

list1=["hi","hello","welcome"]
names=["Krishn","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
    if item=="hello" and name=="Ram":
        break
    print("Out From Inner Loop")   
print("Out From Inner Loop")   