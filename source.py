from tkinter import *
from tkinter import filedialog

filename = None

aditor_about_text = "\
This is a Simple Text Editor \n\
Developed and Designed by ADITYA JAIN. \n\
You can create any kind(extension) of file using this Editor."

aditor_version_text = "version 1.0"


def about_aditor(*args):
    textArea.delete(1.0, END)
    textArea.insert(1.0, aditor_about_text)
    set_title("Aditor: TextEditor --about")


def version_aditor(*args):
    textArea.delete(1.0, END)
    textArea.insert(1.0, aditor_version_text)
    set_title("Aditor: TextEditor --version")


def exit_aditor(*args):
    window.destroy()


def shortcut_keys():
    textArea.bind('<Control-n>', new_file)
    textArea.bind('<Control-o>', open_file)
    textArea.bind('<Control-s>', save_file)
    textArea.bind('<Alt-x>', exit_aditor)
    textArea.bind('<Control-e>', about_aditor)
    textArea.bind('<Control-i>', version_aditor)


def set_title(title=None):
    if title:
        window.title(title)
    else:
        window.title("Aditor: TextEditor")


def new_file(*args):
    global filename
    filename = None
    set_title()
    textArea.delete(1.0, END)


def open_file(*args):
    global filename
    filename = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"),
                   ("Text Files", "*.txt"),
                   ("Python Files", "*.py"),
                   ("C Files", "*.c"),
                   ("Cpp Files", "*.cpp"),
                   ("Java Files", "*.java"),
                   ("HTML Files", "*.html"),
                   ("CSS Files", "*.css"),
                   ("XML Files", "*.xml"),
                   ("Java Script Files", "*.js"),
                   ("Markdown Files", "*.md")])

    if filename:
        set_title(filename)
        textArea.delete(1.0, END)
        with open(filename, 'r') as f:
            textArea.insert(1.0, f.read())


def save_file(*args):
    global filename

    if not filename:
        filename = filedialog.asksaveasfilename(
            initialfile="TextFile.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Files", "*.py"),
                       ("C Files", "*.c"),
                       ("Cpp Files", "*.cpp"),
                       ("Java Files", "*.java"),
                       ("HTML Files", "*.html"),
                       ("CSS Files", "*.css"),
                       ("XML Files", "*.xml"),
                       ("Java Script Files", "*.js"),
                       ("Markdown Files", "*.md")])

    with open(filename, "w") as f:
        f.write(textArea.get(1.0, END))

    set_title(filename)


window = Tk()
window.title("Aditor: TextEditor")
window.geometry("900x500")

menuBar = Menu(window)
window.config(menu=menuBar)

mi_file = Menu(menuBar, font=("arial", 10), tearoff=0)
menuBar.add_cascade(label="File", menu=mi_file)
mi_file.add_command(label="New", command=new_file, accelerator="Ctrl+N")
mi_file.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
mi_file.add_separator()
mi_file.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
mi_file.add_separator()
mi_file.add_command(label="Exit", command=exit_aditor, accelerator="Alt+X")

mi_help = Menu(menuBar, font=("arial", 10), tearoff=0)
menuBar.add_cascade(label="Help", menu=mi_help)
mi_help.add_command(label="About this Editor", command=about_aditor, accelerator="Ctrl+E")
mi_help.add_command(label="Version", command=version_aditor, accelerator="Ctrl+I")

textArea = Text(window, font=("Arial Rounded MT Bold", 20))
textArea.focus_set()
textArea.pack(fill=BOTH, side=LEFT, expand=True)

shortcut_keys()

window.mainloop()
