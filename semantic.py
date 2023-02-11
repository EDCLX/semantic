
import spacy
nlp = spacy.load('en_core_web_md')

w1 = nlp("cat")
w2 = nlp ("monkey")
w3 = nlp ("banana")


print(w1.similarity(w2))
print(w3.similarity(w2))
print(w3.similarity(w1))

#interesting is that spacy associates bananas with the monkey so it adds up similarity

w4 = nlp("tuna")
w5 = nlp("cat")
w6 = nlp("dolphin")

print(w4.similarity(w5))
print(w6.similarity(w5))
print(w6.similarity(w4))

#interesting for me that dolphin and cat has more similarity than cat and tuna.
#my personal opinion is that its wrong as cats eating tuna its normal.

#example number two

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# practice number 3, comparing similarity between sentences
sentence_to_compare = 'why is my cat on the car'

sentences = ["where did my dog go", 'hello, there is my car',
"I have lost my car in my car", "I would like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)