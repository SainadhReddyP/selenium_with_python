"""
The following is the complete list of data types in Python:
Text Type - str
Numeric Type - int, float and complex
Sequence Type - list, tuple and range
Mapping Type - dict
Set Type - set and frozenset
Boolean Type - bool
Binary Type - bytes, bytearray and memoryview

set - mutable
forzenset - immutable
"""

my_set = {1,3,5,7}
print(type(my_set))
my_set.add(9)
print(my_set)

my_frozen_set = frozenset(my_set)
print(type(my_frozen_set))

my_frozen_set.add(11)  # we cannot update it - frozenset is immutable

