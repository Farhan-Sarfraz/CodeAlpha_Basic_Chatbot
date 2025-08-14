

def ChatBot(msg: str ) -> str:
    msg = msg.lower().strip()

    if msg == "hi" or msg == "hello" or msg == "hey":
        return "Hi! How i can help you today? "
    
    elif  msg == "What is your name" or msg == "your name":
        return "My name is ChatBot.Nice to meet you. "
    
    elif msg == "help":
        return (
            "you can try typing: \n"
            "_hello\n"
            "_what is your name\n"
            "_tell me a joke\n"
            "_fun fact\n"
            "_bye\n"
        )
    
    elif msg == "tell me a joke" or msg == "joke":
        return "Why do progarmmers prefer dark mode ?Because light attracts bugs."
    
    elif msg == "fun fact":
        return "Did you know? Honey never spoils!"

    
    elif msg == "bye" or  msg == "goodbye":
        return "Goodbye! have a nice day."
    
    else:
        return "Sorry! I don't understand that. Type 'help' to see what i can do for you. "
    


print(" Welcome To Simple ChatBot! ")
print("Type 'help' to see commands or Type 'bye' to exit.")

while True:
    user_msg = input("you: ")
    ChatBot_reply = ChatBot(user_msg)
    print("ChatBot: ", ChatBot_reply)

    if user_msg.lower().strip() in ["bye" or "goodbye"]:
        break