import tkinter as tk
from tkinter import ttk, filedialog
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import nglview as nv
from ipywidgets import Embed

# Declare global variables
text_area = None
display_section = None
list_section = None
right_pane = None  # Added this global variable

def create_model_tab():
    tab_index = len(notebook.tabs())
    model_tab = ttk.Frame(notebook)
    notebook.add(model_tab, text=f"Model Tab {tab_index + 1}")
    
    # Create a PanedWindow to separate left and right sections
    pane = ttk.PanedWindow(model_tab, orient="horizontal")
    pane.pack(fill="both", expand=True)
    
    # Left section
    left_frame = ttk.Frame(pane)
    pane.add(left_frame, weight=1)
    
    open_button = ttk.Button(left_frame, text="Open File", command=open_file)
    open_button.pack(fill="x", padx=10, pady=5)
    
    global text_area
    text_area = tk.Text(left_frame, wrap=tk.WORD)
    text_area.pack(fill="both", expand=True)
    
    save_button = ttk.Button(left_frame, text="Save", command=save_file)
    save_button.pack(fill="x", padx=10, pady=5)
    
    model_button = ttk.Button(left_frame, text="Model", command=render_model)
    model_button.pack(fill="x", padx=10, pady=5)
    
    # Right section
    right_frame = ttk.Frame(pane)
    pane.add(right_frame, weight=1)
    
    # Create a vertical PanedWindow within the right section
    global right_pane
    right_pane = ttk.PanedWindow(right_frame, orient="vertical")
    right_pane.pack(fill="both", expand=True)
    
    global display_section
    display_section = ttk.Label(right_pane, text="Display Section")
    right_pane.add(display_section)
    
    global list_section
    list_section = tk.Listbox(right_pane)
    right_pane.add(list_section)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
        except Exception as e:
            print(f"Error opening file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        content = text_area.get("1.0", tk.END)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            print(f"Error saving file: {e}")

def render_model():
    rna_codon_triplet = text_area.get("1.0", tk.END).strip()
    if is_valid_rna_codon_triplet(rna_codon_triplet):
        # Display the RNA sequence as a visual representation using nglview
        display_section.pack_forget()  # Remove the Label
        list_section.pack_forget()     # Remove the Listbox

        view = nv.NGLWidget()
        view.add_component(nv.TextStructure(rna_codon_triplet))
        view.center_view(component=0)
        view._remote_call('setSize', target='Widget', args=['100%', '100%'])
        view._remote_call('requestRebuild', target='Widget')
        
        view_container = ttk.Frame(right_pane)
        view_container.pack(fill="both", expand=True)
        view_container.columnconfigure(0, weight=1)
        view_container.rowconfigure(0, weight=1)
        
        # Convert the NGLWidget to an Embed widget for tkinter
        view_widget = Embed()
        view_widget.widget = view
        view_widget.pack(fill="both", expand=True)
        view_widget.grid(row=0, column=0, sticky="nsew")

    else:
        display_section.config(text="Invalid RNA Codon Triplet")

def is_valid_rna_codon_triplet(text):
    # Implement your validation logic here
    # Example: Check if the text contains valid RNA codon triplet characters
    valid_chars = set("ACGU")
    return all(char in valid_chars for char in text)

root = tk.Tk()
root.state("zoomed")  # Open in maximized state
root.title("Dashboard Application")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=create_model_tab)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Close", command=root.quit)

list_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="List", menu=list_menu)

# Configurable maximum number of tabs
max_tabs = 15

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create a default "Model" tab
create_model_tab()

root.mainloop()
