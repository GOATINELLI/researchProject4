from guizero import App, Text, Picture, PushButton, Combo, TextBox, Window


app = App()
max  = 38
min  = 35
healthy = 37
def save_baby():
    cur_temp = int(temp.value)
    baby = [name.value, gender.value, temp.value]
    print(baby)
    if float(temp.value) > max:
        print("THE BABY IS TOO HOTTTT")
    if float(temp.value) < min:
        print("THE BABY IS TOO COLDDD")
    if float(temp.value) <= max:
        print("The baby is healthy:)")

text = Text(app, text="Baby Temperature App")
picture = Picture(app, image="baby.png", width=500, height=200)
gender = Combo(app, options=["Select gender", "Boy", "Girl"])
name = TextBox(app, text="Enter Baby Name", width=20)
temp: TextBox = TextBox(app, text="Enter Baby Temp", width=20)
button = PushButton(app, command=save_baby, text= "Save data")
app.display()
