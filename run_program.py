from keras.models import load_model
import json
import random
import pickle
import nltk
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

model = load_model('chatbot_model.h5')



def bag_of_words(msg, words):

	msg_words = nltk.word_tokenize(msg)
	l_words = [lemmatizer.lemmatize(word.lower()) for word in msg_words]
	bow = [0]*len(words)
	for word in l_words:
		for i,w in enumerate(words):
			if w == word:
				bow[i] = 1
	return(np.array(bow))



def predict(sentence, model , intents_json):
    bow = bag_of_words(sentence, words)
    result = model.predict(np.array([bow]))[0]
    THRESHOLD = 0.25
    for i,r in enumerate(result):
    	if r>THRESHOLD:
    		output_list = [[i,r]]


    output_list.sort(key=lambda x: x[1], reverse=True)
    output = []
    for r in output_list:
        output.append({"intent": classes[r[0]], "probability": str(r[1])})

    tag = output[0]['intent']
    intents_list = intents_json['intents']
    for i in intents_list:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    res = predict(msg, model , intents)
    return res


def chat():
    print("Hi, I'm chiku and I chat alot ;)\n\nPlease type lowercase English language to start a conversation. Type quit to leave \n\n")
    while True:
    	msg = str(input())
    	if msg.lower() == "quit":
    		break
    	res = chatbot_response(msg)
    	print(res)
    	print("\n")




if __name__ == "__main__":
    chat()