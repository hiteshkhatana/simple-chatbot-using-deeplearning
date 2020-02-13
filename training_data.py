import json
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import pickle
import random
import numpy as np
from model import create

words=[]
classes = []
documents = []
ignore_words = ['?', '!' ,'.' ,',',' ']
data_file = open('intents.json').read()
intents = json.loads(data_file)

for i in intents['intents']:
    for pattern in i['patterns']:

        t_words = nltk.word_tokenize(pattern)
        words.extend(t_words)
        documents.append((t_words, i['tag']))

        if i['tag'] not in classes:
            classes.append(i['tag'])


lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))


pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))


train = []
class_list = [0] * len(classes)
for doc in documents:
    bow = []
    p_words = doc[0]

    patterns = [lemmatizer.lemmatize(word.lower()) for word in p_words]
    for w in words:
        bow.append(1) if w in patterns else bow.append(0)

    output = list(class_list)
    output[classes.index(doc[1])] = 1

    train.append([bow, output])

random.shuffle(train)
train = np.array(train)

train_x = list(train[:,0])
train_y = list(train[:,1])

create(train_x,train_y)

print("\n\nModel is trained with training data\n")