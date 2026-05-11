word = input("Enter a word: ")

# reverse the string
reverse_word = word[::-1]

if word == reverse_word:
    print("Palindrome")
else:
    print("Not Palindrome")
