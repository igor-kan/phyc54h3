import os
import glob
import re

base_dir = "/home/igorkan/repos/phyc54h3/extra"
qmd_files = glob.glob(os.path.join(base_dir, "*.qmd"))

def clean_content(content):
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        # Skip lines that are bolded prerequisite/corequisite markers
        if re.match(r'^\*\*(Prerequisite|Corequisite|Advanced Corequisite).*\*\*$', line.strip()):
            continue
        
        # Remove "Prerequisite", "Corequisite" lines even if they don't exactly match the bolding
        if "Corequisite for Taylor" in line or "Prerequisite for Taylor" in line:
            continue
            
        # Clean up "**Concept:**" and "**Application:**"
        line = line.replace('**Concept:** ', '')
        line = line.replace('**Application:** ', '')
        
        new_lines.append(line)
        
    # Join and then remove any double blank lines that might have been created
    text = '\n'.join(new_lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

for filepath in qmd_files:
    # index.qmd shouldn't need this, but it's safe to run over all if it doesn't match
    with open(filepath, 'r') as f:
        content = f.read()
        
    cleaned = clean_content(content)
    
    with open(filepath, 'w') as f:
        f.write(cleaned)

