import tkinter as tk
import tkinterhtml as tkhtml

# Create a function to open the HTML file in a tkinter window
def open_html_viewer():
    # Create a tkinter window
    viewer_window = tk.Toplevel()
    viewer_window.title("RNA Structure Viewer")

    # Create a tkinterhtml widget to display the HTML content
    viewer_widget = tkhtml.HtmlFrame(viewer_window)
    viewer_widget.pack(fill=tk.BOTH, expand=True)

    # Load the HTML file into the tkinterhtml widget
    viewer_widget.set_content("rna_structure_viewer.html")

# Create the main application window
app = tk.Tk()
app.title("RNA Structure Viewer Application")

# Create a button to open the HTML viewer
open_button = tk.Button(app, text="Open RNA Structure Viewer", command=open_html_viewer)
open_button.pack(pady=10)

# Start the tkinter main loop for the application window
app.mainloop()
