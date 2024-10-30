import tkinter as tk
from ui import setup_ui

def main():
    window = tk.Tk()
    window.title("Simple Calculator GUI")
    window.geometry("600x650")
     
    
    setup_ui(window)  # Call the function from `ui.py` to set up the UI
    window.mainloop()

if __name__ == "__main__":
    main()


