import re
import os
import glob

def modify_byline(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        
        # Pattern to match the first structure
        pattern1 = re.compile(
            r'<core:no-title/><core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">(.*?)</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline><!--authors template-->',
            re.DOTALL
        )
        
        # Pattern to match the second structure
        pattern2 = re.compile(
            r'<core:byline><pnfo:contribs>(.*?)</pnfo:contribs></core:byline>',
            re.DOTALL
        )
        
        # Replace the first structure
        matches1 = pattern1.findall(xml_content)
        for match in matches1:
            new_structure1 = f'<core:no-title/><core:byline><pnfo:bio><pnfo:empl-hist>{match}</pnfo:empl-hist></pnfo:bio></core:byline>'
            xml_content = xml_content.replace(
                f'<core:no-title/><core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">{match}</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline><!--authors template-->',
                new_structure1
            )
        
        # Replace the second structure
        matches2 = pattern2.findall(xml_content)
        for match2 in matches2:
            names = re.findall(r'<core:emph typestyle="bf">(.*?)</core:emph>', match2)
            if names:
                names_str = ', '.join(names[:-1]) + ' and ' + names[-1]
                new_structure2 = f'<core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">{names_str}</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline>'
                xml_content = xml_content.replace(
                    f'<core:byline><pnfo:contribs>{match2}</pnfo:contribs></core:byline>',
                    new_structure2
                )
        
        with open(xml_file, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        print(f"Modified byline in {xml_file}")
