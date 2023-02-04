x = 4
print(x)
print(type(x))

x = "Sally"
print(x)
print(type(x))

X = 100.12
print(X)
print(type(X))

#camel case 
myVariableName = "John"

#pascal case
MyVariableName = "John"

#snake case
my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

def myfunc():
  print("I love", x)
myfunc()

def myfunc():
  global x
  x = "fantastic"
myfunc()

print("Python is " + x)