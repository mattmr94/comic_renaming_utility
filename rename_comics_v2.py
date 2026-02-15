import json
import os
import re

# This script is optimized for the .json output from the Grand Comics Database series overview at https://www.comics.org/series/SERIES_ID/overview/
with open('table.json', 'r') as f:
    issue_map = json.load(f)

counter = 0

folder_path_input = input("Please enter the entire file path for the comics you would like to update: ")

while True:
    volume_input = input("Enter volume number if applicable. If not applicable, press Enter: ")
    if volume_input == '':
        volume = ""
        break
    elif not volume_input.isdigit():
        print("Please enter a valid number")
    else:
        volume = f".v{volume_input}"
        break
    

for runs in range(150):
    try:
        run_raw = issue_map[counter]['Cover']
        issue_raw = issue_map[counter]['Issue']
        story_name_raw = issue_map[counter]['Longest Story']
        pub_date_raw = issue_map[counter]['Publication Date']

        run_split = run_raw.split(" (",1)[0]
        if ' ' in run_split:
            run = run_split.replace(" ", ".")
        else:
            run = run_split
        
        issue_number_s1 = issue_raw.split("#",1)[1]
        issue_number_s2 = issue_number_s1.split(" ",1)[0]
        issue_number = int(issue_number_s2)
        
        if story_name_raw is None:
            story_name = ''
        elif 'no title' in story_name_raw:
            story_name = ''
        else:
            story_name_rem_end = story_name_raw.split(" (",1)[0]
            story_name_rem_chars = re.sub(r"[\[\"!,'’:?;\]]", '', story_name_rem_end)
            story_name = story_name_rem_chars.replace(" ", ".")

        if pub_date_raw is None:
            pub_date_input = input(f"If known, enter publication year for {run} {volume} issue {issue_number}: ")
            if pub_date_input == '':
                pub_date = "Unknown"
                break
            else:
                pub_date = pub_date_input
        else:
            pub_date = re.sub(r'\D', '', pub_date_raw)

        comic_filename = f"{run}{volume}.{issue_number:03d}{story_name}.({pub_date}).cbz"

        if run or run_split in folder_path_input:
            pass
        else:
            print("Please ensure you have entered the correct file path")
            break 

        for filename in os.listdir(folder_path_input):
            if f" {issue_number:03d}" in filename:
                old_filename = os.path.join(folder_path_input, filename)
                new_filename = os.path.join(folder_path_input, comic_filename)
                os.rename(old_filename, new_filename)
                print(f"{filename} found, renamed to {new_filename}")
    except IndexError or FileExistsError:
        continue        

    counter += 1

print("Complete")