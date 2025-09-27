from tkinter import *

#===== constants =====#
COLOR = 'beige'
FONT = 'Courier'

window = Tk()
window.minsize(500, 400)
window.title('BMI Calculator')
window.config(bg=COLOR)

# Center columns
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

#---------- Title ----------#
title_label = Label(text='BMI Calculator',bg=COLOR,fg='brown',font=('Times', 25, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

#------------ Weight label & entry ------------#
weight_label = Label(text='Enter your weight (kg)',bg=COLOR,fg='black',font=(FONT, 11))
weight_label.grid(row=1, column=0, pady=10, sticky="e")

user_weight = Entry(width=20, justify="center")
user_weight.grid(row=1, column=1, pady=10, sticky="w")

#------------ Height label & entry ------------#
height_label = Label(text='Enter your height (cm)',bg=COLOR,fg='black',font=(FONT, 11))
height_label.grid(row=2, column=0, pady=10, sticky="e")

user_height = Entry(width=20, justify="center")
user_height.grid(row=2, column=1, pady=10, sticky="w")

#------------ BMI Result Label ------------#
bmi_label = Label(text='', bg=COLOR, fg='black', font=(FONT, 11))
bmi_label.grid(row=5, column=0, columnspan=2, pady=15)

#------------ BMI Calculation ------------#
def bmi_calculation():
    try:
        weight = float(user_weight.get())
        height = float(user_height.get()) / 100
        bmi = weight / (height)**2
        text_color = 'white'

        if bmi <= 18.4:
            result = "You are underweight."
            color = 'blue'
        elif 18.5 <= bmi <= 24.9:
            result = "You are normal."
            color = 'green'
        elif 25.0 <= bmi <= 29.9:
            result = "You are overweight."
            color = 'yellow'
            text_color = 'black'
        elif 30 <= bmi <= 39.9:
            result = "You are obese."
            color = 'orange'
        else:
            result = "You are severely obese."
            color = 'red'

        bmi_result = f"Your Body Mass Index(BMI) is: {round(bmi,2)}\n{result}"
        bmi_label.config(text=bmi_result, bg=color, fg=text_color, font=(FONT, 12, 'bold'))
    except ValueError:
        bmi_label.config(text='Invalid inputs! Please enter numbers.')

#------------ Calculate button ------------#
calculate = Button(text='Calculate',font=(FONT, 11),bg='brown',fg='white',command=bmi_calculation)
calculate.grid(row=4, column=0, columnspan=2, pady=20)

window.mainloop()
