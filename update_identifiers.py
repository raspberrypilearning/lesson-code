import os

root_dir = 'code'

def update_identifier(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        second_line = lines[1]

        identifier = second_line.split(':')[1].strip().strip("'")
        
        #  Update cc- to whatever you want as the prefix
        updated_identifier = f"identifier: 'cc-{identifier}'\n"

        lines[1] = updated_identifier

        with open(file_path, 'w') as file:
            file.writelines(lines)


def update_yml_files_in_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml'):
                file_path = os.path.join(root, file)
                update_identifier(file_path)
                print(f"Updated: {file_path}")


update_yml_files_in_dir(root_dir)
