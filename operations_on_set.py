set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}
set3 = {'Ankur', 'Pradeep'}

print(set1.union(set2, set3))  
# ✅ union() → combines all sets, removes duplicates
# Output: {'Ram','Shyam','Jenny','Jiya','Aakash','Ankur','Pradeep'}

print(set1 | set2 | set3)  
# ✅ Same as union, but using | operator (all operands must be sets)

print(set1.union(('Mohan','Jenny')))  
# ✅ union() can work with other iterables (like tuple/list), duplicates ignored

set1.update(set2)
print(set1)  
# ✅ update() → adds all elements of set2 into set1

set1.update(['Jenny','Mohan'])
print(set1)  
# ✅ update() → can add elements from list/tuple also

set1 |= set2
print(set1)  
# ✅ |= operator works same as update()

print(set1.intersection(set2, set3))  
# ✅ intersection() → common elements among all sets
# Here no common element → Output: set()

print(set1 & set2)  
# ✅ & operator → intersection of two sets
# Output: {'Jenny'}

print(set1.intersection(['Mohan','Shiva']))  
# ✅ intersection() works with other iterables too
# Output: {'Mohan'} if present in set1

print(set1 & set2 & set3)  
# ✅ intersection of all three sets
# Output: set() (no common element)

set2.intersection_update(set1)
print(set2)  
print(set1)  
# ✅ intersection_update() → modifies set2, keeps only common elements with set1
# set2 becomes {'Jenny'}

set2.intersection_update(['Mohan','Shiva'])
print(set2)  
# ✅ intersection_update() with iterable → keeps only common elements
# 'Jenny' not in ['Mohan','Shiva'] → set2 becomes empty set()