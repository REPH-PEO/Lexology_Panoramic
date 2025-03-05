import re
import os
import glob

def modify_contributing_sections(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        # Single contributing editor
        pattern_single = re.compile(
            r'<se:intro><core:title>Contributing Editor</core:title><core:list>(.*?)</core:list></se:intro>',
            re.DOTALL)
        matches_single = pattern_single.findall(xml_content)
        change_count_single = 0
        for match in matches_single:
            names = re.findall(r'<core:para>(.*?)</core:para>', match)
            if names:
                names_str = ', '.join(names)
                new_structure = f'<se:intro><core:generic-hd>Contributing Editor&#x2014;{names_str}</core:generic-hd></se:intro>'
                xml_content = xml_content.replace(f'<core:list>{match}</core:list>', new_structure)
                change_count_single += 1
        # Multiple contributing editors
        pattern_multiple = re.compile(
            r'<se:intro><core:title>Contributing Editors</core:title><core:list>(.*?)</core:list></se:intro>',
            re.DOTALL)
        matches_multiple = pattern_multiple.findall(xml_content)
        change_count_multiple = 0
        for match in matches_multiple:
            names = re.findall(r'<core:para>(.*?)</core:para>', match)
            if names:
                names_str = ', '.join(names[:-1]) + ' and ' + names[-1]
                new_structure = f'<se:intro><core:generic-hd>Contributing Editors&#x2014;{names_str}</core:generic-hd></se:intro>'
                xml_content = xml_content.replace(f'<core:list>{match}</core:list>', new_structure)
                change_count_multiple += 1
        xml_content = xml_content.replace('<se:intro><core:title>Contributing Editor</core:title><se:intro>', '<se:intro>')
        xml_content = xml_content.replace('<se:intro><core:title>Contributing Editors</core:title><se:intro>', '<se:intro>')
        xml_content = xml_content.replace('</se:intro></se:intro>', '</se:intro>')
        with open(xml_file, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        if change_count_single > 0:
            print(f"Modified single contributing editor in {xml_file}: {change_count_single}")
        else:
            print(f"No changes in contributing editor in {xml_file}")
        if change_count_multiple > 0:
            print(f"Modified multiple contributing editors in {xml_file}: {change_count_multiple}")
        else:
            print(f"No changes in contributing editors in {xml_file}")
