from tkinter import *

window = Tk()
window.title("Miles to KM Converter")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km_unit_label = Label(text="KM")
km_unit_label.grid(column=2, row=1)

def convert_miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_label.config(text=f"{km:.2f}")

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)  

window.mainloop()
