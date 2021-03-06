'''Project'''
from Tkinter import *
import tkMessageBox
root = Tk()
weight = IntVar()
jeansdark = IntVar()
topdark = IntVar()
sktrdark = IntVar()
jeanslight = IntVar()
toplight = IntVar()
sktrlight = IntVar()
weight_machine = int()
jeans_dark = int()
top_dark = int()
sktr_dark = int()
jeans_light = int()
top_light = int()
sktr_light = int()
menubar = Menu(root)
class Application(Frame):
    def createwidgets(self):
        self.tkimage = PhotoImage(file = 'background.gif')
        self.bg = Label(root, image = self.tkimage).place(height = 350, width = 250)
        self.L1 = Label(root, text="Weight Machine", bg = 'violet').pack()
        self.E1 = Entry(root, width = 25, bd = 3, textvariable = weight).pack(expand=YES)
        self.L2 = Label(root, text="Dark Jeans", bg = 'dark blue', fg = 'white').pack()
        self.E2 = Entry(root, width = 25, bd = 3, textvariable = jeansdark).pack(expand=YES)
        self.L3 = Label(root, text="Dark Tops", bg = 'black', fg = 'white').pack()
        self.E3 = Entry(root, width = 25, bd = 3, textvariable = topdark).pack(expand=YES)
        self.L4 = Label(root, text="Dark Skirt/Trousers", bg = 'gray', fg = 'white').pack()
        self.E4 = Entry(root, width = 25, bd = 3, textvariable = sktrdark).pack(expand=YES)
        self.L5 = Label(root, text="Light Jeans", bg = 'light blue').pack()
        self.E5 = Entry(root, width = 25, bd = 3, textvariable = jeanslight).pack(expand=YES)
        self.L6 = Label(root, text="Light Tops", bg = 'light pink', fg = 'white').pack()
        self.E6 = Entry(root, width = 25, bd = 3, textvariable = toplight).pack(expand=YES)
        self.L7 = Label(root, text="Light Skirt/Trousers", bg = 'light yellow').pack()
        self.E7 = Entry(root, width = 25, bd = 3, textvariable = sktrlight).pack(expand=YES)
        enterbox = Button(root, text = "Enter", bg = "green", command = self.washingmachine).pack(side=LEFT, expand=YES)
        setbox = Button(root, text = "Reset Value!", bg = "dark orange", command = self.setvalue).pack(side=LEFT, expand=YES)
        quitbox = Button(root, text = "Exit", bg = "red", command = root.quit).pack(side=LEFT, expand=YES)

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.place()
        self.pack()
        self.washingmachine()
        self.createwidgets()
        self.menu()

    def setvalue(self):
        weight_machine = weight.set(0)
        jeans_dark = jeansdark.set(0)
        top_dark = topdark.set(0)
        sktr_dark = sktrdark.set(0)
        jeans_light = jeanslight.set(0)
        top_light = toplight.set(0)
        sktr_light = sktrlight.set(0)

    def washingmachine(self):
        weight_machine = weight.get() * 1000
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
            self.ans1 = "Washing dark clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround)
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
            self.ans2 = "Washing light clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround)
            tkMessageBox.showinfo("Result", (str(self.ans1 + " ") + str(self.ans2)))
        elif self.dark > 0 and self.light == 0:
            while self.dark > weight_machine:
                self.washround += 1
                self.dark -= weight_machine
            while self.dark > (weight_machine/2):
                self.washround += 1
                self.dark -= weight_machine
            if self.dark > 0:
                self.nextround += 1
            tkMessageBox.showinfo("Result", "Washing dark clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround))
        elif self.light > 0 and self.dark == 0:
            while self.light > weight_machine:
                self.washround += 1
                self.light -= weight_machine
            while self.light > (weight_machine/2):
                self.washround += 1
                self.light -= weight_machine
            if self.light > 0:
                self.nextround += 1
            tkMessageBox.showinfo("Result", "Washing light clothes this time " + str(self.washround) + ", And keep to wash next time " + str(self.nextround))
    def help(self):
        toor = Tk()
        toor.title("Help")
        toor.geometry("450x270")
        toor.resizable(width=FALSE, height=FALSE)
        self.aboutproject = "\n This application will help you to decide \n if you put the clothes into the washing machine,it is worthwhile or not."
        self.suggestenter = "This application have 7 inputs are... \n Weight Machine => Capacity of washing machine (input -> integer) \n Dark Jeans => Piece of dark jeans (input -> integer)" +\
                            "\n Dark Tops => Piece of dark tops (input -> integer) \n Dark Skirt/Trousers => Piece of dark skirts or trousers (input -> integer) \n Light Jeans => Piece of light jeans (input -> integer)" +\
                            "\nLight Tops => Piece of light tops (input -> integer) \n Light Skirt/Trousers  => Piece of light skirts or trousers (input -> integer)"
        self.suggestbutton = "And 3 main buttons are...\n Enter => When you put values and want to calculate \n Reset Values => reset all values \n Exit => Close this application"
        text1 = Label(toor, text=self.aboutproject).pack()
        text2 = Label(toor, text=self.suggestenter).pack()
        text3 = Label(toor, text=self.suggestbutton).pack()
    def menu(self):
        optionmenu = Menu(menubar, tearoff = 0)
        optionmenu.add_command(label = "Reset Value", command = self.setvalue)
        optionmenu.add_separator()
        optionmenu.add_command(label = "Exit", command = root.quit)
        menubar.add_cascade(label = "Option", menu = optionmenu)
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Help", command = self.help)
        menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu=menubar)
root.title("Washing Calculator")
root.geometry("250x350")
root.resizable(width=FALSE, height=FALSE)
app = Application(master = root)
root.mainloop()
root.destroy()
