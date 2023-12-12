#Write a program that inputs a text file. The program should print all of the unique words in the file in 
#alphabetical order.
def get_unique_words(file_path):
    unique_words = set()

    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Split the text into words
        words = file.read().split()

        # Add unique words to the set
        for word in words:
            # Remove punctuation and convert to lowercase for better matching
            cleaned_word = word.strip('.,!?()[]{}"\'').lower()
            unique_words.add(cleaned_word)

    return sorted(list(unique_words))

def main():
    file_path = input("Enter the path to the text file: ")

    try:
        unique_words = get_unique_words(file_path)

        print("\nUnique words in alphabetical order:")
        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
