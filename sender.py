import socket
import pyaudio
import sys

# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    sock.sendto(in_data, (target_ip, target_port))
    return (None, pyaudio.paContinue)

# Network configuration
target_ip = "127.0.0.1"  # Use localhost for testing
target_port = 12345  # Ensure this matches the receiver's listening port

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                    frames_per_buffer=CHUNK, stream_callback=callback)

try:
    print("Streaming audio. Press Ctrl+C to stop.")
    stream.start_stream()
    while stream.is_active():
        pass
except KeyboardInterrupt:
    print("Streaming stopped by user.")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    sock.close()
