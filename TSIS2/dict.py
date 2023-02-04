#python dictionaries
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020, "colors": ["red", "white", "blue"]}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#access dictionary items
print()
thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)

x = thisdict.keys()
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

x = thisdict.values()
print(x)