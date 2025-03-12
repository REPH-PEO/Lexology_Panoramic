import re
import os
import glob
import io  

def desig_analysis(self):
    file_path = self.entry.get()
    pattern1 = re.compile(r'<core:desig value="([^"]+)">(.*?)</core:desig>')
    pattern2 = re.compile(r'<core:desig value="(\d+)">Question (\d+)</core:desig>')
    non_matching_pairs1 = {}
    non_matching_pairs2 = {}
    xml_files = glob.glob(os.path.join(file_path, '*.xml'))
    output = io.StringIO()

    for xml_file in xml_files:
        with open(xml_file, 'r', encoding='utf-8') as file:
            content = file.read()
        matches1 = pattern1.findall(content)
        total_count1 = len(matches1)
        print(f"Total desig Country: {total_count1}")
        match_count1 = 0
        
        for value, text in matches1:
            if value == text:
                match_count1 += 1
            else:
                if xml_file not in non_matching_pairs1:
                    non_matching_pairs1[xml_file] = []
                non_matching_pairs1[xml_file].append((value, text))

        matches2 = pattern2.findall(content)
        total_count2 = len(matches2)
        print(f"Total desig Question: {total_count2}")

        match_count2 = 0
        for value, question in matches2:
            if value == question:
                match_count2 += 1
            else:
                if xml_file not in non_matching_pairs2:
                    non_matching_pairs2[xml_file] = []
                non_matching_pairs2[xml_file].append((value, question))
        
        print(f"Total matches for desig Country: {match_count1}")
        if xml_file in non_matching_pairs1:
            print("Non-matching desig Country below:")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=output)
            print("Non-matching desig Country below:", file=output)
            for value, text in non_matching_pairs1[xml_file]:
                print(f"Desig Country value: {value}, Desig Country text: {text}")
                print(f"Desig Country value: {value}, Desig Country text: {text}", file=output)
        else:
            print("All pairs match for desig Country.")
   
        print(f"Total matches for desig Question: {match_count2}")
        if xml_file in non_matching_pairs2:
            print("Non-matching pairs for desig Question:")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=output)
            print("Non-matching pairs for desig Question:", file=output)
            for value, question in non_matching_pairs2[xml_file]:
                print(f"Desig Question value: {value}, Question no.: {question}", file=output)
                print(f"Desig Question value: {value}, Question no.: {question}")
        else:
            print("All pairs match for desig Question.")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=output)  
    # print("Non-matching desig Country below:", file=output)      
    # print(f"Desig Country value: {value}, Desig Country text: {text}", file=output)   
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=output) 
    # print("Non-matching pairs for desig Question:", file=output)    
    # print(f"Desig Question value: {value}, Question no.: {question}", file=output)
    return output.getvalue()
