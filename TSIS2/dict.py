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

car["year"] = 2020
print(x)

x = thisdict.items()
print(x)

x = car.values()
print(x)
car["color"] = "red"
print(x)

car["year"] = 2020
print(x)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#change items
print()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print(thisdict)


#add items
print()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print(thisdict)


#remove items
print()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)


#loop dictionaries
print()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
for x, y in thisdict.items():
  print(x, y)


#copy dictionaries
print()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)


#nested dictionaries
print()
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(type(myfamily))

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)