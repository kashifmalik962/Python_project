import random

class Chatbot:

    def __init__(self):
        self.conversations = {}

    def add_conversation(self, topic, responses):
        self.conversations[topic] = responses

    def get_response(self, user_input):
        topic = self.get_topic(user_input)
        if topic in self.conversations:
            responses = self.conversations[topic]
            response = random.choice(responses)
            return response
        else:
            return "I don't understand."

    def get_topic(self, user_input):
        for topic in self.conversations:
            if user_input.startswith(topic):
                return topic
        return None


chatbot = Chatbot()
chatbot.add_conversation("greeting", ["Hello!", "How can I help you?"])
chatbot.add_conversation("goodbye", ["Goodbye!", "Have a nice day!"])

while True:
    user_input = input("What would you like to talk about? ")
    response = chatbot.get_response(user_input)
    print(response)
    