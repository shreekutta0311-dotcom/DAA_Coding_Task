##"Open a text document read the string and print the string in the document.Handle exceptions accordingly"
try:
    with open("input.txt","r") as file:
        text=file.reead()
        print("text of the file ",text)

except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: Could not read the file.")
