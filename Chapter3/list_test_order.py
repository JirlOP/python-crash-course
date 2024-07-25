
# Numerical order test
floats = [1.5, 1.2, 1.3, 1.1, 1.4]

# String order test
strings = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

# Mixed order test
mixed = ['foo', 1.5, 'bar', 1.2, 'baz', 1.3]

print('Numerical order test')
print(floats)
print(sorted(floats))


print('String order test')
print(strings)
print(sorted(strings))

print('Mixed order test')
print(mixed)
print(sorted(mixed)) # Error not operable str vs float

