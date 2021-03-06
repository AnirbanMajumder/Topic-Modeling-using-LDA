
# coding: utf-8

# In[1]:

""" Topic Modelling using LDA - The following packages have been used to show basic steps to apply LDA for topic modelling:
(1) nltk
(2) stop_words
(3) gensim """

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words
from gensim import corpora, models
import gensim


# In[2]:

""" Text Prerpocessing 
Tokenization - converting documents into its atomic elements
Stopping - removing meaningless words
Stemming - merging words that are equivalent in meaning """


# In[4]:

""" Here RegexpTokenizer has been used to tokenize documents using regular expressions """
tokenizer = RegexpTokenizer(r'\w+')


# In[5]:

""" Here English stop words list has been created using get_stop_words from stop_words """
en_stop = get_stop_words('en')


# In[6]:

""" Here Porter Algorithm for stemming has been used from nltk """
p_stemmer = PorterStemmer()


# In[7]:

""" The following sample documents have been created for testing """

doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."

doc_b = "My mother spends a lot of time driving my brother around to baseball practice."

doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."

doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."

doc_e = "Health professionals say that brocolli is good for your health."


# In[8]:

""" Compile sample documents into a list """
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]
print (doc_set)


# In[9]:

""" Initialise a list for tokenized documents in loop """

texts = []


# In[10]:

#loop through document list
for i in doc_set:
    
    #clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    
    #remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    #stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    #add tokens to list
    texts.append(stemmed_tokens)


# In[11]:

# print the resultant after tokenization, stop words removal and stemming

print(texts)


# In[16]:

""" Constructing a document-term matrix to understand how frequently each term occurs within each document.
First, we need to turn our tokenized documents into an id and  term dictionary suing Dictionary() function."""

dictionary = corpora.Dictionary(texts)

""" Check each tokens unique integer id """

print(dictionary.token2id)


# In[20]:

""" Now we convert tokenized documents into a document-term matrix. The function doc2bow coverts dictionary into bag of words 
where the result ie corpus is a list of vectors equal to the number of documents and each document vector is a series of tuples
and the tuples are (term id , term frequency) pairs """

corpus = [dictionary.doc2bow(text) for text in texts]

print(corpus[0])


# In[23]:

""" Generate LDA model with num_topics as how mnay topics should be generated, id2word as mappings b/w id and strings 
and passes (optional) as the number of lapse the model will take through corpus """

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 2, id2word = dictionary, passes=20)


# In[60]:

""" Print the resultant which includes 3 topics generated by LDA"""

print(ldamodel.print_topics(num_topics=2, num_words=4))


# In[ ]:




# In[ ]:



