first='Johnny'
last='Depp'
message  = first + '[' + last + '] is a coder'
msg=f'{first}[{last}] is a coder'
print(msg)
print(message)
length=len(message)
print(length)
msg.upper()

print(msg.find('n'))
print(msg.replace('Depp','Sins'))
print('coder' in msg)