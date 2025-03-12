import os
import glob

def delete_xlsx(self):
        file_path = self.entry.get()
        xlsx_files = glob.glob(os.path.join(file_path, "*.xlsx"))
        for file_path in xlsx_files:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        print("Deleting .xlsx files") 