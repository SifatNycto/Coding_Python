# import cowsay
# cowsay.cow("hello")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# import pyttsx3

# engine = pyttsx3.init()

# engine.say("hey, yo, arik, who the fuck are you staring at,")
# engine.runAndWait()



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# import pyttsx3

# engine = pyttsx3.init()

# # Change speed
# engine.setProperty('rate', 150)

# # Change volume (0.0 to 1.0)
# engine.setProperty('volume', 1.0)

# # Change voice
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # try 0 / 1

# engine.say("Welcome back, Sifat. System is online.")
# engine.runAndWait()


import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while True:
    try:
        text = input("You: ")

        if text.strip() == "":
            continue   # ignore empty input

        if text.lower() == "exit":
            engine.say("Goodbye.")
            engine.runAndWait()
            break

        response = f"You said {text}"
        
        print("Bot:", response)

        engine.say(response)
        engine.runAndWait()

    except KeyboardInterrupt:
        print("\nExiting...")
        break