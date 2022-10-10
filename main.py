import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from jsonxml import convert_json

root = tk.Tk()
root.title('Maru : Aseprite JSON to XML Converter')
root.resizable(False, False)

s = ttk.Style()
s.configure('.', font=('Arial', 11))

json_dir = ['No JSON File Loaded']

canvas = tk.Canvas(root, height = 400, width=600, bg="#828282")
canvas.pack()

def makeConsoleText(txt):
    print(txt)
    ConsoleText = tk.Label(scrollable_frame, text=txt, anchor='w')
    ConsoleText.pack(fill='both')

def clearWidgets(directory):
        for widget in directory.winfo_children():
            widget.destroy()

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

def open_JSON():
    json_dir.clear()
    clearWidgets(json_directory_frame)
    filename =filedialog.askopenfilename(initialdir="/", title="Select Aseprite JSON", filetypes=(("JSON", "*.json"),("All Files", "*.*")))
    if filename == "":
        json_dir.append('No JSON File Loaded')
        print('JSON NOT FOUND')
    else:
        json_dir.append(filename)
        print('LOADED '+json_dir[0])

    da_dir = tk.Label(json_directory_frame, text=json_dir, bg="#ffffff")
    da_dir.pack(side=tk.LEFT, fill='both')

def convert_JSON():
    if json_dir[0] == 'No JSON File Loaded':
        messagebox.showerror('Error', 'JSON File Not Found')
        return 'sexo'
    test = convert_json(json_dir[0])
    if test[0] == 'XML exported':
        makeConsoleText('XML Exported Succesfully In '+test[1])
    else:
        makeConsoleText('ERROR EXPORTING XML')

#Add Version Text
version = 'v0.1.1'
canvas.create_text(30, 20, text=version, fill="white", font=('Arial 10'), anchor='w')
canvas.pack(fill='both')

json_directory_frame = tk.Frame(root, bg="#bdbdbd")
json_directory_frame.place(relwidth=0.66, relheight=0.15, x=30, y=40)

json_button_frame = tk.Frame(root, bg="#bdbdbd")
json_button_frame.place(relwidth=0.2, relheight=0.15, x=450, y=40)
json_button = tk.Button(json_button_frame, text="Open Aseprite JSON", padx=100, pady=20, fg="black", bg = "white", command=open_JSON).pack()

export_button_frame = tk.Frame(root, bg="#bdbdbd")
export_button_frame.place(relwidth=0.2, relheight=0.15, x=450, y=120)
export_button = tk.Button(export_button_frame, text="Export XML", padx=100, pady=20, fg="black", bg = "white", command=convert_JSON).pack()

def_text = tk.Label(json_directory_frame, text=json_dir[0], bg="#ffffff")
def_text.pack(side=tk.LEFT, fill='both')

console_frame = tk.Frame(root, bg="#bdbdbd")
console_frame.place(relwidth=0.66, relheight=0.6, x=30, y=120)

#Console
container = ttk.Frame(console_frame)
scrollcanvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=scrollcanvas.yview)
scrollable_frame = ttk.Frame(scrollcanvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: scrollcanvas.configure(
        scrollregion=scrollcanvas.bbox("all")
    )
)

scrollcanvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollcanvas.configure(yscrollcommand=scrollbar.set)

container.pack()
scrollcanvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()