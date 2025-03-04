import re
import os
import glob

def xml_byline(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    accented_character_pattern = r'[à-öø-ÿÀ-ÖØ-ß€£¥₩₹$]'
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        pattern = r'<core:byline>(.*?)</core:byline>'
        matches = re.findall(pattern, xml_content, re.DOTALL)
        total_accented_characters = 0
        for match in matches:
            accented_characters = re.findall(accented_character_pattern, match, re.UNICODE)
            total_accented_characters += len(accented_characters)
        if total_accented_characters > 0:
            print(f'Total number of accented characters in {xml_file}: {total_accented_characters}')
        else:
            print(f'No accented characters in {xml_file}')