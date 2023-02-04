cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
print(len(cars))

for x in cars:
  print(x)

cars.append("Honda")
print(cars)

cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)