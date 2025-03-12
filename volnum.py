import re
import os
import glob

def xml_volnum(self):
    file_path = self.entry.get()
    count_hds = {}
    unique_matches = {}
    volnum_yr = {}
    title_yr = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            text_data = file.read()
        pattern = r'volnum="(\d{4})".*?'
        matches = re.findall(pattern, text_data, re.DOTALL)
        unique_match = set(matches)
        unique_matches[xml_file] = ', '.join(unique_match)
        volnum_yr[xml_file] = unique_match.pop() if unique_match else None
        print(f"volnum unique year in {xml_file}: {unique_matches[xml_file]}")
        print(f"volnum common year in {xml_file}: {volnum_yr[xml_file]}")
        pattern1 = r'<core:title>(.*?)</core:title>'
        titles = re.findall(pattern1, text_data, re.DOTALL)
        if titles:
            first_title_content = titles[0]
            pattern_digits = r'\d{4}'
            matches1 = re.findall(pattern_digits, first_title_content)
            title_yr[xml_file] = matches1[0] if matches1 else None
            print(f"Year in core:title for {xml_file} is: {title_yr[xml_file]}")
        pattern2 = r'<se:intro>.*?</se:intro>'
        generic_hds = re.findall(pattern2, text_data, re.DOTALL)
        listtag_pattern = r'<core:list>'
        count_hd = 0
        for generic_hd in generic_hds:
            if re.search(listtag_pattern, generic_hd, re.UNICODE):
                count_hd += 1
        count_hds[xml_file] = count_hd
        if count_hd > 0:
            print(f'Contributing Editor(s) tag in core:list in {xml_file}: {count_hd}')
        else:
            print(f'No Contributing Editor(s) tag in core:list in {xml_file}')
    return count_hds, unique_matches, volnum_yr, title_yr
