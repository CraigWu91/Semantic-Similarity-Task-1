import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.
    # Cat and monkey has a high similarity as they are both animals.
    # Banana and monkey has a high similarity as monkeys eat bananas. 
    # Cat and monkey has a lower similarity compared to the first 2

word1 = nlp("tea")
word2 = nlp("coffee")
word3 = nlp("apple")
print("\nMy own example:")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

    # Tea and cofee has a very high similarity as they are both drinks
    # Cofee with apple has low similarity and tea with apple has little bit lower similarity

# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model 'en_core_web_md'.
    # When using 'en_core_web_sm' on the example file the similarities results are lower compared to 'en_core_web_md'.