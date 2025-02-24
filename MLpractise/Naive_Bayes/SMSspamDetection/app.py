import streamlit as st 
from nltk.stem.porter import PorterStemmer 
from nltk.corpus import stopwords
import nltk
import pickle

def transform_text(txt: str)->str:
    txt = txt.lower()
    word_list = nltk.word_tokenize(txt)

    ps = PorterStemmer()

    filtered_word = [ps.stem(word) for word in word_list if word.isalnum() and word not in stopwords.words('english')]

    return " ".join(filtered_word)

def vectorize(txt: str):
    with open("vectorizer.pkl", "rb") as vectorizer:
        tfidf = pickle.load(vectorizer)
        
        return tfidf.transform([txt]).toarray()

def predict(vectorized_text):
   
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
        result = model.predict(vectorized_text)

        return result[0]

st.header("Spam Detection")
input = st.text_area(label="Enter sms")
if(st.button("Predict")):
    transformed_text = transform_text(input)
    vectorized_text = vectorize(transformed_text)
    if(predict(vectorized_text)):
        st.warning("Spam")
    else:
        st.success("Not a spam")
