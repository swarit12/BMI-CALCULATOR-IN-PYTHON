from tkinter import *
from tkinter import messagebox

root= Tk()

root.geometry("300x200")
root.title("BMI Calculator")
root.minsize("300", "200")
root.maxsize("300", "200")
frame1= Frame(root).grid(row= 5, pady= 45, padx= 50)

def calculate():
    try:
        kg= float(weight_input.get())
        centi= float(height_INput.get())
        bmi= kg/(centi/100)**2
    except:
        messagebox.showerror("BMI Calculator Says", "TYPE YOUR HEIGHT AND WEIGHT IN THE BLANKS GIVEN")
    condition = Label(root, text='')
    condition.grid(row=10, column=1)

    if bmi<18.5:
        messagebox.showinfo("BMI Calculator Says", f"BMI : {bmi}\n\nYOU ARE UNDERWEIGHT")

    elif int(18.5)<bmi<int(24.9):
        messagebox.showinfo("BMI Calculator Says", f"BMI : {bmi}\n\nYOU ARE IN NORMAL CONDITION")

    elif int(24.9)<bmi<int(29.9):
        messagebox.showinfo("BMI Calculator Says", f"BMI : {bmi}\n\nYOU ARE OVERWEIGHT")

    else:
        messagebox.showinfo("BMI Calculator Says", f"BMI : {bmi}\n\nYOU ARE OBESE")

# Labels
weight_input= StringVar()
height_INput= StringVar()

height= Label(frame1, text= "HEIGHT (IN C.M)",font=("Candara", 13, "bold")).grid(padx= 12, row= 5, column= 0)

height_entry= Entry(frame1, textvariable= height_INput).grid(row= 5, column= 1)

weight= Label(frame1, text= "WEIGHT (IN K.G)", font=("Candara", 13, "bold")).grid(row=7, column= 0)

weight_entry= Entry(frame1, textvariable= weight_input).grid(row= 7, column= 1)

calculate= Button(root, text= "CALCULATE", border=3, command= calculate, font="Candara, 14")
calculate.grid(pady= 30, padx= 10, column= 0)

root.mainloop()