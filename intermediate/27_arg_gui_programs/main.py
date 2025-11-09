import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# label.pack(side="left")
# label.place(x=100, y=200)
label.grid(column=0, row=0)

window.mainloop()

# Add a button that closes the window when clicked
def button_clicked():
    print("Button clicked!")
    new_text = input.get()
    label.config(text=new_text)

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry widget to accept user input

input = tk.Entry(width=30)