from guizero import App, Text

app = App(title='Hello GUI')
message = Text(app, text='Hello I am some text!')
app.display()
