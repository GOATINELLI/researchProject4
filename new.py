from guizero import App, Window, PushButton, Text
import random
def open_window():
    window = Window(app, title ="Second Window")
    message = Text(window)
    window.show(wait=True)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    app.bg = [red, green, blue]

app = App(title = "Main Window")
open_button = PushButton(app, text="Open", command=open_window)
open_button.repeat(1, open_window)
app.display()
