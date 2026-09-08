import re

def process_file(filepath, notes_filename):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    out_lines = []
    for line in lines:
        if line.startswith('subtitle: "Problem statements and'):
            line = line.replace('Problem statements and ', '')
        if line.startswith('This article contains full problem statements and'):
            line = line.replace('full problem statements and ', '')
        
        out_lines.append(line)
        
        match = re.match(r'^##\s+SECTION\s+([\d\.]+)\s+(.*)', line)
        if match:
            sec_num = match.group(1)
            sec_name = match.group(2)
            # Create a github-pages style anchor from the section name.
            # E.g. "7.1 Lagrange's Equations for Unconstrained Motion" -> "71-lagranges-equations-for-unconstrained-motion"
            anchor = (sec_num + " " + sec_name).lower()
            anchor = re.sub(r'[^a-z0-9\s-]', '', anchor)
            anchor = re.sub(r'\s+', '-', anchor)
            
            link = f"\n*(See [Section {sec_num} Notes](../notes/{notes_filename}#{anchor}))*\n"
            out_lines.append(link)
            
    with open(filepath, 'w') as f:
        f.writelines(out_lines)

process_file('/home/igorkan/repos/phyc54h3/solutions/taylor-chapter-7-problems.qmd', 'taylor-chapter-7-lagrange-equations.qmd')
process_file('/home/igorkan/repos/phyc54h3/solutions/taylor-chapter-6-problems.qmd', 'taylor-chapter-6-calculus-of-variations.qmd')
