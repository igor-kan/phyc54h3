import json

notebook_path = '/home/igorkan/repos/phyc54h3/solutions/taylor-chapter-6-problems.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Ensure the first cell is markdown and add YAML
if nb['cells'][0]['cell_type'] == 'markdown':
    source = nb['cells'][0]['source']
    # Check if YAML already exists
    if not source[0].startswith('---'):
        yaml_header = [
            "---\n",
            "title: \"Interactive: Taylor Chapter 6 Problems\"\n",
            "subtitle: \"Jupyter notebook with interactive Plotly visualizations and code solutions.\"\n",
            "date: \"2026-09-09\"\n",
            "categories: [interactive, python, jupyter, classical-mechanics]\n",
            "---\n\n"
        ]
        nb['cells'][0]['source'] = yaml_header + source

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

