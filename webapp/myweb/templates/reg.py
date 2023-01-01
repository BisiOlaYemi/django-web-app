from tkinter import *
root = Tk()
root.geometry("500x300")

Label(root, text="Registration form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
email = Label(root, text="Email")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")

name.grid(row=1, column=2)
email.grid(row=2, column=2)
phone.grid(row=3, column=2)
gender.grid(row=4, column=2)

namevalue = StringVar
emailvalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable =namevalue)
emailentry = Entry(root, textvariable =emailvalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)

name.grid(row=1, column=3)
email.grid(row=2, column=3)
phone.grid(row=3, column=3)
gender.grid(row=4, column=3)



root.mainloop()
