import re
import os
import glob

def desig_text(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
    # Read the content of the file
        with open(xml_file, 'r', encoding='utf-8') as file:
            text_data = file.read()
        pattern_desig = r'<core:desig value="([^"]+)">(.*?)</core:desig>'
        matches = re.findall(pattern_desig, text_data)
        # Initialize counters
        total_count = 0
        matching_count = 0
        not_matching_count = 0
        # Compare values and text content within <core:desig> tags
        for match in matches:
            total_count += 1
            value = match[0]
            text_content = match[1].strip()
            if value == text_content:
                matching_count += 1
            elif (value.isdigit() and text_content.isdigit() and int(value) == int(text_content)) or (value == 'Question 1' and text_content == '1'):
                matching_count += 1
            else:
                not_matching_count += 1
        print(f'Total occurrences: {total_count}')
        print(f'Occurrences where text matches the specified value criteria: {matching_count}')
        print(f'Occurrences where text does not match the specified value criteria: {not_matching_count}')
