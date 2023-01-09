from guizero import App, Box, Text

app = App()
b1 = Box(app, width ="fill", height =30)
b1.bg = "blue"
text = Text(b1, width="fill", text="TEST")

b2 = Box(app, width="fill", height=100)
b2.bg = "black"
b4 = Box(b2, align="right", width=40, height="fill")
b4.bg = "yellow"
b5 = Box(b2, align="left", width="fill", height="fill")
b5.bg = "purple"

b3 = Box(app, width="fill", height=30)
b3.bg = "green"


app.display()
