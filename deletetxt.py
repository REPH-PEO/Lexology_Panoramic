import os
import glob

def delete_txtfiles(self):
        file_path = self.entry.get()
        txt_files = glob.glob(os.path.join(file_path, "*.txt"))
        for file_path in txt_files:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        print("Deleting txt files complete")  