import re
import os
import glob

def xml_table(self):
    file_path = self.entry.get()  
    table_counts = {}
    table_changes = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_input = file.read()
            table_pattern = r'<table><tgroup cols="0">.*?</table>'
            tables = re.findall(table_pattern, xml_input, re.DOTALL)
            total_tables = len(tables)
            table_counts[xml_file] = total_tables
            print(f"Total tables found in {xml_file}: {total_tables}")

            def modify_table(table):
                colname_pattern = re.findall(r'colname="col(\d+)"', table)
                if not colname_pattern:
                    return None
                max_col = max(map(int, colname_pattern))
                colspecs = "".join(
                    [f'<colspec colname="col{i}" colwidth="{max(600 // max_col, 85)}"/>' for i in range(1, max_col + 1)]
                )
                print(f'colspecs: {colspecs}')
                print(f'max_col: {max_col}')
                new_table = f'<table><tgroup cols="{max_col}">{colspecs}{table[23:]}'
                return new_table if new_table != table else None

            modified = False
            for table in tables:
                modified_table = modify_table(table)
                if modified_table:
                    table_changes[xml_file] = table_changes.get(xml_file, 0) + 1
                    xml_input = xml_input.replace(table, modified_table)
                    xml_input = re.sub(r'"/>><tbody>', r'"/><tbody>', xml_input)
                    xml_input = re.sub(r'"/>><thead>', r'"/><thead>', xml_input)
                    modified = True

            if modified:
                with open(xml_file, 'w', encoding='utf-8') as file:
                    file.write(xml_input)
                print(f"Modified tables in {xml_file}: {table_changes[xml_file]}")
            else:
                print(f"No tables modified in {xml_file}")

    return table_counts, table_changes
