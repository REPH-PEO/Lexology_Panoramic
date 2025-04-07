import os 
import re 
import glob

# def fix_core_list(self): 
#     file_path = self.entry.get() 
#     xml_files = glob.glob(os.path.join(file_path, '.xml')) 
#     pattern = re.compile(r'(core:list>.*?</core:list>)(</core:para></core:listitem>)')

#     def replacement(match): 
#         return f'</core:para>{match.group(1)}</core:listitem>' 
#     for file in xml_files:
#         with open(file, 'r', encoding='utf-8') as f: 
#             content = f.read() 
#         fixed_xml = pattern.sub(replacement, content) 
#         with open(file, 'w', encoding='utf-8') as f: 
#                 f.write(fixed_xml)

def fix_core_list(self):
        file_path = self.entry.get()
        if os.path.isdir(file_path):
            xml_files = glob.glob(os.path.join(file_path, '*.xml'))
            for xml_file in xml_files:
                if os.path.isfile(xml_file):
                    with open(xml_file, 'r+', encoding='utf-8') as f:
                        xml_tag = f.read()                        
                        pattern = r'(<core:listitem>.*?</core:listitem>)'
                        empty_fnpara_patterns = {r"<core:list>(.*?)</core:list></core:para></core:listitem>": r'</core:para><core:list>\1</core:list></core:listitem>'}
                        def replace_list(match):
                            section = match.group(0)
                            for empty_fnpara_pattern, replacement in empty_fnpara_patterns.items():
                                section = re.sub(empty_fnpara_pattern, replacement, section)
                            return section
                        xml_tag = re.sub(pattern, replace_list, xml_tag)
                        f.write(xml_tag)
                        f.truncate()