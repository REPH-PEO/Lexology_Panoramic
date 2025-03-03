import os
import re
import pandas as pd
import openpyxl
from openpyxl.styles import Font, Alignment

def parse_textfile(self,filepath):
        """Parses the content of a text file and extracts data based on the format."""
        #filepath = os.path.expanduser(self.entry.get().strip())
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        patterns = {
        "Number of atict-add": r"Number of atict-add:\s+(\d+)",
        "Number of atict-del": r"Number of atict-del:\s+(\d+)",
        "Number of Double Dash": r"Double Dash Count \(count only\):\s+(\d+)",
        "Number of Comment": r"Comment Count \(count only\):\s+(\d+)",
        "Number of Empty Tags": r"Empty Tags removed\(core:para/core:emph\):\s+(\d+)",
        "Number of Empty fn:para flag": r"Empty fn:para Tags flag:\s+(\d+)",
        "Number of double space": r"Number of double space removed:\s+(\d+)",
        "Number of space before/after atict": r"Number of space before/after atict removed:\s+(\d+)",
        "Number of three dots": r"Number of three dots replaced:\s+(\d+)",
        "Number of three dots after a period": r"Number of three dots after a period replaced:\s+(\d+)",
        "Number of three dots and a period": r"Number of three dots and a period replaced:\s+(\d+)",
        "Number of four dots": r"Number of four dots replaced:\s+(\d+)",
        "Number of three dots preceding or following quotation mark or square bracket": r"Number of three dots preceding or following\s+quotation mark or square bracket replaced:\s+(\d+)",
        "Number of space after a period in end tag": r"Number of space after a period in end tag removed:\s+(\d+)",
        "Number of section symbol followed by a regular space": r"Number of section symbol followed by a\s+regular space replaced:\s+(\d+)",
        "Number of space after start tag": r"Number of space after start tag removed:\s+(\d+)",
        "Number of space before end tag": r"Number of space before end tag removed:\s+(\d+)",
        "Number of space in start tag outside atict": r"Number of space in start tag outside atict:\s+(\d+)",
        "Number of space in end tag outside atict": r"Number of space in end tag outside atict:\s+(\d+)",
        "Number of space in LNCI tag": r"Number of space in LNCI tag removed:\s+(\d+)"
    }

        data = {}
        for category, pattern in patterns.items():
            match = re.search(pattern, content)
            data[category] = int(match.group(1)) if match else 0
        return data

def extract_pub_and_unit(self, folder_path, filename):
        """Extracts the first 5 digits of the folder name as Pub and the filename as Unit."""
        # Extract folder name from the folder path
        folder_name = os.path.basename(folder_path)
        # Match first 8 digits in the folder name
        match = re.match(r"([a-zA-Z0-9]{1,8})", folder_name)
        pub = match.group(1) if match else "XWeb Pub"  # Capture first 5 digits
        unit = filename.replace("_report.txt","")  # Use file name inside the folder as Unit
        return pub, unit

def convert_text_to_excel(self):
            file_path = os.path.expanduser(self.entry.get().strip())
    #def consolidate_reports(self, folder_path):
            report_data = []
            error_data = []  # To store errors extracted from the pattern
            for root, _, files in os.walk(file_path):
                for file in files:
                    if file.endswith('.txt'):
                        filepath = os.path.join(root, file)
                        pub, unit = self.extract_pub_and_unit(root, file)
                        parsed_data = self.parse_textfile(filepath)
                        parsed_data.update({"Pub": pub, "Unit": unit})
                        report_data.append(parsed_data)
                        # Extract error pattern matches
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        matches = re.findall(r'<atict:add time="00" user=(.*?)</atict:add>', content)
                        for match in matches:
                            error_data.append({"Unit": unit, "Error Reference": match.strip()})
            # Create DataFrames for reports and errors
            df = pd.DataFrame(report_data)
            error_df = pd.DataFrame(error_data)
            # Reorder columns to ensure 'Pub' and 'Unit' are the first two columns
            columns_order = ['Pub', 'Unit'] + [col for col in df.columns if col not in ['Pub', 'Unit']]
            df = df[columns_order]
            output_excel = os.path.join(file_path, 'XWeb_XML_Cleanup_Report.xlsx')
            # Save DataFrame to Excel with an additional "Error" sheet
            with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
                # Write the main report
                df.to_excel(writer, index=False, sheet_name="Report")
                error_df.to_excel(writer, index=False, sheet_name="Reference")
                report_sheet = writer.sheets["Report"]
                self.format_sheet(report_sheet)
                if not error_df.empty:
                    error_sheet = writer.sheets["Reference"]
                    self.format_sheet1(error_sheet)
            print("Consolidated report in Excel saved to", output_excel)

def format_sheet(self, sheet):
        """Applies formatting to a given worksheet."""
        header_font = Font(bold=True, color="FFFFFF")  # Bold, white text
        for cell in sheet[1]:  # First row (headers)
            cell.font = header_font
            cell.fill = openpyxl.styles.PatternFill(start_color="A9A9A9", end_color="000000", fill_type="solid")
            cell.alignment = Alignment(horizontal="center",wrap_text=True)
        # Set specific column widths
        sheet.column_dimensions["A"].width = 10  # First column
        sheet.column_dimensions["B"].width = 20
        sheet.column_dimensions["C"].width = 12
        sheet.column_dimensions["D"].width = 12
        sheet.column_dimensions["E"].width = 10
        sheet.column_dimensions["F"].width = 10
        sheet.column_dimensions["G"].width = 10
        sheet.column_dimensions["H"].width = 10
        sheet.column_dimensions["I"].width = 10
        sheet.column_dimensions["J"].width = 12
        sheet.column_dimensions["K"].width = 10
        sheet.column_dimensions["L"].width = 12
        sheet.column_dimensions["M"].width = 12
        sheet.column_dimensions["N"].width = 10
        sheet.column_dimensions["O"].width = 15
        sheet.column_dimensions["P"].width = 12
        sheet.column_dimensions["Q"].width = 12
        sheet.column_dimensions["R"].width = 10
        sheet.column_dimensions["S"].width = 12
        sheet.column_dimensions["T"].width = 10
        sheet.column_dimensions["U"].width = 12
        sheet.column_dimensions["V"].width = 10
        # Set column width and wrap text
        for col in sheet.columns:
            for cell in col:
                cell.alignment = Alignment(horizontal="center",wrap_text=True)
                
def format_sheet1(self, sheet1):
        """Applies formatting to a given worksheet."""
        header_font = Font(bold=True, color="FFFFFF")  # Bold, white text
        for cell in sheet1[1]:  # First row (headers)
            cell.font = header_font
            cell.fill = openpyxl.styles.PatternFill(start_color="A9A9A9", end_color="000000", fill_type="solid")
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        # Set specific column widths
        sheet1.column_dimensions["A"].width = 20  # First column
        sheet1.column_dimensions["B"].width = 80  # Second column
        # Ensure all cells have wrap text alignment
        for col in sheet1.columns:
            for cell in col:
                cell.alignment = Alignment(wrap_text=True)