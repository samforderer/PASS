sentence = "The dog walked across the street."

search_term = input("Enter a search term: ")

# search the string for user's input, if it exists, then print out the term 

def search_sentence(sentence, term):
    if term in sentence: 
        return True 
    else:
        return False

if search_sentence(sentence, search_term):
    print("It is in there.")
else:
    print("it's not in there.")
        