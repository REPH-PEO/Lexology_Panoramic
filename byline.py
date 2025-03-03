import re
import os
import glob

def xml_byline(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        # Regular expression pattern to extract content within <core:byline> tags
        pattern = r'<core:byline>(.*?)</core:byline>'
        matches = re.findall(pattern, xml_content, re.DOTALL)

        # Initialize counters for matching and non-matching occurrences
        match_count = 0
        no_match_count = 0

        # Define the character range for accented characters and symbols to search for
        accented_character_pattern = r'[à-öø-ÿÀ-ÖØ-ß€£¥₩₹$]'

        # Search for accented characters and symbols within the extracted content
        for match in matches:
            if re.search(accented_character_pattern, match, re.UNICODE):
                match_count += 1
            else:
                no_match_count += 1

        print(f'Accented characters inside core by line: {match_count}')
        print(f'No Accented characters inside core by line: {no_match_count}')
