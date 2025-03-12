import os
import tkinter as tk
from tkinter import messagebox
import glob
import shutil

# def revoke_file(self):
#     file_path = self.entry.get()
#     xml_files = glob.glob(os.path.join(file_path, '*.xml'))
#     for xml_file in xml_files:
#         logs = []
#         source = xml_file
#         wdir = os.path.dirname(source)
#         destination_dir = os.path.join(wdir, "prescript")
#         xml_backupfiles = glob.glob(os.path.join(destination_dir, '*-RAW.xml'))
#         print(xml_backupfiles)
#         for xml_backupfile in xml_backupfiles:
#             backup_source = xml_backupfile
#             destination = os.path.basename(backup_source).replace("-RAW.xml", ".xml")
#             destination = os.path.join(wdir, destination)
#             shutil.copy2(backup_source, destination)
#     if os.path.exists(destination_dir):
#         shutil.rmtree(destination_dir)
#     print("Revoke files")

def revoke_file(self):
    file_path = self.entry.get()
    destination_dir = os.path.join(file_path, "prescript")
    if not os.path.exists(destination_dir):
        print("No 'prescript' folder found. Nothing to revoke.")
        return
    xml_backupfiles = glob.glob(os.path.join(destination_dir, '*.xml'))
    if not xml_backupfiles:
        print("No XML files found in the 'prescript' folder.")
        return
    for xml_backupfile in xml_backupfiles:
        destination = os.path.join(file_path, os.path.basename(xml_backupfile))
        shutil.move(xml_backupfile, destination)
        print(f"Replaced: {destination}")
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    print("Revoked files completed.")