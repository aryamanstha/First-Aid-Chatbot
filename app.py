import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
import pickle
import numpy as np
import json
import random
from keras.models import load_model
model=load_model('chatbot_model.h5')
intents=json.loads(open('intents.json',encoding="utf-8").read())
words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))

from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    return jsonify({"Keyword":"Connection Success"})

def decrypt(message):
    string=message
    new_string=string.replace("+"," ")

def clean_up_sentence(sentence):
    sentence_words=nltk.word_tokenize(sentence)
    sentence_words=[lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence,words,show_details=True):
    sentence_words= clean_up_sentence(sentence)
    bag=[0]*len(words)
    
    for s in sentence_words:
        for i,w in enumerate(words):
            if w==s:
                bag[i]=1
                if show_details:
                    print("found in bag: %s" %w)
    
    return(np.array(bag))  
    
    
def predict_class(sentence,model):
    p=bag_of_words(sentence,words,show_details=False)
    
    
    
    
    
    
    
    
    
def chatbot_response(message):
    intent=predict_class(message,model)
    res=getResponse(intent,intents)
    return res




@app.route("query/<sentence>")
def query_chatbot(sentence):
    decrypt_msg=decrypt(sentence)
    response=chatbot_response(decrypt_msg)
    json_obj=jsonify({"top":{"response":response}})
    return json_obj
    

app.run()