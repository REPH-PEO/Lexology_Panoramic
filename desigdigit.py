import re
import os
import glob

def desig_digit(self):
        file_path = self.entry.get()
        xml_files = glob.glob(os.path.join(file_path, '*.xml'))
        report_data = []
        for xml_file in xml_files:
            with open(xml_file, "r", encoding='utf-8') as file:
                content = file.read()
            # Regular expression pattern to extract numeric values from <core:desig> tags
            pattern = r'<core:desig value="(\d+)">Question (\d+)</core:desig>'
            matches = re.findall(pattern, content)
            print(f"Number of desig found: {len(matches)}")
            # Initialize list for non-matching pairs
            non_matching_pairs = []
            # Compare the extracted numeric values
            for value_attr, value_text in matches:
                if value_attr != value_text:
                    non_matching_pairs.append((value_attr, value_text))
            # Print only non-matching pairs
            print("Non-matching pairs:")
            for pair in non_matching_pairs:
                print(f"Tag Value: {pair[0]}, Question Number: {pair[1]}")
            # Print count of non-matching pairs
            print(f"Desig value do not match: {len(non_matching_pairs)}")