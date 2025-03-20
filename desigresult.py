import os
import re
import glob

def check_desig_status(self):
    file_path = self.entry.get()
    all_results = {}
    mismatch_counts = {} 
    if os.path.isdir(file_path):
        xml_files = glob.glob(os.path.join(file_path, '*.xml'))
        desig_pattern = r'<core:desig value="([^"]+)">(.*?)</core:desig>'
        question_pattern = r'<core:desig value="(\d+)">Question (\d+)</core:desig>'
        for xml_file in xml_files:
            file_results = []
            mismatch_count = 0
            with open(xml_file, 'r', encoding='utf-8') as file:
                content = file.read()
            desig_matches = re.findall(desig_pattern, content)
            for value, text in desig_matches:
                if value == text:
                    status = "match"
                else:
                    question_match = re.match(question_pattern, f'<core:desig value="{value}">{text}</core:desig>')
                    if question_match:
                        value_num, question_num = question_match.groups()
                        if value_num == question_num:
                            status = "match"
                        else:
                            status = "mismatch"
                            mismatch_count += 1 
                    else:
                        status = "mismatch"
                        mismatch_count += 1 
                
                file_results.append({
                    "value": value,
                    "text": text,
                    "status": status
                })
            all_results[xml_file] = file_results
            mismatch_counts[xml_file] = mismatch_count
    print(f"Desig status results: {all_results}")    
    print(f"Total mismatch counts: {mismatch_counts}")        

    return all_results, mismatch_counts
