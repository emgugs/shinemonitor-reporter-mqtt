import os

# List specific Python files to run
python_files = ['get_data.py', 'publish_data.py']

# Run each Python file
for file in python_files:
    os.system(f'python {file}')
