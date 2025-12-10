set1={1,2,3,4,5}
set2={4,10,7,8,-10}

print(set1.isdisjoint(set2))
print(set1.isdisjoint((6,7,8,9)))#disjoint->both sets items diff from each other
print(set1.isdisjoint([6,7,8,9]))

#set1 is subset of set2 if every element of set1 is in set2
print(set1.issubset(set2))
print(set1.issubset((6,7,8,9)))
print(set1.issubset([6,7,8,9]))

#set1 is superset of set2 if set1 contains every element of set2
print(set1.issuperset(set2))
print(set1.issuperset((6,7,8,9)))
print(set1.issuperset([6,7,8,9]))

print(set1>=set2)#issuperset like

set3={'Ram','Shyam','Jenny'}
set4={'Jiya','Aakash'}

print(set3.isdisjoint(set4))
print(set3.isdisjoint(('Amrata','Priya')))
print(set3.isdisjoint(['Ram','Shyam']))

print(set3.issubset(['Ram','Shyam','Jenny']))
print(set3.issubset(set4))
print(set3.issubset(('Amrata','Priya')))

print(set3.issuperset(['Shyam',]))
print(set3.issuperset(set4))
print(set3.issuperset(('Amrata','Priya')))

print(set3 >=set(('Amrata','Priya')))#- Superset check only works between sets.
print(set1 >=set((6,7,8,9)))

print(set3<=set3)#every element is subset of itself 
print(set3.issuperset(set3))#every element is superset of itself 
