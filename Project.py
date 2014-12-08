'''Project'''
from Tkinter import *
root = Tk()
weight_machine = ""
jeans_dark = ""
top_dark = ""
sktr_dark = ""
jeans_light = ""
top_light = ""
sktr_light = ""
weight = IntVar()
jeansdark = IntVar()
topdark = IntVar()
sktrdark = IntVar()
jeanslight = IntVar()
toplight = IntVar()
sktrlight = IntVar()
class Application(Frame):
    def user(self):
##        toor = Tk()
##        toor.title("Washing Machine")
##        toor.mainloop()
##        toor.destroy()
        weight_machine = weight.get()
        jeans_dark = jeansdark.get()
        top_dark = topdark.get()
        sktr_dark = sktrdark.get()
        jeans_light = jeanslight.get()
        top_light = toplight.get()
        sktr_light = sktrlight.get()
        print weight_machine
        print jeans_dark
        print top_dark
        print sktr_dark
        print jeans_light
        print top_light
        print sktr_light
    def createwidgets(self):
        self.L1 = Label(root, text="Weight Machine").pack()
        self.E1 = Entry(root, bd = 3, textvariable = weight).pack()
        self.L2 = Label(root, text="Dark Jeans").pack()
        self.E2 = Entry(root, bd = 3, textvariable = jeansdark).pack()
        self.L3 = Label(root, text="Dark Tops").pack()
        self.E3 = Entry(root, bd = 3, textvariable = topdark).pack()
        self.L4 = Label(root, text="Dark Skirt/Trousers").pack()
        self.E4 = Entry(root, bd = 3, textvariable = sktrdark).pack()
        self.L5 = Label(root, text="Light Jeans").pack()
        self.E5 = Entry(root, bd = 3, textvariable = jeanslight).pack()
        self.L6 = Label(root, text="Light Tops").pack()
        self.E6 = Entry(root, bd = 3, textvariable = toplight).pack()
        self.L7 = Label(root, text="Light Skirt/Trousers").pack()
        self.E7 = Entry(root, bd = 3, textvariable = sktrlight).pack()
        enter = Button(root, text = "Enter", bg = "green",  command = self.user).pack()
        quitbox = Button(root, text = "Quit", bg = "red", command = root.quit).pack()

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createwidgets()

root.title("Washing Machine")
app = Application(master = root)
root.mainloop()
root.destroy()
