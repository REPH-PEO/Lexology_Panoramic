import re
import os
import glob

def xml_generichd(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        pattern = r'<se:intro>(.*?)</se:intro>'
        matches = re.findall(pattern, xml_content, re.DOTALL)
        match_count = 0
        no_match_count = 0
        listtag_pattern = r'<core:list>'
        for match in matches:
            if re.search(listtag_pattern, match, re.UNICODE):
                match_count += 1
                print(f'Contributing Editors in list: {match_count}')
            else:
                no_match_count += 1
                print(f'No Contributing Editors in list: {no_match_count}')
