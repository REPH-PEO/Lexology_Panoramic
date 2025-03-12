import re
import os
import glob

def modify_contributing_sections(self):
    file_path = self.entry.get()
    contrib_counts = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        patterns = [
            (r'<se:intro><core:title>Contributing Editor</core:title><core:list>(.*?)</core:list></se:intro>',
             'Contributing Editor'),
            (r'<se:intro><core:title>Contributing Editors</core:title><core:list>(.*?)</core:list></se:intro>',
             'Contributing Editors')]
        contrib_count = 0
        for pattern, title in patterns:
            matches = re.findall(pattern, xml_content, re.DOTALL)
            for match in matches:
                names = re.findall(r'<core:para>(.*?)</core:para>', match)
                if names:
                    if title == 'Contributing Editor':
                        names_str = ', '.join(names)
                    else: 
                        if len(names) == 1:
                            names_str = names[0]
                        elif len(names) == 2:
                            names_str = ' and '.join(names)
                        else:
                            names_str = ', '.join(names[:-1]) + ', and ' + names[-1]
                    new_structure = f'<se:intro><core:generic-hd>{title}&#x2014;{names_str}</core:generic-hd></se:intro>'
                    xml_content = xml_content.replace(f'<core:list>{match}</core:list>', new_structure)
                    contrib_count += 1
        xml_content = xml_content.replace('<se:intro><core:title>Contributing Editor</core:title><se:intro>', '<se:intro>')
        xml_content = xml_content.replace('<se:intro><core:title>Contributing Editors</core:title><se:intro>', '<se:intro>')
        xml_content = xml_content.replace('</se:intro></se:intro>', '</se:intro>')
        with open(xml_file, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        contrib_counts[xml_file] = contrib_count
        print(f"Contributing editor(s) in {xml_file}: {contrib_counts.get(xml_file, 0)}")
    return contrib_counts