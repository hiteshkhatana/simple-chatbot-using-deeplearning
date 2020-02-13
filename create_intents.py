import json

data = {"intents": [
        {"tag": "one",
         "patterns": ["do you like icecream","you love icecream?","want to have icecream" ],
         "responses": ["No , I don't like icecreams","I am a machine , stop asking me silly questions"],
        },
        {"tag": "two",
         "patterns": ["do you have a girlfriend","who is your girlfriend"],
         "responses": ["I don't have any girlfriend"],
        },
        {"tag": "three",
         "patterns": ["what is you age","tell me your age"],
         "responses": ["I'm a computer program , i don't have age"],
        },
        {"tag": "four",
         "patterns": ["who are you","what is your name"],
         "responses": ["My name is cheeku and i am a chatbot \n\n What is your Name ?"],
        },
        {"tag": "five",
         "patterns": ["who created you"],
         "responses": ["hitesh khatana created me for his assignment"],
        },
        {"tag": "six",
         "patterns": ["Hi there", "How are you", "Is anyone there?","Hey","Hola", "Hello", "Good day"],
         "responses": ["Hello", "Good to see you again", "Hi there, how can I help?"],
        },
        {"tag": "seven",
         "patterns": ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"],
         "responses": ["See you!", "Have a nice day", "Bye! Come back again soon."],
        },
        {"tag": "eight",
         "patterns": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
         "responses": ["you're welcome" ,"Any time!", "My pleasure" , "good luck"],
        },
        {"tag": "noanswer",
         "patterns": [],
         "responses": ["Sorry, can't understand you", "Please give me more info", "Not sure I understand"],
        },
        {"tag": "nine",
         "patterns": ["How you could help me?", "What you can do?", "What help you provide?", "How you can be helpful?", "What support is offered"],
         "responses": ["I am a basic chatbot and I can answer simple questions"],
        },
        {"tag": "ten",
         "patterns": [r"My name is (.*)" , r"I am (.*)" , r"I'm (.*)" ],
         "responses": ["Nice name"],
        },
   ]
}

with open('intents.json', 'w') as outfile:
    json.dump(data, outfile)

print("intents file created and saved in directory")