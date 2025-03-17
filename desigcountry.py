import os
import re
import glob

def desig_analysis(self):
    file_path = self.entry.get()
    country_results = {}
    if os.path.isdir(file_path):
        xml_files = glob.glob(os.path.join(file_path, '*.xml'))  
        pattern1 = re.compile(r'<core:desig value="([^"]+)">(.*?)</core:desig>')
        question_pattern = re.compile(r'Question\s+\d+$')  
        for xml_file in xml_files:
            with open(xml_file, 'r', encoding='utf-8') as file:
                content = file.read()
            matches1 = pattern1.findall(content)
            non_matching_pairs = []
            for value, text in matches1:
                if value != text and not question_pattern.match(text):
                    non_matching_pairs.append((value, text))
            if not non_matching_pairs:
                country_results[xml_file] = "NA"
            else:
                country_results[xml_file] = non_matching_pairs
            print(f"Non-matching pairs for desig in {xml_file}: {non_matching_pairs}")
    return country_results
