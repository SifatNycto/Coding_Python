import pywhatkit
# Convert image to ASCII art and save as a text file
pywhatkit.image_to_ascii_art(r"D:\Coding_Python\LMC-Queen.png", "WordART")
# Print the ASCII art in the terminal
with open("WordART.txt", "r") as f:
    print(f.read())