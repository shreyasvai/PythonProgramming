# Write a function that reverses a string without using library functions

input_string = input("Enter a string to be reversed: ") # Takes string that will be reversed
result_string = "" # Inserts character by character into the resulting string
a = len(input_string) - 1 # Accesses the last character in input string

for i in input_string: # Iterates through the input string an inserts each character in the result string
    result_string = result_string + input_string[a]
    a = a - 1

if input_string == result_string: # Checks to see if the string is a palindrome
    print("Palindrome!")

print(result_string)