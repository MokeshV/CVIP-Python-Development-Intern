# Import the required modules
from os import device_encoding
import sounddevice_encoding as sd
import soundfile as sf

# Define the sampling frequency and duration of recording
fs = 44100 # Hz
duration = 10 # seconds

# Prompt the user to start recording
print("Press Enter to start recording")
input()

# Record the audio using sounddevice module
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait() # Wait until recording is finished

# Prompt the user to save the file
print("Press Enter to save the file")
input()

# Save the file using soundfile module
file_name = input("Enter the file name: ") + ".wav"
sf.write(file_name, audio, fs)
print("File saved as", file_name)
