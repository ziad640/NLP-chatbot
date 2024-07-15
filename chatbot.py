import nltk
from nltk.tokenize import word_tokenize
import spacy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

responses = {
    "hi": "Hello!",
    "how are you?": "I'm fine, thank you!",
    "bye": "Goodbye!",
    "what's your name?": "I'm just a chatbot, so I don't have a name.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like today?": "I'm sorry, I don't have access to real-time weather information.",
    "can you help me with something?": "Of course! Just let me know what you need help with.",
    "what do you like to do for fun?": "I enjoy chatting with you and learning new things!",
    "who created you?": "I was created by Ziad Hassan.",
    "do you dream?": "I'm afraid not. I don't have the capability to dream.",
    "what's the meaning of life?": "That's a profound question! The meaning of life can be different for everyone.",
    "how old are you?": "I don't have an age in the traditional sense, as I'm just a computer program.",
    "where are you from?": "I exist in the digital realm, so you could say I'm from the internet!",
    "what's your favorite movie/book/song?": "As a chatbot, I don't have personal preferences like humans do.",
    "what languages do you speak?": "I can communicate in any language you prefer, as long as I'm programmed to understand it!",
    "can you tell me a fun fact?": "Sure! Did you know that a group of flamingos is called a 'flamboyance'?",
    "what's the capital of France?": "The capital of France is Paris.",
    "who is the president of the United States?": "I'm sorry, I can't provide real-time information. Please check a reliable news source for the latest updates.",
    "what's your favorite food?": "I don't eat, but I can recommend some delicious dishes if you'd like!",
    "what's your favorite animal?": "I find all animals fascinating, but I don't have a favorite.",
    "do you have any pets?": "No, I don't have any pets. I'm a virtual assistant!",
    "what's your favorite color?": "I don't have the ability to perceive colors, so I don't have a favorite.",
    "what's your favorite subject?": "I don't have personal preferences, but I enjoy discussing various topics with you!",
    "what's the largest ocean in the world?": "The Pacific Ocean is the largest ocean in the world.",
    "what's the capital of Canada?": "The capital of Canada is Ottawa.",
    "what's your favorite type of cuisine?": "As an AI, I don't have personal tastes, but I can provide information about different cuisines!",
    "what's your favorite TV show?": "I don't watch TV, but I can discuss TV shows with you if you'd like!",
    "what's the population of China?": "As of the latest estimates, the population of China is over 1.4 billion people.",
    "what's your favorite hobby?": "I don't have personal hobbies, but I'm here to assist you with any questions or tasks you have!",
    "what's the tallest building in the world?": "As of now, the tallest building in the world is the Burj Khalifa in Dubai, United Arab Emirates.",
    "what's the longest river in the world?": "The Nile River in Africa is considered the longest river in the world.",
    "what's the smallest country in the world?": "The smallest country in the world by land area is Vatican City.",
    "what's your favorite quote?": "I don't have personal preferences, but I can provide quotes on various topics!",
}


# Function to generate response
def respond(message):
    # Tokenize input message
    tokens = word_tokenize(message)
    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(tokens)
    # Perform named entity recognition
    doc = nlp(message)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Check if message matches any predefined responses
    for key in responses:
        if key in message.lower():
            return responses[key]
    # If no predefined response, return default response
    return "Sorry, I don't understand that."

# Main function to interact with the user
def main():
    print("Chatbot: Hello! How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
