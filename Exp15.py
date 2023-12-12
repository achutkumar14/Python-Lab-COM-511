#Create a python program to implement Morse Code Translator.
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char
    return morse_code.strip()

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text

def main():
    print("Morse Code Translator")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        text_input = input("Enter the text to convert to Morse Code: ")
        morse_output = text_to_morse(text_input)
        print("Morse Code: ", morse_output)
    elif choice == '2':
        morse_input = input("Enter the Morse Code to convert to text: ")
        text_output = morse_to_text(morse_input)
        print("Text: ", text_output)
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
