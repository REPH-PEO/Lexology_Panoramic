import os
import tkinter as tk
from tkinter import messagebox
import glob
import shutil

def revoke_file(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        logs = []
        source = xml_file
        wdir = os.path.dirname(source)
        destination_dir = os.path.join(wdir, "prescript")
        xml_backupfiles = glob.glob(os.path.join(destination_dir, '*-RAW.xml'))
        print(xml_backupfiles)
        for xml_backupfile in xml_backupfiles:
            backup_source = xml_backupfile
            destination = os.path.basename(backup_source).replace("-RAW.xml", ".xml")
            destination = os.path.join(wdir, destination)
            shutil.copy2(backup_source, destination)
    
    # Delete the 'prescript' folder after files are transferred
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    print("Revoke files")
