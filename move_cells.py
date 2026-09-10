import json

notebook_path = '/home/igorkan/repos/phyc54h3/solutions/Untitled.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

cells = nb['cells']

# We know the structure:
# 0: Title cell
# 1-19: Problem 6.1 to 6.19
# 20+: The code cell (and potentially its output cells) for Problem 6.1

# Let's find the index of Problem 6.1
p6_1_idx = -1
for i, cell in enumerate(cells):
    if cell['cell_type'] == 'markdown' and '### Problem 6.1' in cell['source'][0]:
        p6_1_idx = i
        break

if p6_1_idx != -1:
    # The problem statements are 19 cells starting from index 1 (if title is 0)
    # The code cell and output is at the very end. Let's just grab everything after the last problem statement
    # The last problem statement is "Problem 6.19"
    p6_19_idx = -1
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'markdown' and '### Problem 6.19' in cell['source'][0]:
            p6_19_idx = i
            break
            
    if p6_19_idx != -1:
        # All cells after p6_19_idx belong to the solution of 6.1
        solution_cells = cells[p6_19_idx+1:]
        
        # Remove them from the end
        cells = cells[:p6_19_idx+1]
        
        # Insert them right after Problem 6.1 (p6_1_idx)
        # Note: When we insert, we need to preserve order, so we insert the list of solution cells
        new_cells = cells[:p6_1_idx+1] + solution_cells + cells[p6_1_idx+1:]
        
        nb['cells'] = new_cells

        with open(notebook_path, 'w') as f:
            json.dump(nb, f, indent=1)
        
        print("Success! Moved solution cells under Problem 6.1")
    else:
        print("Could not find Problem 6.19")
else:
    print("Could not find Problem 6.1")
