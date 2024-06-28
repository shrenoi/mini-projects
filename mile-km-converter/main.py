from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0,  pady=10)

miles_unit = Label(text="Miles", font=("Arial", 14))
miles_unit.grid(column=2, row =0, padx=10)

text_label = Label(text="is equal to", font=("Arial", 14))
text_label.grid(column=0, row=1, padx=10)

km_value = Label(text="0", font=("Arial", 14))
km_value.grid(column=1, row=1)

km_unit = Label(text="Km", font=("Arial", 14))
km_unit.grid(column=2, row=1, padx=5)

def calculate():
    km = round((float(miles_input.get()) * 1.6))
    km_value.config(text=f"{km}")

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2, pady=10)

window.mainloop()