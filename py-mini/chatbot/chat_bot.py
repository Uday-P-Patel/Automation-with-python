import random
print("BOT: Hello there!! What's your name?")
user_name = input()

bot_template = "BOT : {0}"
user_template = user_name + " : {0}"

name = "mini-Chatbot" 
weather = ["rainy ","Sunny ","Cold "] 
mood = ["Happy ","Sad :| ","Gloomy ","Anime and Chill XD"]

responses = { 
    
"hello":["hello {0}".format(user_name)],
    
"what's your name?": [ 
"They call me {0}".format(name), 
"I usually go by {0}".format(name), 
"My name is the {0}".format(name) ],
    
"what's today's weather?": [ 
"The weather is {0}".format(random.choice(weather)), 
"It's {0} today".format(random.choice(weather)), 
"Let me check, it looks {0} today".format(random.choice(weather)) ],
    
"Are you a robot?": [ 
"What do you think?", 
"Maybe yes, maybe no!", 
"Yes, I am a robot with human feelings ;)", ],
    
"how are you?": [ 
"I am feeling {0}".format(random.choice(mood)), 
"{0}! How about you?".format(random.choice(mood)), 
"I am {0}! How about yourself?".format(random.choice(mood)), ],
    
"": [ 
"Hey! Are you there?", 
"What do you mean by saying nothing?", 
"Sometimes saying nothing tells a lot :)", ],
    
"default": [
"I don't quite get it!!"] }

def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message

def related(x_text): 
    if "hello" in x_text:
        y_text = "hello"
    elif "name" in x_text: 
        y_text = "what's your name?"
    elif "weather" in x_text: 
        y_text = "what's today's weather?"
    elif "robot" in x_text: 
        y_text = "are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    else: 
        y_text = ""
    return y_text

def send_message(message): 
    print(user_template.format(message)) 
    response = respond(message) 
    print(bot_template.format(response))

print("Any questions?")
while 1: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_message(related_text)
    if my_input == "exit" or my_input == "stop": 
        break
