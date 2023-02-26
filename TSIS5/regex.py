'''
1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

3. Write a Python program to find sequences of lowercase letters joined with a underscore.

4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.

7. Write a python program to convert snake case string to camel case string.

8. Write a Python program to split a string at uppercase letters.

9. Write a Python program to insert spaces between words starting with capital letters.

10. Write a Python program to convert a given camel case string to snake case.
'''
import re

#1

def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ac"))
print(text_match("a"))
print(text_match("abbb"))
print('\n')

#2

def text_match(text):
    patterns = '^a(bb+)$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ac"))
print(text_match("a"))
print(text_match("abb"))
print('\n')

#3

def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))
print('\n')

#4

def text_match(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))
print('\n')

#5

def text_match(text):
    patterns = 'a.*?b$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))
print('\n')

#6

text = 'Python Exercises, GO exercises.'
print(re.sub("[ ,.]", ":", text))
print('\n')

#7

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


print(snake_to_camel('python_exercises'))
print('\n')

#8

text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))
print('\n')

#9

def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))
print('\n')

#10

def camel_to_snake(text):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()


print(camel_to_snake('PythonExercises'))