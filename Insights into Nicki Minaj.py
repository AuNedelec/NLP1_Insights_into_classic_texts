
# # Project 1.2 : Insights into Nicki Minaj

# ## Importing and Preprocessing Text Data

# importing NLTK functions for part-of-speech tagging and regex-based parsing
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, RegexpParser

# importing function that returns most common noun phrases and verb phrases chunks
from chunk_counters import np_chunk_counter, vp_chunk_counter
# importing function that tokenizes text input firstly into sentences, then into words
from tokenize_words import word_sentence_tokenize


# importing the song Chun-Li from Nicki Minaj, lowering the case for processing
text = open('nicki_minaj.txt', encoding = 'utf-8').read().lower()

# sentence and word tokenizing text in order to perform sentence-by-sentence parsing analysis later.
word_tokenized_text = word_sentence_tokenize(text)

# storing and printing a random index of word_tokenized_text to visualize what the function returns

test_word_tokenized_sentence = word_tokenized_text[1]
print(test_word_tokenized_sentence)



# ## Part-of-speech Tag Text

# creating an empty list to hold part-of-speech tagged sentences from the text under analysis.
pos_tagged_text = []

# creating a for loop through each word tokenized sentence (token) and append to list of pos tagged text using nltk's pos_tag() function.
for token in word_tokenized_text:
    pos_tagged_text.append(pos_tag(token))

# storing and printing any random part-of-speech tagged sentence to visualize single pos-tagged sentences
test_pos_sentence = pos_tagged_text[4]
print(test_pos_sentence)



# ## Chunk Sentences

# defining a noun phrase 
# (considered here as an optional determiner, any number of adjectives and an obligatory noun, in this order) chunk grammar 
np_chunk_grammar = 'NP: {<DT>?<JJ>*<NN>}'

# creating a noun phrase RegexpParser object 
np_chunk_parser = RegexpParser(np_chunk_grammar)

# defining verb phrase (here considered as noun phrase, a verb in any form and an optional adverb, in this order) chunk grammar
vp_chunk_grammar = 'VP: {<DT>?<JJ>*<NN><VB.*><RB>?}'

# creating verb phrase RegexpParser object
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# creating empty lists to hold noun phrase chunked sentences and verb phrase chunked sentences
np_chunked_text = []
vp_chunked_text = []

# creating a for loop through each pos-tagged sentence which chunks each sentence and appends to list 
for pos_tagged in pos_tagged_text:
    np_chunked_text.append(np_chunk_parser.parse(pos_tagged))
    vp_chunked_text.append(vp_chunk_parser.parse(pos_tagged))
 
# visualizing random indexes of chunked sentences
print(vp_chunked_text[2])  
print(np_chunked_text[2])



# ## Analyze Chunks

# storing and printing the most common NP-chunks in order to gain insights about the book's most relevant noun phrases
# using the function np_chunk_counter()
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)

# thanks to this process, we gain a clear insight about the song's main themes. 
# however, we can notice that the analysis is way less accurate than with a novel like The Iliad due to many interjections and less meaning


# storing and printing the most common VP-chunks using the function vp_chunk_counter()
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)
