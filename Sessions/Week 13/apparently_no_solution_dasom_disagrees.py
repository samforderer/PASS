# @author: Sam Forderer

#Write a Python program to prompt the user for a string that contains a sentence. Keep prompting for sentences until the user enters "exit" in upper, lower or mixed case. While collecting data, you must validate the sentences according to these rules: 
#Sentences must start with an upper-case letter. 
#Sentences must end with a period (".")
#Sentences must have at least three words, separated by a space. 
#Add all valid sentences to a list called valid_sentences. Print all the sentences stored in this list one per line.
sentences = []

while True:
    sentence = input("Enter sentence")
    
    if sentence.lower() == "exit":
        break
    
    if sentence[0].isupper():
        if sentence[len(sentence) - 1] == ".":
            if len(sentence.split()) >= 3:
                sentences.append(sentence)

       
counter = 1 
for i in sentences:
    print(f"sentence {counter}: {i}")
    counter += 1