# Assume that you have been given a list called mylist that contains 0 or more strings, for example ["Hello", "world", "I", "am", "an", "AI", "assistant"]. Do not make any assumptions about how many strings are in the list, or the contents, other than they will all be valid strings. 
# Create a function called count_lowercase_letters that takes in the list as a parameter and 
# returns the total count of lowercase letters in all the strings in the list. 

list = ["Hello", "world", "I", "am", "an", "AI", "assistant"]

def count_lowercase_letters(list):
    count_lowercase = 0
    for word in list:
        for character in word:
            if character.islower():
                count_lowercase += 1 
    
    return count_lowercase

lowercase_count = count_lowercase_letters(list)

print(lowercase_count)