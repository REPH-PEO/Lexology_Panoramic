import tkinter as tk
from tkinter import messagebox, PhotoImage, Label
from PIL import Image, ImageTk
import pandas as pd
from openpyxl.utils import get_column_letter
from datetime import datetime
import os
import backupfiles as bf
import revoke
import deletetxt
import createexcel
import deletexlsx
import createreport


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lexology Panoramic")
        self.geometry("800x500")
        self.resizable(False, False)  
        self.configure(bg="#05162a", highlightbackground="white", borderwidth=1, relief="solid", highlightthickness=2, highlightcolor="black")
        self.iconbitmap(r'C:\Users\labradbm\Downloads\Local\YB\Python\Lexology Panoramic Automation\Codes\Lexology_Panoramic\logo4.ico')
        # self.iconbitmap(r'\\fabwebd5.net\neptune\DataConversion\Tools\Lexology_Panoramic\Main\logo4.ico')
        self.sidebar_frame = tk.Frame(self, width=200, height=10, highlightbackground="black", borderwidth=1, relief="solid", bg="#223556")
        self.sidebar_frame.pack(side="left", fill="y", padx=10, pady=10)
        self.sidebar_label = Label(self.sidebar_frame, text="Notes:", font=("Arial", 16), bg="#223556", fg="white")
        self.sidebar_label.pack(pady=20)
        self.sidebar_frame1 = tk.Frame(self.sidebar_frame, width=200, height=500, background="#223556")
        self.sidebar_frame1.pack(side="bottom", fill="y", padx=10, pady=10)
        self.sidebar_frame2 = tk.Frame(self.sidebar_frame1, width=200, height=20, bg="#223556")
        self.sidebar_frame2.pack(side="top", fill="y", padx=10, pady=10)
        self.sidebar_note = Label(self.sidebar_frame1, width=50, height=10, bg="#223556", fg="white")
        self.sidebar_note.place(x=5, y=5, anchor="e")
        self.sidebar_note1 = Label(self.sidebar_frame1, width=50, height=10, bg="#223556")
        self.sidebar_note1.place(x=10, y=10, anchor="n")
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)
        help_menu = tk.Menu(main_menu, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Guide", command=self.show_guide)
        main_menu.insert_cascade(0, label="Help", menu=help_menu)    
        self.main_frame = tk.Frame(self, bg="#223556", width=150 , height=50)
        self.main_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        self.main_frame1 = tk.Frame(self.main_frame, bg="#223556")
        self.main_frame1.pack(side="top", expand=True, fill="both", padx=5, pady=5)
        # self.image_file = r'C:\Users\labradbm\Downloads\Local\YB\Python\Lexology Panoramic Automation\Codes\lex1.png'
        # self.image = Image.open(self.image_file)
        # # self.image = self.image.resize((50, 50))  # Resize to desired size
        # # self.photo = ImageTk.PhotoImage(self.image)
        # self.image_label = Label(self.main_frame1, image=self.photo, bg="#223556")
        # self.image_label.pack(side="left", padx=10)
        self.main_label = Label(self.main_frame1, text="XML and Metadata Clean Up Tool", font=("Arial", 18), bg="#223556", fg="white")
        self.main_label.pack(side="bottom", padx=10, pady=10)
        self.sub_frame1 = tk.Frame(self.main_frame, bg="#223556")
        self.sub_frame1.pack(side="top", expand=False, fill="both", padx=5, pady=5)
        self.entry = tk.Entry(self.sub_frame1, width=70, font=("Arial", 8))
        # self.entry.insert(0, "XML files: Enter the folder path here")
        self.entry.pack(pady=10, side="top", anchor="w", expand=True, fill="both")
        self.submit_button = tk.Button(self.sub_frame1, text="Submit", command=self.check_path, width=15, height=2)
        self.submit_button.pack(pady=10, padx=10, side="left", anchor="w")
        self.Revoke_button = tk.Button(self.sub_frame1, text="Revoke", command=self.check_pathrevoke, width=15, height=2)
        self.Revoke_button.pack(padx=10, side="left", anchor="w")
        self.rerun_button = tk.Button(self.sub_frame1, text="Rerun", command=self.refresh_run, width=15, height=2)
        self.rerun_button.pack(padx=10, side="left", anchor="w")
        self.exit_app_button = tk.Button(self.sub_frame1, text="Exit", command=self.exit_app, width=15, height=2)
        self.exit_app_button.pack(padx=10, side="left", anchor="w")

        self.sub_frame4 = tk.Frame(self.main_frame, bg="gray", width=150, height=100)
        self.sub_frame4.pack(side="top", expand=False, fill="both", padx=5, pady=5)        
        self.sub_frame2 = tk.Frame(self.main_frame, bg="#223556")
        self.sub_frame2.pack(side="top", expand=False, fill="both", padx=5, pady=5)
        # Create and place the progress bar
        # self.progress_bar = tk.Scale(self.sub_frame2, from_=0, to=100, orient="horizontal", length=525, showvalue=1, sliderlength=20, 
        #                              bg="#223556", fg="white", troughcolor="#7daaf8", highlightbackground="black")
        # self.progress_bar.set(0)  # Initial progress set to 0%
        # self.progress_bar.pack(side="bottom", anchor="w", expand=True)
        # Create and place the status label
        self.sub_frame3 = tk.Frame(self.main_frame, bg="#223556")
        self.sub_frame3.pack(side="top", expand=True, fill="both", padx=5, pady=5)
        self.sidebar_ver = Label(self.sub_frame2, width=150, height=10, bg="#223556", fg="white")
        self.sidebar_ver.pack(pady=10, expand=True, anchor="w", fill="both")
        self.percent_label = Label(self.sub_frame3, text="0%", font=("Arial", 5), bg="#223556", fg="white", height=1)
        self.percent_label.pack(pady=1, side="top", anchor="n")        
    
    def exit_app(self):
        self.destroy()

    def show_about(self):
        messagebox.showinfo("About", "Lexology Panoramic Automation Tool\nVersion 1.0\nDeveloped by: Lester & BRi\nProject Manager: Red\nBusiness Analyst: Ela\n© 2025 Lexology Panoramic")

    def show_guide(self):
        messagebox.showinfo("Guide", "This tool will do XML cleanup, Metadata checks & fixing of any invalid Tables")

    def check_path(self):
        checkout_folder = self.entry.get()
        if os.path.exists(checkout_folder):
            if os.path.isdir(checkout_folder):
                xml_files = [f for f in os.listdir(checkout_folder) if f.endswith('.xml')]
                if not xml_files:
                    messagebox.showerror("Error", "No XML files found in the folder.")
                    return
            elif os.path.isfile(checkout_folder):
                # Check if the single file is an XML file
                if not checkout_folder.endswith('.xml'):
                    messagebox.showerror("Error", "The specified file is not an XML file.")
                    return
            else:
                messagebox.showerror("Error", "Invalid path.")
                return            
            if messagebox.askyesno("Confirm", "Make sure that the xml file is not open before you proceed!"):
                    self.submit_button.configure(state="disabled", text="Processing...")
                    self.Revoke_button.configure(state="disabled", text="Revoke")
                    self.rerun_button.configure(state="disabled", text="rerun")
                    self.exit_app_button.configure(state="disabled", text="Exit")
                    bf.backup_file(self)
                    createreport.create_report(self)
                    createexcel.create_xlsreport(self)
                    deletetxt.delete_txtfiles(self)
                    self.submit_button.configure(state="disabled", text="Complete") 
                    self.Revoke_button.configure(state="normal", text="Revoke")
                    self.rerun_button.configure(state="normal", text="Rerun")
                    self.exit_app_button.configure(state="normal", text="Exit")
                    print("Process Complete!") 
        else:
            messagebox.showerror("Error", "Invalid path")    

    def check_pathrevoke(self):
            checkout_folder = self.entry.get()
            if os.path.exists(checkout_folder):
                if os.path.isdir(checkout_folder):
                    xml_files = [f for f in os.listdir(checkout_folder) if f.endswith('.xml')]
                    if not xml_files:
                        messagebox.showerror("Error", "No XML files found in the directory.")
                        return
                    backup_folder_path = os.path.join(checkout_folder, "prescript")
                    if not os.path.exists(backup_folder_path) or not os.path.isdir(backup_folder_path):
                        messagebox.showerror("Error", "Not processed or already revoked.")
                        return
                elif os.path.isfile(checkout_folder):
                    if not checkout_folder.endswith('.xml'):
                        messagebox.showerror("Error", "The specified file is not an XML file.")
                        return
                else:
                    messagebox.showerror("Error", "Invalid path.")
                    return          
                if messagebox.askyesno("Confirm", "Proceed?"):
                    self.submit_button.configure(state="disabled", text="Complete")
                    self.Revoke_button.configure(state="disabled", text="Processing...")
                    self.rerun_button.configure(state="disabled", text="Rerun")
                    self.exit_app_button.configure(state="disabled", text="Exit")
                    revoke.revoke_file(self)
                    deletexlsx.delete_xlsx(self)
                    deletetxt.delete_txtfiles(self)
                    self.submit_button.configure(state="normal", text="Submit")
                    self.Revoke_button.configure(state="normal", text="Revoke")
                    self.rerun_button.configure(state="normal", text="Rerun")
                    self.exit_app_button.configure(state="normal", text="Exit")
                    print("Revoke Complete!")            
            else:
                messagebox.showerror("Error", "Invalid path")

    def refresh_run(self):
        self.submit_button.configure(state="normal", text="Submit")    
        self.entry.delete(0, tk.END)  
        messagebox.showinfo("Re-run", "You can do another Clean up.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
