# Word Guessing Game
import random

easy_words = [
    "cat", "dog", "sun", "hat", "ball", "tree", "book", "fish", "milk", "home",
    "car", "road", "rain", "star", "moon", "pen", "cup", "shoe", "bird", "apple",
    "bread", "clock", "grass", "chair", "table", "water", "fire", "wind", "snow",
    "leaf", "rock", "sand", "toy", "key", "door", "bed", "ring", "box", "cake",
    "salt", "sugar", "smile", "laugh", "cry", "play", "run", "jump", "walk",
    "sleep", "dream", "light", "dark", "hand", "foot", "face", "hair", "nose",
    "ear", "eye", "leg", "arm", "kid", "man", "woman", "boy", "girl"
]


medium_words = [
    "planet", "window", "garden", "forest", "river", "mountain", "castle",
    "bridge", "mirror", "shadow", "pencil", "market", "wallet", "camera",
    "pillow", "blanket", "pocket", "silver", "golden", "engine", "rocket",
    "island", "desert", "ocean", "storm", "thunder", "lightning",
    "teacher", "student", "friend", "family", "holiday", "journey",
    "picture", "message", "battery", "signal", "network",
    "music", "guitar", "piano", "drums", "violin",
    "soccer", "cricket", "tennis", "runner", "player",
    "doctor", "engineer", "artist", "writer", "driver",
    "village", "city", "country",
    "laptop", "mobile", "screen", "keyboard", "mouse"
]

hard_words = [
    "adventure", "discovery", "knowledge", "challenge", "mystery",
    "computer", "software", "hardware", "internet", "database",
    "algorithm", "function", "variable", "developer", "programmer",
    "security", "password", "encryption",
    "mountains", "waterfall", "earthquake", "volcano",
    "satellite", "spaceship", "astronaut",
    "direction", "navigation", "destination",
    "community", "education", "government",
    "electricity", "generator", "mechanical",
    "confidence", "attention", "patience",
    "happiness", "darkness", "brightness",
    "restaurant", "supermarket", "transport",
    "temperature", "pollution", "environment",
    "communication", "information"
]

print("Choose Difficulty Level:")
print("1.Easy \n 2.Medium \n 3.Hard")
choice=input("Enter your choice:")

if (choice=='1'):
    word=random.choice(easy_words)
elif (choice=='2'):
    word=random.choice(medium_words)
elif (choice=='3'):
    word=random.choice(hard_words)
else:
    print("Invalid Choice")
    exit()

display=["_"]*len(word)


attempt=0
while True:
    
    guess=input("Enter your guess:").lower()
    attempt=attempt+1
    for i in range(len(word)):
        if i<len(guess) and word[i]==guess[i]:
            display[i]=word[i]
    print("Matched:","".join(display))
        
    if word==guess:
        print("Correct guess")
        print("Guessed in attempts:",attempt)
        break


