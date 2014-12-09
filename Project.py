'''Project'''
from Tkinter import *
root = Tk()
weight_machine = int()
jeans_dark = int()
top_dark = int()
sktr_dark = int()
jeans_light = int()
top_light = int()
sktr_light = int()
weight = IntVar()
jeansdark = IntVar()
topdark = IntVar()
sktrdark = IntVar()
jeanslight = IntVar()
toplight = IntVar()
sktrlight = IntVar()
class Application(Frame):
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
        enter = Button(root, text = "Enter", bg = "green",  command = self.washingmachine).pack()
        quitbox = Button(root, text = "Quit", bg = "red", command = root.quit).pack()

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createwidgets()

    def washingmachine(self):
        weight_machine = weight.get()
        jeans_dark = jeansdark.get()
        top_dark = topdark.get()
        sktr_dark = sktrdark.get()
        jeans_light = jeanslight.get()
        top_light = toplight.get()
        sktr_light = sktrlight.get()
        self.answer = ""
        self.washround, self.nextround = 0, 0
        self.dark = (jeans_dark*550)+(top_dark*200)+(sktr_dark*300)
        self.light = (jeans_light*550)+(top_light*200)+(sktr_light*300)
        if self.dark > 0 and self.light > 0:
            while self.dark > weight_machine:
                self.washround += 1
                self.dark -= weight_machine
            while self.dark > (weight_machine/2):
                self.washround += 1
                self.dark -= weight_machine
            if self.dark > 0:
                self.nextround += 1
            self.answer = "Washing dark clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround)
            self.result = Label(root, text = self.answer).pack()
            self.washround = 0
            self.nextround = 0
            while self.light > weight_machine:
                self.washround += 1
                self.light -= weight_machine
            while self.light > (weight_machine/2):
                self.washround += 1
                self.light -= weight_machine
            if self.light > 0:
                self.nextround += 1
            self.answer = "Washing light clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround)
            self.result = Label(root, text = self.answer).pack()
        elif self.dark > 0 and self.light == 0:
            while self.dark > weight_machine:
                self.washround += 1
                self.dark -= weight_machine
            while self.dark > (weight_machine/2):
                self.washround += 1
                self.dark -= weight_machine
            if self.dark > 0:
                self.nextround += 1
            self.answer = "Washing dark clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround)
            self.result = Label(root, text = self.answer).pack()
        elif self.light > 0 and self.dark == 0:
            while self.light > weight_machine:
                self.washround += 1
                self.light -= weight_machine
            while self.light > (weight_machine/2):
                self.washround += 1
                self.light -= weight_machine
            if self.light > 0:
                self.nextround += 1
            self.answer = "Washing light clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround)
            self.result = Label(root, text = self.answer).pack()

root.title("Washing Machine")
root.geometry("400x400")
app = Application(master = root)
root.mainloop()
root.destroy()
