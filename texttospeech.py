import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)

# Speed of speech
engine.setProperty('rate', 150)  
# Volume level (0.0 to 1.0)
engine.setProperty('volume', 0.9)  
# Get the list of available voices
voices = engine.getProperty('voices')

# Print available voices and their IDs
# Set the voice using the voice ID
for voice in voices:
    print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)
    engine.setProperty('voice', voice.id)
    # Input text
    text = """
    In this example,The script prints the 
    voice ID, name, and supported languages
    for each voice"""

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
