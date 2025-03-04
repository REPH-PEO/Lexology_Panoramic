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
        print(f"volnum unique year in {xml_file}: {unique_matches}")
        print(f"volnum common year in {xml_file}: {volnum_yr}")

        if titles:
            first_title_content = titles[0]
            pattern_digits = r'\d{4}'
            matches1 = re.findall(pattern_digits, first_title_content)
            title_yr = matches1[0] if matches1 else None
            print(f"core:title year in {xml_file} is: {title_yr}")

        listtag_pattern = r'<core:list>'
        count_hd = 0
        nocount_hd = 0
        for generic_hd in generic_hds:
            if re.search(listtag_pattern, generic_hd, re.UNICODE):
                count_hd += 1
                print(f'Contributing Editors in list in {xml_file}: {count_hd}')
            else:
                nocount_hd += 1
                print(f'No Contributing Editors in list in {xml_file}: {nocount_hd}')
