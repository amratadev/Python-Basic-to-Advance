set1 = {10, 56, 89, 90, 'Jenny', True}
print(set1)  # ✅ Set items are unordered (no fixed sequence)

set2 = {10, 56, 89, 90, 'Jenny', True, 10, 1}
print(set2)  # ✅ Duplicates are not allowed in set

# print(set2[1])  # ❌ Indexing & slicing not allowed because sets are unordered

print(type(set2))  # ✅ <class 'set'>

set3 = {}
print(type(set3))  # ✅ Empty {} creates dict, not set

# To create empty set
set4 = set()
print(type(set4))  # ✅ <class 'set'>

# set1[2] = 99
# print(set1)  # ❌ Cannot replace set item (immutable positions, no indexing)

set1.add(25)  # ✅ add() method adds only one item at a time (position not guaranteed)
print(set1)

print(len(set1))  # ✅ Shows number of elements in set

set1.remove(10)  # ✅ remove() deletes element; if not present → KeyError
# set1.remove(28)  # ❌ KeyError because 28 not present
print(set1)

"""
✅ remove() → error if element not present
✅ discard() → no error if element not present, silently ignores
"""
set1.discard(28)
print(set1)

print(set1.pop())  # ✅ pop() removes and returns a random element
print(set1)

set1.clear()
print(set1)  # ✅ clear() removes all items from set

# set1.pop()
# print(set1)  # ❌ KeyError because no item left to pop

set1.add((20, 30, 40))
print(set1)  # ✅ Tuples are immutable, so can be added to set

# set1.add([25, 35, 41])  # ❌ Lists are mutable, cannot be added to set
# print(set1)