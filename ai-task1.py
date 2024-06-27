# task1 (chatbot with rule_based responses)
def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("you: ").strip().lower()
        if "hello" in user_input or "hi" in user_input:
            print("chatbot: Hello! How can I assist you today?")
        elif"how are you" in user_input:
            print("chatbot: I'm just a bot, but I'm functioning properly!How about you?")
        elif"what is your name" in user_input:
            print("chatbot: I am a simple chatbot created by Giridhar. ")
        elif"bye" in user_input or "exit" in user_input:
            print("chatbot: Goodbye! Have a great day!")
            break
        else:
            print("chatbot:I'm sorry, I dont't understand that. Can you please rephrase?")
if __name__== "__main__":
    chatbot()