import re
import os
import glob

def xml_volnum(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            text_data = file.read()
        pattern = r'volnum="(\d{4})".*?'
        pattern1 = r'<core:title>(.*?)</core:title>'
        pattern2 = r'<se:intro>.*?</se:intro>'
        titles = re.findall(pattern1, text_data, re.DOTALL)
        generic_hds = re.findall(pattern2, text_data, re.DOTALL)
        matches = re.findall(pattern, text_data, re.DOTALL)
        unique_matches = set(matches)
        volnum_yr = unique_matches.pop() if unique_matches else None
        print(f"volnum unique year: {unique_matches}")
        print(f"volnum common year: {volnum_yr}")

        if titles:
            first_title_content = titles[0]
            pattern_digits = r'\d{4}'
            matches1 = re.findall(pattern_digits, first_title_content)
            title_yr = matches1[0] if matches1 else None
            print(f"core:title year is: {title_yr}")
        if generic_hds:
            first_generic_hd = generic_hds[0]
            pattern_hd = r'<core:listitem>'
            matches2 = re.findall(pattern_hd, first_generic_hd)
            count_hd = len(matches2)
            print(f"list in generic hd: {count_hd}")
