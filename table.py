import re
import os
import glob

def xml_table(self):
    file_path = self.entry.get()  # Get directory from GUI entry
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))  # Find all XML files in the directory
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_input = file.read()
        
        table_pattern = re.compile(r'(<table><tgroup cols="\d+">.*?</table>)', re.DOTALL)
        tables = table_pattern.findall(xml_input)
        total_tables = len(tables)
        print(f"Total tables found in {xml_file}: {total_tables}")
        def modify_table(table):
            colname_pattern = re.findall(r'colname="col(\d+)"', table)
            if not colname_pattern:
                return None  # Skip if no colname found
            max_col = max(map(int, colname_pattern))  # Find the highest column number
            colspecs = "".join(
                [f'<colspec colname="col{i}" colwidth="{max(600 // max_col, 85)}"/>' for i in range(1, max_col + 1)]
            )
            new_table = f'<table><tgroup cols="{max_col}">{colspecs}{table[23:]}'  # Replace table opening
            return new_table if new_table != table else None 
        modified = False
        for table in tables:
            modified_table = modify_table(table)
            if modified_table:
                xml_input = xml_input.replace(table, modified_table)  # Replace old table with modified one
                xml_input = re.sub(r'"/>><tbody>', r'"/><tbody>', xml_input)
                modified = True
        if modified:
            with open(xml_file, 'w', encoding='utf-8') as file:
                file.write(xml_input)
            
            print(f"Modified tables saved in {xml_file}")