import os
import re
import glob

def fix_core_list(self):
    file_path = self.entry.get().strip()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    pattern = r'</core:para></core:listitem>(<!--.*?--><core:list>.*?</core:list>)<core:listitem>'
    pattern1 = r'</core:emph>(<!--.*?--><core:list>.*?</core:list>)</core:para></core:listitem><core:listitem>'
    
    replacement = r'</core:para>\1</core:listitem><core:listitem>'
    replacement1 = r'</core:emph></core:para>\1</core:listitem><core:listitem>'

    for file in xml_files:
        with open(file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        updated_content = re.sub(pattern, replacement, original_content)
        updated_content = re.sub(pattern1, replacement1, updated_content)
        if updated_content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print("List has been modified in the file:", file)
        else:
            print(f"No changes made to file: {file}")