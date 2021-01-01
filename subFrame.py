import tkinter as tk
from tkinter import filedialog
from getSubFile import subDelay


class SubFrame(tk.Frame):
    def print_value(self, val):
        self.entry3.delete(-1, 'end')
        self.entry3.insert(0, str(val))

    def button_click(self):
        self.scale.set(self.entry3.get())
        subDelay(self.entry.get(), self.entry2.get(), self.entry3.get())

    def file_select(self):
        self.entry.delete(-1, 'end')
        self.file = filedialog.askopenfilename(
            initialdir="/Users/spvobl/Downloads/", title="Select Subtitle file", filetypes=(("sub files", "*.sub *.srt *.mpl *.webvtt *.dfxp *.txt"), ("all files", "*.*")))
        self.entry.insert(0, self.file)

    def save_file(self):
        self.entry2.delete(-1, 'end')
        self.file2 = filedialog.asksaveasfilename(
            initialdir="/Users/spvobl/Downloads/", title="Select Folder")
        if "srt" in self.file2 or "sub" in self.file2 or "mpl" in self.file2 or "webvtt" in self.file2 or "dfxp" in self.file2 or "txt" in self.file2:
            self.entry2.insert(0, self.file2)
        else:
            self.entry2.insert(0, self.file2+".srt")

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('1000x515')
        self.master.resizable(0, 0)
        self.master.title('Subtitle Delayer')
        self.label = tk.Label(self.master, text="Subtitle Delayer", font=(
            'Default', 40), bg="gray", width=40, pady=15)
        self.label2 = tk.Label(self.master, text="Enter Subtitle File",
                               font=('Default', 18, 'bold'))
        self.label3 = tk.Label(self.master, text="Enter New Name for Subtitle File",
                               font=('Default', 18, 'bold'))
        self.label4 = tk.Label(self.master, text="Delay Time",
                               font=('Default', 18, 'bold'))
        self.scale = tk.Scale(self.master, orient=tk.HORIZONTAL,
                              resolution=0.001, length=950, from_=-250, to=250, fg="black", command=self.print_value)  # -600, #600
        self.button = tk.Button(self.master, text="Create Subtitle File",
                                width=20, height=3, bg="red", activebackground="red", command=self.button_click, font=('default', 16, 'bold'))
        self.button2 = tk.Button(
            self.master, text="Select File", command=self.file_select)
        self.button3 = tk.Button(
            self.master, text="Save As", command=self.save_file)
        self.entry = tk.Entry(self.master, width=70)
        self.entry2 = tk.Entry(self.master, width=70)
        self.entry3 = tk.Entry(self.master, width=10)
        self.entry3.insert(0, "0.000")
        self.label.pack()
        self.label2.pack(pady=(20, 5))
        self.entry.pack()
        self.button2.pack(pady=(5, 0))
        self.label3.pack(pady=(20, 5))
        self.entry2.pack()
        self.button3.pack(pady=(5, 0))
        self.label4.pack(pady=(20, 0))
        self.scale.pack(anchor=tk.CENTER)
        self.entry3.pack(pady=10)
        self.button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    subFrame = SubFrame(master=root)
    subFrame.mainloop()
