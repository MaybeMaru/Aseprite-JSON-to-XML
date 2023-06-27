import tkinter as tk
from tkinter import filedialog
import customtkinter
from jsonxml import convert_json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class ScrollableLabelFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, **kwargs):
        super().__init__(master, **kwargs)

        self.label_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        label = customtkinter.CTkLabel(self, text=item)
        label.configure(anchor='w', justify='left')
        label.grid(row=0)
        self.label_list.append(label)

    def clear_items(self):
        for label in self.label_list:
            label.destroy()
            self.label_list.remove(label)
    
    def get_item_str(self):
        return self.label_list[0].cget('text')

# App config
app = customtkinter.CTk()
app.title('Aseprite JSON to XML Converter')
app.resizable(False, False)
app.geometry("535x375")

# Functions
def open_json(): # Set path string
    filename = filedialog.askopenfilename(initialdir="/", title="Select JSON", filetypes=(("JSON", "*.json"),("All Files", "*.*")))
    json_path_entry.delete(0, len(json_path_entry.get()))
    json_path_entry.insert(0, filename)

def _convert_json(): # Get converted XML string
    xml = convert_json(json_path_entry.get())
    scrollable_frame.clear_items()
    scrollable_frame.add_item(xml)

def save_xml(): # Save converted XML to path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xml",
        filetypes=[("XML", "*.xml"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(scrollable_frame.get_item_str())

# Elements placement
json_path_entry = customtkinter.CTkEntry(app, width=350)
json_path_entry.grid(padx=10, pady=10, row=0, column= 0)

json_button = customtkinter.CTkButton(app, text="Open JSON", command=open_json)
json_button.grid(padx=10, pady=0, row=0, column= 1)

export_button = customtkinter.CTkButton(app, text="Convert XML", command=_convert_json)
export_button.grid(padx=10, pady=0, row=1, column= 1, sticky=customtkinter.NW)

export_button = customtkinter.CTkButton(app, text="Save XML", command=save_xml)
export_button.grid(padx=10, pady=0, row=1, column= 1, sticky=customtkinter.SW)

scrollable_frame = ScrollableLabelFrame(app, width=325, height=300, item_list=[])
scrollable_frame.grid(padx=0, pady=0, row=1, column= 0)


app.mainloop()