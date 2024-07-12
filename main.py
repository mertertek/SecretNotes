import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import cryptocode

# Initialize the main window
m = tkinter.Tk()
m.maxsize(400, 400)
m.title("Secret Notes")
m.minsize(300, 600)

# Load the image
path = 'C:/Users/Mert/top_secret.jpg'
original_img = Image.open(path)
resized_img = original_img.resize((300, 130))
img = ImageTk.PhotoImage(resized_img)

# Display the image
panel = tkinter.Label(m, image=img)
panel.pack(side="top")

# Create title label and entry
my_title = tkinter.Label(m, text="Enter Your Title")
my_title.pack()
my_entry = tkinter.Entry(m)
my_entry.pack()

# Create secret label and text box
my_secret = tkinter.Label(m, text="Enter Your Secret")
my_secret.pack()
my_secret_enter = tkinter.Text(m, width=25, height=15)
my_secret_enter.pack()

# Create password label and entry
my_pass = tkinter.Label(m, text="Enter Your Password")
my_pass.pack()
my_key = tkinter.Entry(m, show="*")
my_key.pack()

encoded = ""

def create_secret():
    global encoded
    title = my_entry.get()
    secret = my_secret_enter.get("1.0", "end-1c")
    password = my_key.get()

    # Check if all fields are filled
    if not title or not secret or not password:
        messagebox.showerror("ERROR", "Please fill in all fields")
        return

    # Encrypt the secret
    encoded = cryptocode.encrypt("[{}][{}]".format(title, secret), password)
    print(encoded)

    # Save the encrypted secret to a file
    with open("notes.txt", "w") as f:
        f.write(encoded)

    messagebox.showinfo("Success", "Encrypted successfully")

# Create "Create" button
my_button = tkinter.Button(m, text="Create", bg="Green", command=create_secret)
my_button.pack()

def solve_secret():
    global encoded
    password = my_key.get()

    # Check if encoded secret and password are provided
    if not encoded or not password:
        messagebox.showerror("ERROR", "Please provide the necessary fields")
        return

    # Decrypt the secret
    decoded = cryptocode.decrypt(encoded, password)
    if decoded:
        print(decoded)
        messagebox.showinfo("Success", decoded)
    else:
        messagebox.showerror("Error", "Decryption failed")

# Create "Solve" button
my_button_2 = tkinter.Button(m, text="Solve", bg="Red", command=solve_secret)
my_button_2.pack()

# Run the main loop
m.mainloop()
