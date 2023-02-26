import tkinter as tk

class Prompt(tk.Tk):
    def __init__(self, default_value):
        self.answer = None
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.entry.insert(string=str(default_value), index=0)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()


    def on_button(self):
        self.answer = self.entry.get()
        self.quit()

def get_input_data(default_value):
    promptData = Prompt(default_value)
    promptData.mainloop()
    promptData.destroy()
    return promptData.answer