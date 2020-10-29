stack = []

stack.append('a')
stack.append('b')
stack.append('c')
try:
    raise IndexError 
except Exception as e:
    excepName = type(e)._name_ 

print('Initial stack')
print(stack)


print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
