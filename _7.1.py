def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string without spaces: ")

if is_palindrome(input_string):
    print("yes")
else:
    print("no")
