import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()
import nltk
nltk.download('punkt_tab')

def main():
    print("Hello, I am MemeReactionbot, and I am the personal Meme reaction generator of Mr. Turja Dutta.")
    print("You can end this conversation at any time by typing 'bye'")    
    print("After typing each answer, press 'enter'")
    print("How are you doing today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Goodbye! Have a great day!")
            break
        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)
            np = user_input_blob.noun_phrases
            response = ""
            if user_input_blob.polarity <= -0.5:
                response = "Its the biggest piece of dogshit! " # The ROCK interview
            elif user_input_blob.polarity <= 0:
                response = "I mean, its all right like. Overrated as fuck in my opinion. " # Burger eating guy
            elif user_input_blob.polarity <= 0.5:
                response = "Woooooooo! yeeeeaaaaahhhh Babbyyy. " # Moist Cr1TiKaL reaction
            elif user_input_blob.polarity <= 1:
                response = "Man! I gotta tell you. It was Perfect. PERFECT, everything, down to the last minute details. " # Homelander
            elif user_input_blob.polarity > 1:
                response = "Thats why he is the GOAT. Theee GOOAAT"
            
            if len(np) != 0:
                response += "Noice! What about " + np[0].pluralize() + "?"
            else:
                response += "Tell me more man! "
            
            print(f"Bot: {response}")

main()
            
