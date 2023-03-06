# semantic
# Word and Sentence Similarity Using spaCy
This program uses spaCy's natural language processing library to compare the similarity between words and sentences. It includes three examples.

## Installation
To run this program, you will need to have Python 3.x and the spaCy library installed. You can install spaCy by running the following command in your terminal:
pip install spacy

You will also need to download the en_core_web_md model by running the following command:
python -m spacy download en_core_web_md

## Usage
### Example 1: Comparing Word Similarity
This example compares the similarity between different words and prints the results.
import spacy

#load the en_core_web_md model
nlp = spacy.load('en_core_web_md')

#create spacy tokens for different words
w1 = nlp("cat")
w2 = nlp("monkey")
w3 = nlp("banana")

#calculate similarity between the tokens
print(w1.similarity(w2))
print(w3.similarity(w2))
print(w3.similarity(w1))
