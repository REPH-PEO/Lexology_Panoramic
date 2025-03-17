import os
import re
import glob

def desig_analysis1(self):
    file_path = self.entry.get()
    question_result = {}
    if os.path.isdir(file_path):
        xml_files = glob.glob(os.path.join(file_path, '*.xml'))
        pattern2 = re.compile(r'<core:desig value="(\d+)">Question (\d+)</core:desig>')
        for xml_file in xml_files:
            with open(xml_file, 'r', encoding='utf-8') as file:
                content = file.read()
            matches2 = pattern2.findall(content)
            non_matching_pairs2 = []
            for value, question in matches2:
                if value != question:
                    non_matching_pairs2.append((value, question))
            if not non_matching_pairs2:
                question_result[xml_file] = "NA"
            else:
                question_result[xml_file] = non_matching_pairs2
            print(f"Non-matching pairs for desig in {xml_file}: {non_matching_pairs2}")
    return question_result