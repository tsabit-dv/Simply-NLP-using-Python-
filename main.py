import spacy
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio, display

class SimpleChatbot:
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)
        self.intents = {
            "greeting": ["hello", "hi", "hey"],
            "farewell": ["bye", "goodbye", "see you"],
            "weather": ["weather", "rain", "sunny", "cold"],
        }
        self.responses = {
            "greeting": "Hello! How can I help you?",
            "farewell": "Goodbye! Have a great day!",
            "weather": "I can't predict the weather, but you can check a weather app!",
            "unknown": "Sorry, I didn't understand that."
        }
    
    def text_to_speech(self, text, lang="en"):
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        display(Audio(audio_buffer.read(), autoplay=True))
    
    def get_intent(self, text):
        doc = self.nlp(text.lower())
        for intent, keywords in self.intents.items():
            if any(token.text in keywords for token in doc):
                return intent
        return "unknown"
    
    def chat(self):
        print("Chatbot: Hello! Type 'exit' to stop.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                self.text_to_speech("Goodbye!")
                break
            intent = self.get_intent(user_input)
            response = self.responses.get(intent, "unknown")
            print(f"Chatbot: {response}")
            self.text_to_speech(response)

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()
