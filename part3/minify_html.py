import os
import re

templates_dir = 'templates'

print(f"Processing files in {templates_dir}...")

for filename in os.listdir(templates_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(templates_dir, filename)
        print(f"Minifying {filename}...")
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        # 1. Remove HTML comments <!-- ... -->
        # Use non-greedy match .*? and DOTALL to match newlines
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # 2. Collapse multiple whitespace characters (including newlines) into a single space
        content = re.sub(r'\s+', ' ', content)
        
        # 3. Remove whitespace between tags: > <  becomes ><
        content = re.sub(r'>\s+<', '><', content)
        
        # 4. Strip leading/trailing whitespace
        content = content.strip()
        
        with open(filepath, 'w') as f:
            f.write(content)

print("Done!")
