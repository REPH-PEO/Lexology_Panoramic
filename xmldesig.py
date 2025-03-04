import re
import os
import glob

def desig_analysis(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            text_data = file.read()
        pattern_text = r'<core:desig value="([^"]+)">(.*?)</core:desig>'
        pattern_digit = r'<core:desig value="(\d+)">Question (\d+)</core:desig>'
        matches_text = re.findall(pattern_text, text_data)
        matches_digit = re.findall(pattern_digit, text_data)
        total_count = 0
        matching_count = 0
        not_matching_count = 0
        for match in matches_text:
            total_count += 1
            value = match[0]
            text_content = match[1].strip()
            if value == text_content:
                matching_count += 1
            elif (value.isdigit() and text_content.isdigit() and int(value) == int(text_content)) or (value == 'Question 1' and text_content == '1'):
                matching_count += 1
            else:
                not_matching_count += 1

        print(f'Matches values/pcdata in text desig in {xml_file}: {matching_count}')
        print(f'Do not match values/pcdata in text desig in {xml_file}: {not_matching_count}')
        print(f'Total values/pcdata in text desig in {xml_file}: {total_count}')
        print(f'Total values/pcdata in digit desig in {xml_file}: {len(matches_digit)}')
        non_matching_pairs = []
        for value_attr, value_text in matches_digit:
            if value_attr != value_text:
                non_matching_pairs.append((value_attr, value_text))
        for pair in non_matching_pairs:
            print(f"Desig value in number desig {xml_file}: {pair[0]}, Question Number: {pair[1]}")
        print(f"Desig value do not match in number desig {xml_file}: {len(non_matching_pairs)}")
