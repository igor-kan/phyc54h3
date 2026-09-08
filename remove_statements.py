import re

def process_file(filepath, notes_file):
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove all **Statement:** lines
    # It might be multi-line if the statement is long, but they seem to be one-liners in the provided output.
    # Actually, looking at Problem 7.47, it's one long line. So re.sub(r'\*\*Statement:\*\*.*?\n', '', content) might work if they are on one line.
    
    # Wait, looking at Problem 7.10: 
    # **Statement:** A particle is confined to move on the surface of a circular cone with its axis on the z axis, vertex at the origin (pointing down), and half-angle a. The particle's position can be specified by two generalized coordinates, which you can choose to be the coordinates (p, 0) of cylindrical polar coordinates. Write down the equations that give the three Cartesian coordinates of the particle in terms of the generalized coordinates (p, 0) and vice versa.
    # It is indeed a single line.
    content = re.sub(r'\*\*Statement:\*\*.*\n', '', content)
    
    with open(filepath, 'w') as f:
        f.write(content)

process_file('/home/igorkan/repos/phyc54h3/solutions/taylor-chapter-7-problems.qmd', 'taylor-chapter-7-lagrange-equations.qmd')
process_file('/home/igorkan/repos/phyc54h3/solutions/taylor-chapter-6-problems.qmd', 'taylor-chapter-6-calculus-of-variations.qmd')
