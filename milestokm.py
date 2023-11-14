from tkinter import *


def calculate():
    miles = float(input.get())
    km = miles * 1.609
    label2.config(text=f"{km:.2f}")


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#  we need 4 label, 1 entry and 1 button

# label 1
label1 = Label(text="is equal to", font=("Arial", 18, "bold"))
label1.grid(column=0, row=1)

# label 2
label2 = Label(text="Miles", font=("Arial", 18, "bold"))
label2.grid(column=2, row=0)

# label 3
label3 = Label(text="Km", font=("Arial", 18, "bold"))
label3.grid(column=2, row=1)

# label 2
label2 = Label(text="0", font=("Arial", 18, "bold"))
label2.grid(column=1, row=1)

# entry
input = Entry(width=10)
input.grid(column=1, row=0)

# button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# to keep the window open
window.mainloop()
