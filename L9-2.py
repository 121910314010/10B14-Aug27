stack = []

stack.append('a')
stack.append('b')
stack.append('c')
try:
    raise IndexError #as test error
except Exception as e:
    excepName = type(e)._name_ # returns the name of the exception

print('Initial stack')
print(stack)


print('\nElements poped from stack:')
print(stack.pop(3))

print(stack)
