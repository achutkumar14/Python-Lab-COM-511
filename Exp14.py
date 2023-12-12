#Create a text file “MyFile.txt” in python and ask the user to write separate 3 lines with three input 
#statements from the user.
def create_file():
    # Open the file in write mode
    with open("MyFile.txt", "w") as file:
        # Ask the user to input three lines
        for i in range(3):
            line = input(f"Enter line {i + 1}: ")
            file.write(line + "\n")

    print("File 'MyFile.txt' has been created successfully.")

if __name__ == "__main__":
    create_file()
