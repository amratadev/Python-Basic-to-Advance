a = "Amrata"
b = "amrata"
c = '5'

print(a is b)

print(a is not c)

print(id(a))

List1=["Amrata","Hrutuja"]
List2=["Amrata","Hrutuja"]
print(List1 is not List2)
print(id(List1))
print(id(List2))
#- Small integers (usually from -5 to 256) are pre‑allocated and reused.
#- In Python, every time you create a new list with [...], Python allocates a new object in memory.
