import os
import sys

# Locate the ensure library in the current environment
env_path = sys.prefix
ensure_main_path = os.path.join(env_path, 'Lib', 'site-packages', 'ensure', 'main.py')

# Check if the file exists
if not os.path.exists(ensure_main_path):
    print(f"File not found: {ensure_main_path}")
    sys.exit(1)

# Read the content of the main.py file
with open(ensure_main_path, 'r') as file:
    content = file.read()

# Replace assertRaisesRegexp with assertRaisesRegex
content = content.replace('assertRaisesRegexp', 'assertRaisesRegex')

# Write the modified content back to the main.py file
with open(ensure_main_path, 'w') as file:
    file.write(content)

print("Patched ensure library successfully.")