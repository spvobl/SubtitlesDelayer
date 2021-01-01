import tkinter as tk
from tkinter import filedialog
from getSubFile import subDelay


class SubFrame(tk.Frame):
    def print_value(self, val):
        self.timeDelayEntry.delete(-1, 'end')
        self.timeDelayEntry.insert(0, str(val))

    def button_click(self):
        self.scale.set(self.timeDelayEntry.get())
        subDelay(self.enterFileEntry.get(),
                 self.saveFileEntry.get(), self.timeDelayEntry.get())

    def file_select(self):
        self.enterFileEntry.delete(-1, 'end')
        self.file = filedialog.askopenfilename(
            initialdir="/Users/spvobl/Downloads/", title="Select Subtitle file", filetypes=(("sub files", "*.sub *.srt *.mpl *.webvtt *.dfxp *.txt"), ("all files", "*.*")))
        self.enterFileEntry.insert(0, self.file)

    def save_file(self):
        self.saveFileEntry.delete(-1, 'end')
        self.newFile = filedialog.asksaveasfilename(
            initialdir="/Users/spvobl/Downloads/", title="Select Folder")
        if "srt" in self.newFile or "sub" in self.newFile or "mpl" in self.newFile or "webvtt" in self.newFile or "dfxp" in self.newFile or "txt" in self.newFile:
            self.saveFileEntry.insert(0, self.newFile)
        else:
            self.saveFileEntry.insert(0, self.newFile+".srt")

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('1000x515')
        self.master.resizable(0, 0)
        self.master.title('Subtitle Delayer')
        self.title = tk.Label(self.master, text="Subtitle Delayer", font=(
            'Default', 40), bg="gray", width=40, pady=15)
        self.enterSubFileLabel = tk.Label(self.master, text="Enter Subtitle File",
                                          font=('Default', 18, 'bold'))
        self.newSubFileLabel = tk.Label(self.master, text="Enter New Name for Subtitle File",
                                        font=('Default', 18, 'bold'))
        self.delayTimeLabel = tk.Label(self.master, text="Delay Time",
                                       font=('Default', 18, 'bold'))
        self.scale = tk.Scale(self.master, orient=tk.HORIZONTAL,
                              resolution=0.001, length=950, from_=-250, to=250, fg="black", command=self.print_value)  # -600, #600
        self.createSubButton = tk.Button(self.master, text="Create Subtitle File",
                                         width=20, height=3, bg="red", activebackground="red", command=self.button_click, font=('default', 16, 'bold'))
        self.selectFileButton = tk.Button(
            self.master, text="Select File", command=self.file_select)
        self.saveFileButton = tk.Button(
            self.master, text="Save As", command=self.save_file)
        self.enterFileEntry = tk.Entry(self.master, width=70)
        self.saveFileEntry = tk.Entry(self.master, width=70)
        self.timeDelayEntry = tk.Entry(self.master, width=10)
        self.timeDelayEntry.insert(0, "0.000")
        self.title.pack()
        self.enterSubFileLabel.pack(pady=(20, 5))
        self.enterFileEntry.pack()
        self.selectFileButton.pack(pady=(5, 0))
        self.newSubFileLabel.pack(pady=(20, 5))
        self.saveFileEntry.pack()
        self.saveFileButton.pack(pady=(5, 0))
        self.delayTimeLabel.pack(pady=(20, 0))
        self.scale.pack(anchor=tk.CENTER)
        self.timeDelayEntry.pack(pady=10)
        self.createSubButton.pack()


if __name__ == "__main__":
    root = tk.Tk()
    subFrame = SubFrame(master=root)
    subFrame.mainloop()
