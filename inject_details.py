import re

with open('/home/igorkan/repos/phyc54h3/extra/landau-chapter-1.qmd', 'r') as f:
    text = f.read()

# 1. Phase 1 Background Theory: Foundations
phase1_text = r"""
> [!NOTE]
> ### Phase 1 Background Theory: Foundations
> Before diving into the calculus of variations used in the text, it is essential to understand the difference between Newtonian and Lagrangian Mechanics.
> 
> **Newtonian Formulation:** Newtonian mechanics is based on differential equations (e.g., $F=ma$). It determines the system's state locally at every instant in time. It determines the system's path by looking forward one infinitesimal moment at a time.
> 
> **Lagrangian Formulation (Principle of Least Action):** This is an integral formulation. Instead of asking how the system evolves locally from moment to moment, it asks: Among all possible paths connecting initial time $t_1$ to final time $t_2$, which specific path will a particle take?
> 
> The Principle of Least Action answers: The system will choose the unique path where a specific mathematical quantity, called Action ($S$), is stationary (typically a minimum).
> 
> The state of a mechanical system is fully defined by its generalized coordinates ($q$) and generalized velocities ($\dot{q}$) at that moment. This defines its location in what is called phase space (or more precisely here, the configuration space tangent bundle). Therefore, the special function defined in the text, the Lagrangian ($L$), is a function of these variables: $L(q, \dot{q}, t)$. Typically, for non-relativistic systems, $L = T - V$ (Kinetic Energy minus Potential Energy).
> 
> Action is an integral functional of the path $q(t)$:
> $$S = \int_{t_1}^{t_2} L(q(t), \dot{q}(t), t) dt$$
> Action maps a function (the entire path) to a scalar number. We are looking for the path function $q(t)$ that minimizes this number.
"""

text = text.replace('## §1. Generalised co-ordinates', phase1_text + '\n## §1. Generalised co-ordinates')

# 2. Highlighted Section 1: Endpoints of Variation
endpoints_text = r"""
> [!TIP]
> ### Highlighted Section 1: Endpoints of Variation
> **Background Theory and Proof:**
> To find the minimum of normal calculus function $f(x)$, we introduce a small change $\Delta x$ near the assumed minimum $x^*$. If $x^*$ is truly a minimum, then $f(x^* + \Delta x) \geq f(x^*)$.
> 
> In the calculus of variations, we apply this analogy to functions. We assume $q(t)$ is the true, minimizing path. We define a nearby "varied" (but false) path:
> $$\text{varied path}(t) = q(t) + \delta q(t)$$
> Where $\delta q(t)$ is called the "variation" of the coordinates. It represents an arbitrary, infinitely small 'wiggle' or perturbation added to the true path at any time $t$ between $t_1$ and $t_2$.
> 
> **Missing Step Proof: Why must $\delta q(t_1) = \delta q(t_2) = 0$?**
> The problem of action minimization specifies a system starting at location $A$ at time $t_1$ and ending at location $B$ at time $t_2$. While we don't know the path between $A$ and $B$, we absolutely know where the system is at the initial and final times.
> 
> We define $q(t)$ as the true path. It must satisfy the boundary conditions: $q(t_1) = q^{(1)}$ (location $A$) and $q(t_2) = q^{(2)}$ (location $B$).
> We consider varied, alternative paths. For them to be valid alternative paths connecting $A$ to $B$, they must also satisfy those boundary conditions.
> 
> Let's test the varied path at $t_1$:
> $$\text{Varied Path}(t_1) = q(t_1) + \delta q(t_1)$$
> Since both paths must pass through the fixed initial point:
> $$q^{(1)} = q^{(1)} + \delta q(t_1) \implies \delta q(t_1) = 0$$
> The same logic holds for $t_2$. Therefore, the variation 'wiggle' must go to zero at the endpoints. The endpoints are 'pinned down'.
"""
text = text.replace('$$ \delta q(t_1) = \delta q(t_2) = 0. $$', '$$ \delta q(t_1) = \delta q(t_2) = 0. $$\n' + endpoints_text)


# 3. Footnote
footnote_text = r"""
> [!IMPORTANT]
> ### Highlighted Section 2 (Footnote): Stationary vs. Minimum
> *(Note: The original text includes a footnote here: "This formulation... is not always valid for the entire path of the system, but only for any sufficiently short segment of the path. The integral... for the entire path must have an extremum, but not necessarily a minimum.")*
> 
> **Background Theory on the highlighted portion:**
> This is a subtle but deep mathematically rigorous note. Landau is clarifying that while we derive Lagrange's equations assuming a minimum, it’s more correct to say we are seeking a stationary point.
> 
> This is analogous to elementary calculus. When we find points where $df/dx = 0$, we find global minima, local minima, local maxima, and even saddle points (neither min nor max). $df/dx = 0$ is a necessary condition for a maximum or minimum, but it only technically means the function is flat at that point—it is stationary.
> 
> In mechanics, the true principle is stationary action ($\delta S = 0$). For simple systems and sufficiently short time intervals $[t_1, t_2]$, this stationary point is usually a true minimum. (Consider a curved surface; a direct line between two nearby points is always a minimum distance. If you go halfway around a sphere, many paths are the same distance).
> 
> The crucial point made in the footnote is this: the derivation of the equations of motion only uses the derivative condition $\delta S = 0$. They do not depend on the "second derivative test" (which determines if it is truly a max or min). Therefore, the Lagrange equations derived assuming $\delta S=0$ are mathematically correct for finding the equations of motion whether the path is a minimum or just stationary.
"""
text = text.replace('takes the least possible value. The function $L$ is called the Lagrangian of the system concerned, and the integral $S$ is called the action.', 'takes the least possible value. The function $L$ is called the Lagrangian of the system concerned, and the integral $S$ is called the action.\n' + footnote_text)


# 4. Highlighted Section 1: Taylor Series and the First Variation
taylor_text = r"""
> [!TIP]
> ### Highlighted Section 1: Taylor Series and the First Variation
> **Background Theory: Multivariable Taylor Expansion**
> To understand "expanded in powers," we need the background on Taylor series for functions of multiple variables.
> 
> For a function of one variable, $f(x^*+\Delta x) \approx f(x^*) + f'(x^*)\Delta x + \frac{1}{2}f''(x^*)(\Delta x)^2 + \dots$. A minimum condition is $f'(x^*)\Delta x = 0$ for all $\Delta x$, necessitating $f'(x^*)=0$. We only care about the first power ($\Delta x^1$) term to find stationary points.
> 
> The Lagrangian $L(q, \dot{q}, t)$ is a function of multiple independent variables. We are wiggling two of them at once: $q \to q+\delta q$ and $\dot{q} \to \dot{q}+\delta \dot{q}$. The background Taylor formula needed is:
> $$f(x+\Delta x, y+\Delta y, t) \approx f(x,y,t) + \frac{\partial f}{\partial x}\Delta x + \frac{\partial f}{\partial y}\Delta y + \mathcal{O}(2^{\text{nd}} \text{ order})$$
> We ignore higher-order terms ($(\delta q)^2$, $\delta q\delta \dot{q}$, etc.) because the variation $\delta q$ is chosen to be infinitesimal (infinitely small).
> 
> **Missing Mathematical Proof of the expansion shown:**
> Applying the background Taylor formula above to $L$:
> $$L(q + \delta q, \dot{q} + \delta \dot{q}, t) \approx L(q, \dot{q}, t) + \frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial \dot{q}}\delta \dot{q}$$
> We now calculate the change in the integrand:
> $$\delta L \approx \left[ L(q, \dot{q}, t) + \frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial \dot{q}}\delta \dot{q} \right] - L(q, \dot{q}, t)$$
> $$\delta L = \frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial \dot{q}}\delta \dot{q}$$
> We have strictly defined the "first variation" $\delta L$ as only those terms that are linear (first order) in the "wiggles" $\delta q$ and $\delta \dot{q}$. This justifies the steps Landau takes. The Principle of Stationary Action now states that the total first variation of action must be zero:
> $$\delta S = \int_{t_1}^{t_2} \delta L dt = 0 \implies \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial \dot{q}}\delta \dot{q} \right) dt = 0$$
"""
text = text.replace('Thus the principle of least action may be written in the form\n$$ \delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) dt = 0, $$', 'Thus the principle of least action may be written in the form\n$$ \delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) dt = 0, $$\n' + taylor_text)

# 5. Effecting the Variation
effecting_text = r"""
> [!NOTE]
> ### Highlighted Section 2: Effecting the Variation
> **Explanation:** As proven in the missing steps above, this highlighted phrase simply means substituting the result of the Taylor expansion back into the integrand. It takes the abstract concept of "changing $L$ because we wiggled the path" and turns it into concrete calculus using partial derivatives.
"""
text = text.replace('$$ \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot{q} \right) dt = 0. $$', '$$ \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot{q} \right) dt = 0. $$\n' + effecting_text)

# 6. Commuting Derivatives & 7. Integration by Parts
commuting_text = r"""
> [!TIP]
> ### Highlighted Section 3: Defining and Commuting Derivatives
> **Background Theory and Proof:**
> This is a critical concept in the calculus of variations: the varied position $q$ and varied velocity $\dot{q}$ are related because velocity is just the derivative of position.
> 
> **Proof:**
> Velocity is $\dot{q} = \frac{dq}{dt}$. Now we consider the "wiggle". The varied velocity (let's call it $V_{varied}$) must be the time derivative of the varied position.
> $$V_{varied}(t) = \frac{d}{dt} \left( \text{varied path}(t) \right) = \frac{d}{dt} [q(t) + \delta q(t)]$$
> Because differentiation is linear, this is:
> $$V_{varied}(t) = \frac{dq(t)}{dt} + \frac{d(\delta q(t))}{dt} = \dot{q}(t) + \frac{d}{dt}\delta q(t)$$
> We also defined varied velocity as the true velocity plus a velocity wiggle: $\text{varied velocity} = \dot{q}(t) + \delta \dot{q}(t)$.
> Comparing the two expressions for varied velocity:
> $$\dot{q}(t) + \frac{d}{dt}\delta q(t) = \dot{q}(t) + \delta \dot{q}(t) \implies \delta \dot{q}(t) = \frac{d}{dt}\delta q(t)$$
> The highlighted equation is proven. The variation ($\delta$) operator and the time derivative ($d/dt$) commute.
> 
> ---
> 
> ### Detailed Proof of Missing Steps: Integration by Parts
> The textbook immediately jumps from the commuter relationship to the result in (2.5) with the integration by parts trick. It skips the crucial steps of how parts is applied and why the boundary term vanishes. I will fill this gap.
> 
> We are solving:
> $$\int_{t_1}^{t_2} \frac{\partial L}{\partial q}\delta q dt + \int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}}\delta \dot{q} dt = 0$$
> Let's focus only on the second integral. We use the commuter result proven above to rewrite it:
> $$\text{Target integral} = \int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}} \frac{d(\delta q)}{dt} dt$$
> 
> **Missing Step: Setting up Integration by Parts**
> Standard Integration by Parts is: $\int_a^b u dv = [uv]_a^b - \int_a^b v du$.
> Our target integral is $\int \text{Term1} \cdot \text{DerivativeTerm2} \cdot dt$.
> 
> *   $u = \frac{\partial L}{\partial \dot{q}}$
> *   $dv = \frac{d(\delta q)}{dt} dt = d(\delta q)$
> 
> Now, calculate the remaining required pieces:
> *   $du = \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) dt$. (This is applying the total time derivative to a partial derivative, a common operation in mechanics).
> *   $v = \delta q$
> 
> Apply the Parts Formula:
> $$\int_{t_1}^{t_2} \underbrace{\frac{\partial L}{\partial \dot{q}}}_{u} \underbrace{\frac{d(\delta q)}{dt} dt}_{dv} = \left[ \underbrace{\frac{\partial L}{\partial \dot{q}}}_{u}\underbrace{\delta q}_{v} \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \underbrace{\delta q}_{v} \underbrace{\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}} \right) dt}_{du}$$
> 
> **Missing Step Proof: Boundary Term Vanishes**
> Let's look at the "uv term":
> $$\text{Boundary Term} = \left[ \frac{\partial L}{\partial \dot{q}}(t_2)\delta q(t_2) \right] - \left[ \frac{\partial L}{\partial \dot{q}}(t_1)\delta q(t_1) \right]$$
> Remember we just proved: $\delta q(t_1) = 0$ and $\delta q(t_2) = 0$. The wiggle height is zero at both ends. Substituting this in:
> $$\text{Boundary Term} = (\text{stuff} \cdot 0) - (\text{other stuff} \cdot 0) = 0$$
> The entire boundary term vanishes identically.
> 
> **Assemble the results:**
> Substitute the integration by parts result back into the main integral:
> $$\delta S = \int_{t_1}^{t_2} \frac{\partial L}{\partial q}\delta q dt + 0 - \int_{t_1}^{t_2} \delta q \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}} \right) dt = 0$$
> Both integrals have the common arbitrary wiggle function $\delta q(t)$, so we collect the terms together:
> $$\delta S = \int_{t_1}^{t_2} \left[ \frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) \right] \delta q(t) dt = 0$$
"""
text = text.replace('$$ \delta S = \left[ \frac{\partial L}{\partial \dot{q}} \delta q \right]_{t_1}^{t_2} + \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt = 0. $$', '$$ \delta S = \left[ \frac{\partial L}{\partial \dot{q}} \delta q \right]_{t_1}^{t_2} + \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt = 0. $$\n' + commuting_text)

# 8. Fundamental Lemma
lemma_text = r"""
> [!NOTE]
> ### Detailed Theory Background: The Fundamental Lemma of the Calculus of Variations
> How do we go from the integral above to saying the term inside the bracket is zero? This is based on a foundational background theory theorem.
> 
> The total integral of $( (\text{TermA}) \cdot (\text{arbitrary small wiggle } \delta q) )$ must be zero. Since $\delta q(t)$ can be any function we want (it's arbitrary between the fixed endpoints), imagine we want $\delta S > 0$. If "TermA" was positive at some time $t^*$, we could choose a wiggle $\delta q$ that is also non-zero and positive around $t^*$ and zero elsewhere. This would make the integrand $(A \cdot B)$ non-negative and positive near $t^*$, forcing the total integral to be positive, contradicting $\delta S=0$.
> 
> The only mathematical way that the integral can always be exactly zero, regardless of what wiggle $\delta q$ we pick, is if the first term, (TermA), is zero everywhere.
> 
> This forces the term inside the parenthesis to be zero:
> $$\frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) = 0$$
> Rearranging to the conventional textbook form:
> $$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0$$
> This is the Euler-Lagrange Equation derived for a system with 1 degree of freedom (1 coordinate $q$).
"""
text = text.replace('$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0. $$', '$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0. $$\n' + lemma_text)

# 9. Multiple Degrees of Freedom
multidof_text = r"""
> [!TIP]
> ### Highlighted Section: Multiple Degrees of Freedom
> **Background Theory and Missing Step:**
> Systems are complex; we use multiple coordinates $q_i$. For example, a single particle needs three coordinates ($x, y, z$). So we need $s$ functions: $q_1(t), q_2(t), \dots, q_s(t)$. This means the "wiggle" is now a vector wiggle: $\delta \mathbf{q}(t) = (\delta q_1(t), \delta q_2(t), \dots, \delta q_s(t))$.
> 
> The background theory needed is Taylor expansion for many variables. We expand the variation of $L$:
> $$\delta L = \sum_{i=1}^s \frac{\partial L}{\partial q_i}\delta q_i + \sum_{i=1}^s \frac{\partial L}{\partial \dot{q}_i}\delta \dot{q}_i$$
> Now, plug this sum back into the main action integral:
> $$\delta S = \int_{t_1}^{t_2} \left( \sum_{i=1}^s \frac{\partial L}{\partial q_i}\delta q_i + \sum_{i=1}^s \frac{\partial L}{\partial \dot{q}_i}\delta \dot{q}_i \right) dt = 0$$
> $$\delta S = \sum_{i=1}^s \left[ \int_{t_1}^{t_2} \frac{\partial L}{\partial q_i}\delta q_i dt + \int_{t_1}^{t_2} \frac{\partial L}{\partial \dot{q}_i}\delta \dot{q}_i dt \right] = 0$$
> 
> The key highlighted statement—that they are varied independently—means that $\delta q_1(t)$ is completely unrelated to $\delta q_2(t)$. They do not influence each other.
> 
> Because of this independence, we can apply the "wiggle logic" (Fundamental Lemma) from the previous step to every single coordinate individually. (E.g., imagine you set all wiggles $\delta q_{j=2,3,\dots,s} = 0$, and only vary $\delta q_1$. The remaining terms in the integral for only $i=1$ must still be exactly zero because $\delta S=0$. This forces the single EL equation to hold for coordinate $i=1$. We repeat this argument for every coordinate index).
> 
> This results in the set of $s$ independent equations.
"""
text = text.replace('$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0 \quad (i = 1, 2, \dots, s). $$', '$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0 \quad (i = 1, 2, \dots, s). $$\n' + multidof_text)

# 10. Non-Interacting Subsystems
additivity_text = r"""
> [!NOTE]
> ### Highlighted Section: Non-Interacting Subsystems
> **Explanation:**
> This highlighted section discusses the property of additivity of the Lagrangian.
> Imagine two mechanical systems: a ball bouncing in London (System A) and a moon orbiting Jupiter (System B). They don't interact.
> 
> *   System A has coordinates $q_A$ and varied position $q_A+\delta q_A$. Its action change is $\delta S_A = 0$, leading to Euler-Lagrange equations for A.
> *   System B has coordinates $q_B$ and varied position $q_B+\delta q_B$. Its action change is $\delta S_B = 0$, leading to Euler-Lagrange equations for B.
> 
> If you decide to treat them as a single mathematical system:
> *   Total Coordinates $q_{Total} = (q_A, q_B)$.
> *   Total varied wiggles $\delta q_{Total} = (\delta q_A, \delta q_B)$.
> 
> Because the two systems do not interact, the total Lagrangian must be the sum of individual Lagrangians (kinetic energies add, non-existent interaction potentials are zero).
> $$L_{Total}(q_{Total}, \dot{q}_{Total}, t) = L_A(q_A, \dot{q}_A, t) + L_B(q_B, \dot{q}_B, t)$$
> The total Action is $S = \int L_{Total} dt = \int (L_A+L_B) dt = \int L_A dt + \int L_B dt = S_A + S_B$.
> 
> Varying the total system: $\delta S = \delta(S_A+S_B) = \delta S_A + \delta S_B = 0 + 0 = 0$.
> 
> This additivity is a fundamental result: the Lagrangian of non-interacting systems must be extensive.
"""
text = text.replace('$$ \lim L = L_A + L_B. $$', '$$ \lim L = L_A + L_B. $$\n' + additivity_text)

# 11. Arbitrariness and Units
arbitrary_text = r"""
> [!NOTE]
> ### Highlighted Section: Arbitrariness and Units
> **Explanation:**
> The text states that Lagrangians are unique up to an overall multiplicative constant.
> Let the true Lagrangian be $L_{true}$ which gives stationary path $S_{true}$ leading to Euler-Lagrange (EL) equations that look like: $\text{Term1} - \text{Term2} = 0$.
> 
> Imagine a student uses a varied Lagrangian $L' = k \cdot L_{true}$, where $k$ is a non-zero constant (like a conversion factor).
> Let's plug $L'$ into the Euler-Lagrange derivative operator:
> $$\frac{d}{dt}\frac{\partial (kL_{true})}{\partial \dot{q}} - \frac{\partial(kL_{true})}{\partial q} = 0$$
> Since $k$ is a constant, we can pull it out of all derivatives:
> $$k \left[ \frac{d}{dt}\frac{\partial L_{true}}{\partial \dot{q}} - \frac{\partial L_{true}}{\partial q} \right] = 0$$
> $$k \cdot [ \text{original correct equations} ] = 0$$
> 
> Since $k$ is non-zero (you cannot multiply by zero), the only way the entire expression is true is if the bracketed part is zero. Physically, this means your choice of units (Joules vs. calories, or kilograms vs. pounds) doesn't change the derived physical laws derived from $L=T-V$. Units just scale the entire equation by a constant factor. Action $S$ has units of Energy $\times$ Time (or Planck's constant $h$).
"""
text = text.replace('choice of the unit of measurement of the Lagrangian, a matter to which we shall return in §4.', 'choice of the unit of measurement of the Lagrangian, a matter to which we shall return in §4.\n' + arbitrary_text)

# 12. Adding a Total Time Derivative
total_time_text = r"""
> [!TIP]
> ### Highlighted Section: Adding a Total Time Derivative
> **Detailed Mathematical Proof:**
> The textbook explains this via Action $S$ and Action variation $\delta S=0$. I will provide an alternative, more concrete proof based directly on the Lagrange differential equations. The textbook states that $L'(q, \dot{q}, t) = L(q, \dot{q}, t) + \frac{df(q,t)}{dt}$ leads to the same equations.
> 
> Let's calculate the Euler-Lagrange operator terms for the special added part, $\frac{df}{dt}$. Let's define the new potential change as $L_{added} = \frac{d}{dt}f(q(t), t)$.
> 
> **Background Theory needed: Total time derivative chain rule for $f(q,t)$:**
> $$\frac{df(q,t)}{dt} = \frac{\partial f}{\partial q}\frac{dq}{dt} + \frac{\partial f}{\partial t} = \frac{\partial f}{\partial q}\dot{q} + \frac{\partial f}{\partial t}$$
> 
> **Calculate the momentum term ($\partial L / \partial \dot{q}$):**
> $$\text{Partial Mom Term} = \frac{\partial}{\partial \dot{q}} \left( \frac{df}{dt} \right) = \frac{\partial}{\partial \dot{q}} \left[ \frac{\partial f}{\partial q}\dot{q} + \frac{\partial f}{\partial t} \right]$$
> The first term in the brackets is linear in $\dot{q}$, with coefficient $\frac{\partial f}{\partial q}$. The second term $\frac{\partial f}{\partial t}$ is independent of velocity $\dot{q}$ (it only depends on $q$ and $t$). So this derivative is:
> $$\frac{\partial L_{added}}{\partial \dot{q}} = \frac{\partial f}{\partial q}$$
> 
> **Calculate the entire velocity derivative part ($\frac{d}{dt} \frac{\partial L}{\partial \dot{q}}$):**
> $$\text{Vel Deriv Part} = \frac{d}{dt} \left( \frac{\partial f}{\partial q} \right)$$
> This is now a total time derivative applied to a partial derivative. This also requires background chain rule:
> $$\text{Vel Deriv Part} = \frac{\partial}{\partial q} \left( \frac{\partial f}{\partial q} \right)\dot{q} + \frac{\partial}{\partial t} \left( \frac{\partial f}{\partial q} \right) = \frac{\partial^2 f}{\partial q^2}\dot{q} + \frac{\partial^2 f}{\partial t \partial q}$$
> 
> **Calculate the position derivative term ($\partial L / \partial q$):**
> $$\text{Pos Deriv Part} = \frac{\partial}{\partial q} \left( \frac{df}{dt} \right) = \frac{\partial}{\partial q} \left[ \frac{\partial f}{\partial q}\dot{q} + \frac{\partial f}{\partial t} \right]$$
> $$\text{Pos Deriv Part} = \left( \frac{\partial}{\partial q}\frac{\partial f}{\partial q} \right)\dot{q} + \frac{\partial}{\partial q}\frac{\partial f}{\partial t} = \frac{\partial^2 f}{\partial q^2}\dot{q} + \frac{\partial^2 f}{\partial q \partial t}$$
> 
> **Now combine them to find the Euler-Lagrange equations for the added term:**
> $$\text{E-L LHS of added term} = [\text{Vel Deriv Part}] - [\text{Pos Deriv Part}]$$
> $$= \left( \frac{\partial^2 f}{\partial q^2}\dot{q} + \frac{\partial^2 f}{\partial t \partial q} \right) - \left( \frac{\partial^2 f}{\partial q^2}\dot{q} + \frac{\partial^2 f}{\partial q \partial t} \right)$$
> 
> Since the higher-order partial derivatives commute for continuous functions ($\frac{\partial^2 f}{\partial t \partial q} = \frac{\partial^2 f}{\partial q \partial t}$), the parenthesis terms match perfectly.
> $$\text{E-L LHS of added term} = 0 - 0 = 0$$
> 
> This means adding a total time derivative $\frac{df}{dt}$ contributes exactly zero to the equations of motion. It doesn't change them. This proves the highlighted statement. Physically, this is akin to how potential energy is only defined up to an added constant; the difference in reference level doesn't change the derived force $F = -\nabla V$. This property is fundamental to gauge theory in electrodynamics and quantum field theory.
"""
text = text.replace('Thus the Lagrangian is defined only to within an additive total time derivative of any function of co-ordinates and time.', 'Thus the Lagrangian is defined only to within an additive total time derivative of any function of co-ordinates and time.\n' + total_time_text)

with open('/home/igorkan/repos/phyc54h3/extra/landau-chapter-1.qmd', 'w') as f:
    f.write(text)

