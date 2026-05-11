print("````````````````````````````````````````````````````````")
print("             Welcome! to our chatbot.🤖🤖..")
print("     you can ask me question and ai get response")
print("````````````````````````````````````````````````````````")

import random

responses = {
    "hello": ["hi kaisa ha aap 😊","hey there","Hey bro","bolo friend"],
    "how are you": "me acha hu how can i help you",
    "motivate me": "Nothing in life is to be feared, it is only to be understood.",
    "what is c": "C is a programming language",
    "who built you": "Mr.Joydip sir built me",
    "bye": "Goodbye! Have a nice day 😊"
}

def getresponseofBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachkey in responses:
        if eachkey in userQuestion:
            return random.choice(responses[eachkey])
    return "sorry i don't understand that..."
while True:
    userInput = input(" --> Please ask your question: ")
    reply = getresponseofBot(userInput)
    print("chat Bot Response: ", reply)
    
    if "bye" in userInput.lower():
        break