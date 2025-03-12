import re
import os
import glob

def modify_byline(self):
    file_path = self.entry.get()
    authtemp_counts = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    count_change = 0  
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        pattern1 = re.compile(r'<core:no-title/><core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">(.*?)</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline><!--authors template-->',
            re.DOTALL)
        pattern2 = re.compile(
            r'<core:byline><pnfo:contribs>(.*?)</pnfo:contribs></core:byline>',
            re.DOTALL)
        
        matches1 = pattern1.findall(xml_content)
        print(f"pattern1 in {xml_file}:{matches1}")
        count_pattern1 = 0
        for match in matches1:
            new_structure1 = f'<core:no-title/><core:byline><pnfo:bio><pnfo:empl-hist>{match}</pnfo:empl-hist></pnfo:bio></core:byline>'
            xml_content = xml_content.replace(f'<core:no-title/><core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">{match}</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline><!--authors template-->',
                new_structure1)
            count_pattern1 += 1  

        matches2 = pattern2.findall(xml_content)
        count_pattern2 = 0
        for match2 in matches2:
            names = re.findall(r'<core:emph typestyle="bf">(.*?)</core:emph>', match2)
            print(f"pattern2 in {xml_file}: {names}")
            if names:
                if len(names) == 1:
                    names_str = names[0]
                elif len(names) == 2:
                    names_str = ' and '.join(names)
                else:
                    names_str = ', '.join(names[:-1]) + ', and ' + names[-1]
                new_structure2 = (
                    f'<core:byline><pnfo:contribs><pnfo:contrib><core:person>'
                    f'<core:name.text><core:emph typestyle="bf">{names_str}</core:emph>'
                    f'</core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline>')
                xml_content = xml_content.replace(f'<core:byline><pnfo:contribs>{match2}</pnfo:contribs></core:byline>',
                    new_structure2)
                count_pattern2 += 1
        count_change = count_pattern1 + count_pattern2
        authtemp_counts[xml_file] = count_change
        with open(xml_file, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        print(f"Modified byline in {xml_file}: {count_change}")
    return authtemp_counts 
