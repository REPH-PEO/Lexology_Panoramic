import re
import os
import glob

def xml_byline(self):
    file_path = self.entry.get()
    byline_counts = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    accented_character_pattern = r'[à-öø-ÿÀ-ÖØ-ß€£¥₩₹$áéíóúàèìòùâêîôûãñõäëïöüç]|(&aacute;|&#225;|&eacute;|&#233;|&iacute;|&#237;|&oacute;|&#243;|&uacute;|&#250;|&agrave;|&#224;|&egrave;|&#232;|&igrave;|&#236;|&ograve;|&#242;|&ugrave;|&#249;|&acirc;|&#226;|&ecirc;|&#234;|&icirc;|&#238;|&ocirc;|&#244;|&ucirc;|&#251;|&atilde;|&#227;|&ntilde;|&#241;|&otilde;|&#245;|&auml;|&#228;|&euml;|&#235;|&iuml;|&#239;|&ouml;|&#246;|&uuml;|&#252;|&ccedil;|&#231;)'
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()
        pattern = r'<core:byline>(.*?)</core:byline>'
        matches = re.findall(pattern, xml_content, re.DOTALL)
        total_accented_characters = 0
        for match in matches:
            accented_characters = re.findall(accented_character_pattern, match, re.UNICODE)
            total_accented_characters += len(accented_characters)
        byline_counts[xml_file] = total_accented_characters
        if total_accented_characters > 0:
            print(f'Number of accented characters in {xml_file}: {total_accented_characters}')
        else:
            print(f'No accented characters in {xml_file}')
    return byline_counts
