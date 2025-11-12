
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello" # string data type
name = "World" # string data type

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
# git add .
# git commit -m "working with strings"
# git push origin

# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!

name = "your name"
#upper case
# lower case
#print them out

# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
#see if your name is uppercase
print("name ", name.isupper()) # true or false
# capitalization
print("name", name.capitalize()) # capitalizes the variable
# # Find the length of the string
print("Length of phrase:", len(phrase))  # Output: 14


declaration_of_independence = "The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
#find the first paragraph of this online
#paste it in between the quotation marks
#print out the length of it
print(declaration_of_independence)

#push it to github
# git add .
# git commit -m "declaration"
# git push origin

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------

chicago_mayor = "Johnson"
#index slicing
print(chicago_mayor[0])
#get the last letter
print(chicago_mayor[-1])
#get the "s" in the string
print(chicago_mayor[4])
# slicing
#get the "son" from the string
print(chicago_mayor[ 4 : ])
# the first number in slicing is inclusing
# the second number is exclusive
# get the string "John"
print(chicago_mayor[0 : 4])
print(chicago_mayor[0 : -3])
# get "ohns"
print(chicago_mayor[1:5])
# when we get one character/letter
# its called string indexing
# when we get a chunk of letters
#from a string, its called 
# string slicing
# git add .
# git commit -m "string slicing"
#git push origin 

phrase3 = "Supercagifragilstic"
#uppercase it
#slice Super out of it into a different variable
# slice cagi out of phrase3 into its own variable
#print out the last letter
print(phrase.upper())
cut = phrase3[0:5]
print(cut)
# git add .
# git commit -m "practice slicing"
# git push origin 



# # Slicing: Get a range of characters (start inclusive, end exclusive)
soup= " range of characters (start inclusive, end exclusive)"
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth
print("Characters 1 to 4:", soup[:4])
# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"
bathroom = 'Ii was using bahtrooom'
office= "I was in the office"
# # Printing Strings
print(bathroom)
print(office)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)
#git add .
# git commit -m "advanced strings"
# git push origin 

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
