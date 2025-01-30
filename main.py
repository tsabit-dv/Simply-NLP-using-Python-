import spacy
import logging
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio, display
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SpeechChatbot:
    
    def __init__(self, model="en_core_web_sm"):
        try:
            self.nlp = spacy.load(model)
            logging.info(f"Model NLP '{model}' berhasil dimuat.")
        except Exception as e:
            logging.error(f"Gagal memuat model NLP: {e}")
            raise
        
        self.response_rules = {
            "perkenalan": ["halo", "hai", "hey"],
            "dadah": ["bye", "goodbye", "see you", "sampai jumpa"],
            "cuaca": ["cuaca", "hujan", "cerah", "panas", "dingin"],
            "gurauan": ["joke", "guyon", "funny", "humor"]
        }

        self.responses = {
            "perkenalan": "Halo, ada yang bisa saya bantu?",
            "dadah": "Baik, terima kasih! Semoga harimu menyenangkan!",
            "cuaca": "Saya tidak tahu pasti, coba cek aplikasi cuaca ya!",
            "gurauan": "Gula, gula apa yang bukan gula? Gula aren! Hahaha.",
            "unknown": "Maaf, saya tidak mengerti maksudmu."
        }

    def text_to_speech(self, text, lang="id"):
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            display(Audio(audio_buffer.read(), autoplay=True))
        except Exception as e:
            logging.error(f"Error dalam text-to-speech: {e}")

    def get_intent(self, text):
        doc = self.nlp(text.lower())
        for intent, keywords in self.response_rules.items():
            if any(token.text in keywords for token in doc):
                return intent
        return "unknown"

    def generate_response(self, text):
        intent = self.get_intent(text)
        return self.responses.get(intent, "unknown")

    def chat(self):e
        print("Chatbot: Hi! Saya bot suara. Ketik 'exit' untuk keluar.")

        while True:
            user_input = input("Kamu: ")
            if user_input.lower() == "exit":
                self.text_to_speech("Dadah, sampai jumpa lagi!")
                break

            response = self.generate_response(user_input)
            print(f"Avatar: {response}")
            self.text_to_speech(response)
            time.sleep(1)

if __name__ == "__main__":
    chatbot = SpeechChatbot()
    chatbot.chat()
