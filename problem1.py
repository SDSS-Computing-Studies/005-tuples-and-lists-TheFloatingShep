#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
x = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(x)
n1 = input("Enter a word from the list: ")
n2 = input("Enter any word: ")
x[x.index(n1)] = n2
print(x)