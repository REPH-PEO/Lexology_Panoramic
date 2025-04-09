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
import createreport
import createexcel
import deletexlsx
import time
import urlfix
# import listfix

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lexology Panoramic® ")
        self.geometry("500x300")
        self.resizable(False, False)  
        self.configure(bg="#05162a", highlightbackground="white", borderwidth=1, relief="solid", highlightthickness=2, highlightcolor="black")
        # self.iconbitmap(r'C:\Users\labradbm\Downloads\Local\YB\Python\Lexology Panoramic Automation\Codes\Lexology_Panoramic\logo4.ico')
        self.iconbitmap(r'\\fabwebd5.net\neptune\DataConversion\Tools\Lexology_Panoramic\Main\logo4.ico')
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)
        help_menu = tk.Menu(main_menu, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a tool to clean up XML files and generate reports.\nVersion: 1.0\nDeveloped by: Lester & BRi\nProject Manager: Red\nBusiness Analyst: Ela\nFor issues and concerns, please contact: lesterjohn.reyes@reedelsevier.com or brian.labrador@reedelsevier.com"))
        help_menu.add_command(label="Guide", command=lambda: messagebox.showinfo("Guide", "1. Enter the path of the XML file or folder containing XML files.\n2. Click Submit to start the process.\n3. Click Revoke to undo the process.\n4. Click Rerun to start a new process.\n5. Click Exit to close the application."))
        main_menu.insert_cascade(0, label="Help", menu=help_menu)    
        self.main_frame = tk.Frame(self, bg="#223556", width=150 , height=50)
        self.main_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        self.main_frame1 = tk.Frame(self.main_frame, bg="#223556", width=300, height=50)
        self.main_frame1.pack(side="top", expand=True, fill="both", padx=5, pady=5)
        # self.image_file = r'C:\Users\labradbm\Downloads\Local\YB\Python\Lexology Panoramic Automation\Codes\lex1.png'
        self.image_file = r'\\fabwebd5.net\neptune\DataConversion\Tools\Lexology_Panoramic\Main\lex1.png'
        self.image = Image.open(self.image_file)
        self.image = self.image.resize((50, 50))  # Resize to desired size
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.main_frame1, image=self.photo, bg="#223556")
        self.image_label.pack(side="left", padx=10)
        self.main_label = Label(self.main_frame1, text="XML and Metadata Clean Up Tool", font=("Corporate", 18), bg="#223556", fg="white")
        self.main_label.pack(side="bottom", padx=10, pady=10)
        self.sub_frame1 = tk.Frame(self.main_frame, bg="#223556")
        self.sub_frame1.pack(side="top", expand=False, fill="both", padx=5, pady=5)
        self.entry = tk.Entry(self.sub_frame1, width=70, font=("Arial", 8))
        self.entry.pack(pady=10, side="top", anchor="w", expand=True, fill="both")
        self.submit_button = tk.Button(self.sub_frame1, text="Submit", font=("Gagalin", 10), command=self.check_path, width=13, height=2)
        self.submit_button.pack(pady=10, padx=10, side="left", anchor="w")
        self.Revoke_button = tk.Button(self.sub_frame1, text="Revoke", command=self.check_pathrevoke, width=13, height=2)
        self.Revoke_button.pack(padx=10, side="left", anchor="w")
        self.rerun_button = tk.Button(self.sub_frame1, text="Rerun", command=self.refresh_run, width=13, height=2)
        self.rerun_button.pack(padx=10, side="left", anchor="w")
        self.exit_app_button = tk.Button(self.sub_frame1, text="Exit", command=self.exit_app, width=13, height=2)
        self.exit_app_button.pack(padx=10, side="left", anchor="w")
        self.sub_frame4 = tk.Frame(self.main_frame, bg="gray", width=150, height=100)
        self.sub_frame4.pack(side="top", expand=False, fill="both", padx=5, pady=5) 
        self.sub_frame3 = tk.Frame(self.main_frame, bg="#223556")
        self.sub_frame3.pack(side="top", expand=True, fill="both", padx=5, pady=5)               
        self.sub_frame2 = tk.Frame(self.main_frame, bg="#223556")
        self.sub_frame2.pack(side="top", expand=False, fill="both", padx=5, pady=5)
        self.percent_label = Label(self.sub_frame3, text="0%", font=("Arial", 8), bg="#223556", fg="white", height=1)
        self.percent_label.pack(pady=1, side="top", anchor="n")         
        self.progress_bar = tk.Scale(self.sub_frame4, orient="horizontal", length=525, sliderlength=10, 
                                     bg="#223556", highlightbackground="#223556")
        self.progress_bar.set(0)  
        self.progress_bar.pack(side="bottom", anchor="w", expand=True)

    def exit_app(self):
        self.destroy()

    def check_path(self):
        checkout_folder = self.entry.get()
        if os.path.exists(checkout_folder):
            if os.path.isdir(checkout_folder):
                xml_files = [f for f in os.listdir(checkout_folder) if f.endswith('.xml')]
                if not xml_files:
                    messagebox.showerror("Error", "No XML files found in the folder.")
                    return
            elif os.path.isfile(checkout_folder):
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
                    urlfix.wrap_core_url(self)
                    # listfix.fix_core_list(self)
                    for i in range(101):  
                                    self.progress_bar.set(i)  
                                    self.percent_label.configure(text=f"{i}% Process Complete!")  
                                    self.update_idletasks() 
                                    time.sleep(0.0001)  
                    self.submit_button.configure(state="disabled", text="Complete") 
                    self.Revoke_button.configure(state="normal", text="Revoke")
                    self.rerun_button.configure(state="normal", text="Rerun")
                    self.exit_app_button.configure(state="normal", text="Exit")
                    print("Process Complete!") 
        else:
            messagebox.showerror("Error", "Invalid path")    
                        
        messagebox.showinfo("Complete", "Process Complete!")             

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
                    for i in range(101):  
                        self.progress_bar.set(i)  
                        self.percent_label.configure(text=f"{i}% Process Complete!")
                        self.update_idletasks() 
                        time.sleep(0.0001)                     
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
            messagebox.showinfo("Complete", "Revoke Complete!")              

    def refresh_run(self):
        self.submit_button.configure(state="normal", text="Submit")    
        self.entry.delete(0, tk.END)  
        messagebox.showinfo("Re-run", "You can do another Clean up.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
