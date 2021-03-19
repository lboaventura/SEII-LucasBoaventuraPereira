message0 = 'Hello world'
print(message0)
print(len(message0))
print(message0[0:5])
print(message0.upper())

greeting = 'Hello'
name= 'Lucas'

message1 = greeting + ', ' + name + '. Welcome!'
print(message1)

message2 = '{}, {}. Welcome!'.format(greeting, name)
print(message2)

message3 = f'{greeting}, {name}. Welcome!'
print(message3)