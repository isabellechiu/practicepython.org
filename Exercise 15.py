#Exercise 15
#Reverse Word Order
#strings
#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.

#My answer
string = input("Enter a long string: ")
print(string[::-1])

#More string practices
#1. Splitting strings
# You can “split” or tear apart strings based on a given set of characters. For example:
# teststring = "this is a test"
# result = teststring.split("t")
# And at the end, result will contain the list:
# ['', 'his is a ', 'es', '']
# Instead of "t", you can write any character you want. If you do not include any character, it means “split on all whitespace”:
# teststring = "  this      has a lot    of   spaces and    tabs"
# result = testring.split()
# Then result contains:
# ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
string = input("Enter a long string: ")
teststring = "this is a test"
result = teststring.split(" ")
print(result)

#My answer
string = input("Enter a long string: ")
def split(string):
    s = string.split(" ")
    return print(s[::-1])
split(string)
#2. Joining strings
# You can also relatively easily “join” or “smush” strings together:
# listofstrings = ['a', 'b', 'c']
# result = "**".join(listofstrings)
# Then result will contain the string:
# a**b**c


#My answer
string = input("Enter a long string: ")
def join(string):
    j = "aaa".join(string)
    return print(j[::-1])
join(string)
