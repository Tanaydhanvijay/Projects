# music_player.py

import random
import webbrowser

# List of random music URLs (MP3 streaming links or YouTube songs)
music_links = [
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
]

def play_random_song():
    song = random.choice(music_links)
    print("🎵 Now playing:", song)
    webbrowser.open(song)
