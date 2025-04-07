
import os
import re
import glob

def wrap_core_url(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))  
    pattern = r'([^\w\s])</core:para><core:url type="http" address="([^"]+)">https?://[^\s"<>]+</core:url>'
    pattern1 = r' </core:para><core:url type="http" address="([^"]+)">https?://[^\s"<>]+</core:url>'
    pattern2 = r' </core:para><core:url type="http" address="([^"]+)">([^"]+)</core:url>'
    pattern3 = r'<core:list>(.*?)</core:list></core:para></core:listitem>'
    
    replacement = r'\1 <core:url type="http" address="\2">https://\2</core:url></core:para>'
    replacement1 = r' <core:url type="http" address="\1">https://\1</core:url></core:para>'
    replacement2 = r' <core:url type="http" address="\1">\2</core:url></core:para>'
    replacement3 = r'</core:para><core:list>\1</core:list></core:listitem>'

    for file in xml_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        updated_content = re.sub(pattern, replacement, content)
        updated_content = re.sub(pattern1, replacement1, updated_content)  
        updated_content = re.sub(pattern2, replacement2, updated_content)
        updated_content = re.sub(pattern3, replacement3, updated_content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated_content)