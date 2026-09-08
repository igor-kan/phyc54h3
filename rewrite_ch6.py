import re

with open('/home/igorkan/repos/phyc54h3/notes/taylor-chapter-6-calculus-of-variations.qmd', 'r') as f:
    text = f.read()

# Extract sections
# Intro
intro_match = re.search(r'(---.*?# Introduction to the Calculus of Variations.*?)(?=## 6\.1 Two Examples)', text, re.DOTALL)
intro = intro_match.group(1)

# 6.1 Setup Shortest path
shortest_setup_match = re.search(r'(### Example 1: The Shortest Path Between Two Points.*?)(?=### Example 2: The Brachistochrone Problem)', text, re.DOTALL)
shortest_setup = shortest_setup_match.group(1)

# 6.1 Setup Brach (to be merged later)
brach_setup_match = re.search(r'(### Example 2: The Brachistochrone Problem.*?)(?=## 6\.2 The Euler-Lagrange Equation)', text, re.DOTALL)
brach_setup = brach_setup_match.group(1)

# 6.2 E-L Equation
el_match = re.search(r'(## 6\.2 The Euler-Lagrange Equation.*?)(?=### ⚠️ Stationary Action vs)', text, re.DOTALL)
el_eq = el_match.group(1)

# Min Max details (My added section)
min_max_details_match = re.search(r'(### ⚠️ Stationary Action vs\. "Least" Action: Minimum, Maximum, or Saddle Point\?.*?)(?=## 6\.3 Applications of the Euler-Lagrange Equation)', text, re.DOTALL)
min_max_details = min_max_details_match.group(1)

# 6.3 Shortest Path Revisited
shortest_sol_match = re.search(r'(### 1\. Shortest Path Revisited.*?)(?=### 2\. The Brachistochrone Solution)', text, re.DOTALL)
shortest_sol = shortest_sol_match.group(1)

# 6.3 Brach Solution
brach_sol_match = re.search(r'(### 2\. The Brachistochrone Solution.*?)(?=## 6\.4 More Than Two Variables)', text, re.DOTALL)
brach_sol = brach_sol_match.group(1)

# 6.4 More than Two Variables
more_vars_match = re.search(r'(## 6\.4 More Than Two Variables.*)', text, re.DOTALL)
more_vars = more_vars_match.group(1)

# Constructing the new document
new_doc = []

# Intro
new_doc.append(intro.strip())

# 6.1 Two Examples
new_doc.append("\n\n## 6.1 Two Examples\n")
new_doc.append("The calculus of variations involves finding the minimum or maximum of a quantity that is expressible as an integral. To see how this can arise, let's start with two simple, concrete examples.\n\n")
new_doc.append(shortest_setup.replace("### Example 1: The Shortest Path Between Two Points", "### The Shortest Path between Two Points").strip())

new_doc.append("\n\n### Fermat's Principle\n")
new_doc.append("A similar problem is to find the path that light will follow between two points. Fermat's principle states that the path taken by light is the one for which the time of travel is minimum (or more precisely, stationary).\n")
new_doc.append("The time to travel a short distance $ds$ is $ds/v$, where $v = c/n(x,y)$ is the speed of light in a medium with refractive index $n(x,y)$. The total time is:\n")
new_doc.append("$$ t = \\int_1^2 \\frac{ds}{v} = \\frac{1}{c} \\int_{x_1}^{x_2} n(x, y) \\sqrt{1 + (y')^2} \\, dx $$\n")
new_doc.append("As with the shortest path, we seek a function $y(x)$ that makes this integral stationary. In elementary calculus, a point where $df/dx = 0$ can be a maximum, minimum, or neither. Similarly, in the calculus of variations, making an integral stationary means an infinitesimal variation of the path leaves the integral unchanged, though it doesn't guarantee a strict minimum.")

# 6.2 The Euler-Lagrange Equation
new_doc.append("\n\n" + el_eq.strip())

# 6.3 Applications of the Euler-Lagrange Equation
new_doc.append("\n\n## 6.3 Applications of the Euler-Lagrange Equation\n")
new_doc.append("\n### Example 6.1: Shortest Path between Two Points\n")
# Remove the old header from shortest_sol
s_sol_clean = shortest_sol.replace("### 1. Shortest Path Revisited", "").strip()
new_doc.append(s_sol_clean)

new_doc.append("\n\n### A Note on Variables\n")
new_doc.append("So far we have used $x$ as the independent variable and $y$ as the dependent variable. In mechanics, the independent variable is usually time $t$, and the dependent variable is position $x(t)$. Sometimes, as in the next example, it is more convenient to use $y$ as the independent variable and $x(y)$ as the dependent variable.\n")

new_doc.append("\n\n### Example 6.2: The Brachistochrone\n")
# Merge Brach setup and solution
b_setup_clean = brach_setup.replace("### Example 2: The Brachistochrone Problem", "").strip()
b_sol_clean = brach_sol.replace("### 2. The Brachistochrone Solution", "").replace("#### Problem Formulation & The Beltrami Identity", "#### Problem Formulation & The Beltrami Identity\n").strip()
new_doc.append(b_setup_clean + "\n\n" + b_sol_clean)

new_doc.append("\n\n### Maximum and Minimum vs. Stationary\n")
new_doc.append("You have probably noticed that we haven't rigorously checked if the cycloid gives a true *minimum* time, as opposed to a maximum or saddle point. For instance, the geodesic between two points on a globe is a great circle. While the shortest path is a great circle, the *long* way around the globe on the same great circle is also a stationary path, but it is neither a minimum nor a maximum (it's a saddle point).\n\n")
new_doc.append(min_max_details.replace("### ⚠️ Stationary Action vs. \"Least\" Action: Minimum, Maximum, or Saddle Point?", "#### ⚠️ Stationary Action vs. \"Least\" Action in Physics").strip())

# 6.4 More than Two Variables
new_doc.append("\n\n" + more_vars.strip())

with open('/home/igorkan/repos/phyc54h3/notes/taylor-chapter-6-calculus-of-variations.qmd', 'w') as f:
    f.write(''.join(new_doc) + '\n')
