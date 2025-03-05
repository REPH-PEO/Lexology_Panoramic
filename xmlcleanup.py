import os
import re
from pathlib import Path
import glob

def xml_cleanup(self):
    file_path = self.entry.get()
    cleanup_counts = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    replacements = [
        (re.compile(r"<core:para>&#xa0;</core:para>"), ""),
        (re.compile(r'<core:para><core:emph typestyle="bf">&#xa0;</core:emph></core:para>'), ""),
        (re.compile(r'</core:emph></core:name.text></core:person><pnfo:disclaimer><core:para>and</core:para></pnfo:disclaimer></pnfo:contrib><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">'), ", "),
        (re.compile(r'<core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">([a-zA-Z0-9\s\|\+#\/\.,;&\(\)\-]+)</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline><!--authors template-->'), r'<core:byline><pnfo:bio><pnfo:empl-hist>\1</pnfo:empl-hist></pnfo:bio></core:byline>'),
        (re.compile(r'<se:intro><core:title>Contributing Editor<\/core:title><core:list><core:listitem><core:enum>&#x2014;<\/core:enum><core:para>'), "<se:intro><core:generic-hd>Contributing Editor&#x2014;"),
        (re.compile(r'<se:intro><core:title>Contributing Editors<\/core:title><core:list><core:listitem><core:enum>&#x2014;<\/core:enum><core:para>'), "<se:intro><core:generic-hd>Contributing Editors&#x2014;"),
        (re.compile(r'<\/core:para><\/core:listitem><core:listitem><core:enum>&#x2014;</core:enum><core:para>'), ", "),
        (re.compile(r'<\/core:para><\/core:listitem><\/core:list><\/se:intro>'), "</core:generic-hd></se:intro>"),
        (re.compile(r',\s([A-Z][a-z]+\s[A-Z][a-z]+)(<\/core:generic-hd><\/se:intro>)'), r' and \1\2'),
        (re.compile(r',\s([A-Z][a-z]+\s[A-Z][a-z]+)<\/core:emph><\/core:name.text><\/core:person><\/pnfo:contrib><\/pnfo:contribs><\/core:byline>'), r' and \1</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline>'),
        (re.compile(r' , '), ", "),
        (re.compile(r'<core:para></core:para>'), "")
    ]

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
            print(f"No changes in {file}")
    return cleanup_counts

# def xml_cleanup(self):
#     file_path = self.entry.get()
#     cleanup_counts = {}
#     if os.path.isdir(file_path):
#         # Get all XML files in the directory
#         xml_files = glob.glob(os.path.join(file_path, '*.xml'))
#         for xml_file in xml_files:
#             if os.path.isfile(xml_file):
#                 with open(xml_file, 'r+', encoding='utf-8') as f:
#                     xml_content = f.read()
#                     patterns = [
#                         (re.compile(r"<core:para> </core:para>"), ""),
#                         (re.compile(r'<core:para><core:emph typestyle="bf"> </core:emph></core:para>'), ""),
#                         (re.compile(r'</core:emph></core:name.text></core:person><pnfo:disclaimer><core:para>and</core:para></pnfo:disclaimer></pnfo:contrib><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">'), ", "),
#                         (re.compile(r'<core:byline><pnfo:contribs><pnfo:contrib><core:person><core:name.text><core:emph typestyle="bf">([a-z 0-9 \s \| \+ \# \/ \. \, \; \& \\uE001\\uE001 \-]+)</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline><!--authors template-->'), r'<core:byline><pnfo:bio><pnfo:empl-hist>\1</pnfo:empl-hist></pnfo:bio></core:byline>'),
#                         (re.compile(r'<se:intro><core:title>Contributing Editor</core:title><core:list><core:listitem><core:enum>—</core:enum><core:para>'), "<se:intro><core:generic-hd>Contributing Editor—"),
#                         (re.compile(r'<se:intro><core:title>Contributing Editors</core:title><core:list><core:listitem><core:enum>—</core:enum><core:para>'), "<se:intro><core:generic-hd>Contributing Editors—"),
#                         (re.compile(r'</core:para></core:listitem><core:listitem><core:enum>—</core:enum><core:para>'), ", "),
#                         (re.compile(r'</core:para></core:listitem></core:list></se:intro>'), "</core:generic-hd></se:intro>"),
#                         (re.compile(r', ([a-z 0-9 \# \. \; \&]+)</core:generic-hd></se:intro>'), r' and \1</core:generic-hd></se:intro>'),
#                         (re.compile(r', ([a-z 0-9 \s \# \. \; \&]+)</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline>'), r' and \1</core:emph></core:name.text></core:person></pnfo:contrib></pnfo:contribs></core:byline>'),
#                         (re.compile(r' , '), ", "),
#                         (re.compile(r'<core:para></core:para>'), "")
#                     ]
#                     changes_count = 0
#                     for pattern, replacement in patterns:
#                         new_content, num_changes = pattern.subn(replacement, xml_content)
#                         xml_content = new_content
#                         changes_count += num_changes
#                     cleanup_counts[xml_file] = changes_count
#                     if changes_count > 0:
#                         f.seek(0)
#                         f.write(xml_content)
#                         f.truncate()
#                         print(f"Cleaned {changes_count} instance(s) in {xml_file}")
#                     else:
#                         print(f"No changes in {xml_file}")
#     print(cleanup_counts)
#     print("XML cleanup completed.")
#     return cleanup_counts
