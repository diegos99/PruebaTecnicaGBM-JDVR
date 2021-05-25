input_text = input("please enter a word:") # variable saves the word entered by the user
if input_text == input_text[::-1]: # [::-1] take a word and write it in reverse
    print("The word is Palindrome.")
else:
    print("The word isn't Palindrome.")