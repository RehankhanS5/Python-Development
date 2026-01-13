def is_palindrome(text):
    # Convert to lowercase and remove spaces
    cleaned_text = text.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    return cleaned_text == cleaned_text[::-1]


# User input
user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print("The given string is a palindrome")
else:
    print("The given string is NOT a palindrome")
