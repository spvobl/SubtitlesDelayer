import tkinter as tk
from getSubFile import subDelay


class SubFrame(tk.Frame):
    def print_value(self, val):
        self.entry3.delete(-1, 'end')
        self.entry3.insert(0, str(val))

    def button_click(self):
        self.scale.set(self.entry3.get())
        subDelay(self.entry.get(), self.entry2.get(), self.entry3.get())

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('1000x525')
        self.master.resizable(0, 0)
        self.master.title('Subtitle Delayer')
        self.label = tk.Label(self.master, text="Subtitle Delayer", font=(
            'Default', 40), bg="gray", width=40, pady=10)
        self.label2 = tk.Label(self.master, text="Enter Subtitle File",
                               font=('Default', 18, 'bold'))
        self.label3 = tk.Label(self.master, text="Enter New Name for Subtitle File",
                               font=('Default', 18, 'bold'))
        self.label4 = tk.Label(self.master, text="Delay Time",
                               font=('Default', 18, 'bold'))
        self.scale = tk.Scale(self.master, orient=tk.HORIZONTAL,
                              resolution=0.001, length=950, from_=-250, to=250, command=self.print_value)  # -600, #600
        self.button = tk.Button(self.master, text="Create Subtitle File",
                                width=20, height=3, bg="red", activebackground="red", command=self.button_click, font=('default', 16, 'bold'))
        self.entry = tk.Entry(self.master, width=70)
        self.entry2 = tk.Entry(self.master, width=70)
        self.entry3 = tk.Entry(self.master, width=10)
        self.entry3.insert(0, "0.000")
        self.label.pack()
        self.label2.pack(pady=(35, 5))
        self.entry.pack()
        self.label3.pack(pady=(35, 5))
        self.entry2.pack()
        self.label4.pack(pady=(35, 0))
        self.scale.pack(anchor=tk.CENTER)
        self.entry3.pack(pady=10)
        self.button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    subFrame = SubFrame(master=root)
    subFrame.mainloop()
