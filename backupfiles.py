import os
import glob
import shutil

# def backup_file(self):
#     file_path = self.entry.get()
#     xml_files = glob.glob(os.path.join(file_path, '*.xml'))
#     for xml_file in xml_files:
#         wdir = os.path.dirname(xml_file)
#         destination_dir = os.path.join(wdir, "prescript")
#         if not os.path.exists(destination_dir):
#             os.mkdir(destination_dir)
#         destination = os.path.basename(xml_file).replace(".xml", "-RAW.xml")
#         destination = os.path.join(destination_dir, destination)
#         shutil.copyfile(xml_file, destination)
#         print(f"Backup file created at: {destination}")

def backup_file(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        wdir = os.path.dirname(xml_file)
        destination_dir = os.path.join(wdir, "prescript")
        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)
        moved_file = os.path.join(destination_dir, os.path.basename(xml_file))
        shutil.move(xml_file, moved_file)
        backup_file = os.path.basename(xml_file).replace(".xml", ".xml")
        backup_file = os.path.join(wdir, backup_file)
        shutil.copyfile(moved_file, backup_file)
        print(f"Backup file created at: {destination_dir}")

