# What will be the length of the following set S:
# S = Set() --> empty set length 0

# S.add(20) --> 1

# S.add(20.0) --> 2

# S.add(“20”) --> 3

S = set()
S.add(20)
S.add(20.0)
S.add('20')
print(S)
print(len(S))