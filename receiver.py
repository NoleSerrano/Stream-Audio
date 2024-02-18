import socket
import pyaudio
import os
import signal
import keyboard

def stop_script():
    print("Stopping script")
    os.kill(os.getpid(), signal.SIGTERM)

stop_keybind="alt+z"
keyboard.add_hotkey(stop_keybind, stop_script)

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Match this with the sender's configuration
RATE = 44100  # Match this with the sender's configuration
CHUNK = 1024  # This should be the same as in the sender to ensure smooth playback

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream for playback
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, output=True,
                    frames_per_buffer=CHUNK)

# Network configuration
bind_ip = "0.0.0.0"
bind_port = 12345  # Ensure this matches the sender's target port

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((bind_ip, bind_port))

print(f"Listening on {bind_ip}:{bind_port} for incoming audio. Press Ctrl+C to stop.")
try:
    while True:
        data, addr = sock.recvfrom(CHUNK * CHANNELS * 2)  # Adjust buffer size if necessary
        stream.write(data)
except KeyboardInterrupt:
    print("Audio reception stopped by user.")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    sock.close()
