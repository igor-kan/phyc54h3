import json

notebook_path = '/home/igorkan/repos/phyc54h3/solutions/Untitled.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Problem statements to add
problem_statements = [
    "### Problem 6.1\nFind the geodesics on the cone whose equation in cylindrical polar coordinates is z = Ap. [Let the required curve have the form 0 = 0(p).] Check your result for the case that 0.",
    "### Problem 6.2\nShow that the shortest path between two given points in a plane is a straight line, using plane polar coordinates.",
    "### Problem 6.3\nA surface of revolution is generated as follows: Two fixed points (x1, y1) and (x2, y2) in the x, y plane are joined by a curve y = y(x). [Actually you'll make life easier if you start out writing this as x = x(y).] The whole curve is now rotated about the x axis to generate a surface. Show that the curve for which the area of the surface is minimum has the form y = y0 cosh[(x — x0)/y0], where x0 and y0 are constants. (This is often called the soap-bubble problem, since the resulting surface is usually the shape of a soap bubble held by two coaxial rings of radii y1 and y2.)",
    "### Problem 6.4\nIf you haven't done it, take a look at Problem 6.10. Here is a second situation in which you can find a \"first integral\" of the Euler—Lagrange equation: Argue that if it happens that the integrand f (y, y', x) does not depend explicitly on x, that is, f = f (y, y'), then df/dx = (partial f / partial y) y' + (partial f / partial y') y''. Use the Euler—Lagrange equation to replace partial f / partial y on the right, and hence show that d/dx [f - y' (partial f / partial y')] = 0. This gives you the first integral f — y'(partial f / partial y') = const. This can simplify several calculations. (See Problems 6.21 and 6.22 for examples.) In Lagrangian mechanics, where the independent variable is the time t, the corresponding result is that if the Lagrangian function is independent of t, then energy is conserved. (See Section 7.8.)",
    "### Problem 6.5\nIn Example 6.2 (page 222) we found the brachistochrone by exchanging the variables x and y. Here is a method that avoids that exchange: Write the time as in Equation (6.19) but using x as the variable of integration. Your integrand should have the form f (y, y', x) = sqrt(y'^2 + 1)/sqrt(y). Since this is independent of x, you can invoke the \"first integral\" (6.43) of Problem 6.20. Show that this differential equation leads you to the same integral for x as in Equation (6.23) and hence to the same curve as before.",
    "### Problem 6.6\nYou are given a string of fixed length l with one end fastened at the origin 0, and you are to place the string in the xy plane with its other end on the x axis in such a way as to enclose the maximum area between the string and the x axis. Show that the required shape is a semicircle. The area enclosed is of course integral y dx, but show that you can rewrite this in the form integral y sqrt(1 - y'^2) ds, where s denotes the distance measured along the string from 0, where y' denotes dy/ds. Since f does not involve the independent variable s explicitly, you can exploit the \"first integral\" (6.43) of Problem 6.20.",
    "### Problem 6.7\nAn aircraft whose airspeed is v0 has to fly from town 0 (at the origin) to town P, which is a distance D due east. There is a steady gentle wind shear, such that v_wind = V y x_hat, where x and y are measured east and north respectively. Find the path, y = y(x), which the plane should follow to minimize its flight time, as follows: (a) Find the plane's ground speed in terms of v0, V, theta (the angle by which the plane heads to the north of east), and the plane's position. (b) Write down the time of flight as an integral of the form integral f dx. Show that if we assume that y' and theta both remain small (as is certainly reasonable if the wind speed is not too large), then the integrand f takes the approximate form f = (1 + 1/2 y'^2)/(1 + ky) (times an uninteresting constant) where k = V/v0. (c) Write down the Euler—Lagrange equation that determines the best path. To solve it, make the intelligent guess that y(x) = Ax(D — x), which clearly passes through the two towns. Show that it satisfies the EulerLagrange equation, provided A = ... How far north does this path take the plane, if D = 2000 miles, v0 = 500 mph, and the wind shear is V = 0.5 mph/mi? How much time does the plane save by following this path?",
    "### Problem 6.8\nConsider a medium in which the refractive index n is inversely proportional to r^2 ; that is, n = a / r^2, where r is the distance from the origin. Use Fermat's principle, that the integral (6.3) is stationary, to find the path of a ray of light travelling in a plane containing the origin. [Hint: Use twodimensional polar coordinates and write the path as phi = phi(r). The Fermat integral should have the form integral f (phi, phi', r) dr, where f is actually independent of phi. The Euler—Lagrange equation therefore reduces to partial f / partial phi' = const. You can solve this for phi' and then integrate to give phi as a function of r. Rewrite this to give r as a function of phi and show that the resulting path is a circle through the origin. Discuss the progress of the light around the circle.]",
    "### Problem 6.9\nConsider a single loop of the cycloid (6.26) with a fixed value of a, as shown in Figure 6.11. A car is released from rest at a point P0 anywhere on the track between 0 and the lowest point P. Show that the time for the cart to roll from P0 to P is given by the integral ... and prove that this time is equal to pi sqrt(a/g). Since this is independent of the position of P0, the cart takes the same time to roll from P0 to P whether P0 is at 0, or anywhere between 0 and P, even infinitesimally close to P. Explain qualitatively how this surprising result can possibly be true.",
    "### Problem 6.10\nGive in detail the argument that leads from the stationary property of the integral (6.30) to the two Euler—Lagrange equations (6.34).",
    "### Problem 6.11\nProve that the shortest path between two points in three dimensions is a straight line. Write the path in the parametric form x = x(u), y = y(u), and z = z(u) and then use the three Euler—Lagrange equations corresponding to (6.34).",
    "### Problem 6.12\nThe shortest path between two points on a curved surface, such as the surface of a sphere, is called a geodesic. To find a geodesic, one has first to set up an integral that gives the length of a path on the surface in question. Use spherical polar coordinates $(r, \\theta, \\phi)$ to show that the length of a path joining two points on a sphere of radius $R$ is ...",
    "### Problem 6.13\nFind the equation of the path $y(x)$ that makes the integral $ \\int_{x_1}^{x_2} \\sqrt{x} \\sqrt{1 + (y')^2} dx $ stationary.",
    "### Problem 6.14\nFind the Euler-Lagrange equation for the functional $\\int_{x_1}^{x_2} x^2 (y')^2 dx$.",
    "### Problem 6.15\nFind the Euler-Lagrange equation for the functional $S = \\int (y'^2 + y^2) dx$.",
    "### Problem 6.16\nFind the geodesic on the surface of a cylinder $R = \\text{const}$.",
    "### Problem 6.17\nFind the geodesic on a cone of half-angle $\\alpha$.",
    "### Problem 6.18\nFermat's principle states that light travels between two points along the path that requires the least time. Show that this leads to Snell's Law $n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$ for light crossing a boundary between media with refractive indices $n_1$ and $n_2$.",
    "### Problem 6.19\nA particle is constrained to move on the surface of a sphere. Formulate the integral for action and extract the equations of motion."
]

# Create markdown cells
md_cells = []
for stmt in problem_statements:
    cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [stmt]
    }
    md_cells.append(cell)

# Combine: place problem statements before the existing cells
nb['cells'] = md_cells + nb['cells']

# Also add a title cell
title_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": ["# Taylor Chapter 6: Calculus of Variations Problems\n\nBelow are the problem statements for Chapter 6, followed by interactive code solutions and visualizations."]
}
nb['cells'].insert(0, title_cell)

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

