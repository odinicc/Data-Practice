import subprocess
import json
import subprocess
import threading
import concurrent.futures

# List of scripts to run
script_paths = ["11_find_campaign_tree.py", "12_find_segment.py", "16_find_cam_name.py" , "13_find_content_name.py"]

# Function to run a script and return its output
def run_script(script_path):
    result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, text=True,encoding='utf-8')
    return result.stdout

# Function to run scripts in parallel
def run_scripts_parallel():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit each script to the executor
        futures = {executor.submit(run_script, script): script for script in script_paths}

        # Get the outputs of each script
        for future in concurrent.futures.as_completed(futures):
            script = futures[future]
            output = future.result()
            script_outputs[script] = output

# Function to remove lines
def remove_newlines_and_quotes(input_string):
    # Remove newline symbols
    cleaned_string = input_string.replace("\n", "")
    # Remove single and double quotes
    cleaned_string = cleaned_string.replace("'", "").replace('"', '')
    return cleaned_string


# Dictionary mapping script paths to their outputs
script_outputs = {}

# Run scripts in parallel
run_scripts_parallel()

# Save outputs in variables
find_campaign_tree_output = script_outputs["11_find_campaign_tree.py"]
find_segment_output = script_outputs["12_find_segment.py"]
find_cam_name_output = script_outputs["16_find_cam_name.py"]
find_content_output = script_outputs["13_find_content_name.py"]

campaign_tree_id = remove_newlines_and_quotes(find_campaign_tree_output)
segment_id = int(remove_newlines_and_quotes(find_segment_output))
cam_name_str = 'A ' + str(remove_newlines_and_quotes(find_cam_name_output))
content_resp = remove_newlines_and_quotes(find_content_output)

# Remove the square brackets
content_resp = content_resp.strip('[]')

# Split the string into a list
content_list = content_resp.split(', ')

# Convert numerical strings to integers
content_list = [int(item) if item.isdigit() else item for item in content_list]
content_channel = content_list[0]
content_id = content_list[1]
variant_id = content_list[2]

subfolder = 'campaign jsons'
#pick up proper json tree
filename = campaign_tree_id + '.json'
filepath = subfolder + '/' + filename

with open(filepath, 'r',encoding="utf8") as file:
    data_in_json = json.load(file)


#function to put placeholders to campaign Json
def replace_value(obj, old_value, new_value):
    if isinstance(obj, dict):
        return {k: replace_value(v, old_value, new_value) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_value(elem, old_value, new_value) for elem in obj]
    elif obj == old_value:
        return new_value
    else:
        return obj

#Update segment to Current
old_value = "segmentId_placeholder"
new_value = segment_id
data_in_json = replace_value(data_in_json, old_value, new_value)

#Update content channel to Current
old_value = "channel_placeholder"
new_value = content_channel
data_in_json = replace_value(data_in_json, old_value, new_value)

#Update content variant to Current
old_value = "variant_placeholder"
new_value = variant_id
data_in_json = replace_value(data_in_json, old_value, new_value)

#Update content to Current
old_value = "contentunit_placeholder"
new_value = content_id
data_in_json = replace_value(data_in_json, old_value, new_value)

#Update cam description to Current
old_value = "cam_name_placeholder"
new_value = cam_name_str
data_in_json = replace_value(data_in_json, old_value, new_value)

with open('Campaign_from_promt.json', 'w',encoding='utf8') as file:
    json.dump(data_in_json, file, indent=4,ensure_ascii=False)