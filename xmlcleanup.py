import os
import re
import glob
from openpyxl import Workbook

def xml_cleanup(self):
    file_path = self.entry.get()
    cleanup_counts = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    replacements = [
        (re.compile(r"<core:para>&#xa0;</core:para>"), ""),
        (re.compile(r'<core:para><core:emph typestyle="bf">&#xa0;</core:emph></core:para>'), ""),
        (re.compile(r' , '), ", "),
        (re.compile(r'<core:para></core:para>'), "")]
    for file in xml_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        changes_count = 0
        for pattern, replacement in replacements:
            new_content, num_changes = pattern.subn(replacement, content)
            content = new_content
            changes_count += num_changes
        cleanup_counts[file] = changes_count
        if changes_count > 0:
            print(f"XML clean up changes in {file}: {changes_count}")
        else:
            print(f"No clean up changes in {file}")
    return cleanup_counts

