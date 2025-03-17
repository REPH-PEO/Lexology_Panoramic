import os
from pathlib import Path
import xmlcleanup
import contributingEd  
import authtemplate
import volnum
import byline
import table
import desigcountry
import questiondesig

def create_report(self):
    cleanup_counts = xmlcleanup.xml_cleanup(self)
    contrib_counts = contributingEd.modify_contributing_sections(self)  
    authtemp_counts = authtemplate.modify_byline(self)  
    count_hds, unique_matches, volnum_yr, title_yr = volnum.xml_volnum(self) 
    byline_counts = byline.xml_byline(self)
    table_counts, table_changes = table.xml_table(self)
    country_results = desigcountry.desig_analysis(self)
    question_results = questiondesig.desig_analysis1(self)

    for xml_file in cleanup_counts.keys():
        report_file_path = os.path.splitext(xml_file)[0] + "_report.txt"
        with open(report_file_path, "w", encoding='utf-8') as report_file:
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"XML Cleanup Report for {os.path.basename(xml_file)}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Xml clean up: {cleanup_counts.get(xml_file, 0)}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Contributing Editor(s): {contrib_counts.get(xml_file, 0)}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"By-line change: {authtemp_counts.get(xml_file, 0)}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Contributing Editor(s) still in core:list: {count_hds.get(xml_file, 0)}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Unique year in volnum: {unique_matches.get(xml_file, 'N/A')}\n") 
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Volnum Year: {volnum_yr.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Title Year: {title_yr.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Non matching Country: {country_results.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            report_file.write(f"Non matching Question: {question_results.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")            
            report_file.write(f"Number of accented character(s): {byline_counts.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")    
            report_file.write(f"Total tables found: {table_counts.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")   
            report_file.write(f"Modified tables: {table_changes.get(xml_file, 'N/A')}\n")
            report_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")                               
        print(f"Report file created: {report_file_path}")