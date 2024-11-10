from tkinter import *  # Import all tkinter modules for GUI
from random import randint  # Import randint from random module to generate random numbers

# Initialize the main Tkinter window
root = Tk()
root.title('Password Generator')  # Set window title
root.geometry("500x300")  # Set window size

# Function to generate a new random password
def new_rand():
    # Clear the current password entry box before generating a new one
    pw_entry.delete(0, END)

    # Get the password length from the input and convert to an integer
    try:
        pw_length = int(my_entry.get())
    except ValueError:
        pw_entry.insert(0, "Please enter a valid number")
        return

    # Create an empty string to hold the password
    my_password = ''

    # Loop to generate a password of the specified length
    for _ in range(pw_length):
        my_password += chr(randint(33, 126))  # Append a random ASCII character to the password

    # Output the generated password to the screen in the entry box
    pw_entry.insert(0, my_password)

# Function to copy the generated password to the clipboard
def clipper():
    # Clear any previous clipboard contents
    root.clipboard_clear()

    # Append the generated password to the clipboard
    root.clipboard_append(pw_entry.get())

# Label frame to display instructions for the number of characters
lf = LabelFrame(root, text="Enter the number of characters")
lf.pack(pady=20)

# Create an entry box for users to input the desired password length
my_entry = Entry(lf, font=("Abadi", 24))
my_entry.pack(pady=20, padx=20)

# Create an entry box to display the generated password
pw_entry = Entry(lf, text='', font=("Abadi", 24),
                 bd=0, bg="systembuttonface")  # Make it look like a label
pw_entry.pack(pady=20)

# Frame to contain the buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Button to generate a strong password based on the input length
my_button = Button(
    my_frame, text="Generate a Strong Password!", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

# Button to copy the generated password to the clipboard
clip_button = Button(my_frame, text=" Copy to the Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

# Start the main event loop to run the application
root.mainloop()
