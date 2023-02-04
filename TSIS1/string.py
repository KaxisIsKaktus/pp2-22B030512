#python strings
print("Hello")
print('Hello')

a = """Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you"""
print(a)
print(a[101])
print(len(a))

for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
print(txt[5:15])
if "free" in txt:
  print("Yes, 'free' is present.")
if "free" in txt:
  print("Yes, 'free' is present.")


#slicing strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])


#modify strings
print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.replace("f", "t"))
print(txt.split(" "))


#concatenate strings
print(b + "" + txt)


#format strings
b = 18
c = "Kaxis is kaktus. Also he is {}"
print(c.format(b))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#escape charecters
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""
txt = "We are the so-called \"Vikings\" from the north."
print(txt)