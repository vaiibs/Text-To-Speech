import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 200)  # Speed of speech (higher is faster)
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Input text
text = """
Artificial intelligence (AI) is revolutionizing various industries and sectors, 
bringing advancements in automation, data processing, and decision-making capabilities. 
AI is transforming healthcare, finance, manufacturing, and more!!
"""

# Convert text to speech
text_to_speech(text)
