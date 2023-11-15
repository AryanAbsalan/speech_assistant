from playsound import playsound

import os

# Get the current working directory
current_directory = os.getcwd()

# Specify the path to the audio file
audio_file = "audio8566559.mp3"

# Construct the full path to the audio file
audio_file_path = os.path.join(current_directory, audio_file)


# Play the audio file
playsound(audio_file_path)