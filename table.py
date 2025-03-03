import re
import os
import glob

def xml_table(self):
    file_path = self.entry.get()
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_input = file.read()

            table_pattern = re.compile(r'(<table><tgroup cols="0"><thead>.*?</table>)', re.DOTALL)
            tables = table_pattern.findall(xml_input)
            Total_tables = len(tables)
            print(f"Total tables found: {Total_tables}")

            # Function to replace tables based on highest colname
            def modify_table(table):
                colname_pattern = re.findall(r'colname="col(\d+)"', table)
                if not colname_pattern:
                    return None  # No colname found, no modification needed

                max_col = max(map(int, colname_pattern))  # Get the highest column number

                # Generate replacement table based on max_col
                colspecs = "".join(
                    [f'<colspec colname="col{i}" colwidth="{max(600 - (i-1)*50, 85)}"/>' for i in range(1, max_col+1)]
                )
                new_table = f'<table><tgroup cols="{max_col}">{colspecs}{table[23:]}'  # Keep content

                return new_table if new_table != table else None  # Return only if changed

            # Process each table and print modifications
            for table in tables:
                modified_table = modify_table(table)
                if modified_table:
                    print("Modified Table:\n", modified_table, "\n")