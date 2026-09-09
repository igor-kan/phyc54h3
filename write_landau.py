content = r"""---
title: "Landau & Lifshitz: Mechanics - Chapter I"
subtitle: "The Equations of Motion"
date: "2026-09-09"
date-modified: last-modified
categories: [landau, mechanics, reading]
format:
  html:
    toc: true
    math: true
---

# CHAPTER I: THE EQUATIONS OF MOTION

## §1. Generalised co-ordinates

ONE of the fundamental concepts of mechanics is that of a particle. By this we mean a body whose dimensions may be neglected in describing its motion. The possibility of so doing depends, of course, on the conditions of the problem concerned. For example, the planets may be regarded as particles in considering their motion about the Sun, but not in considering their rotation about their axes.

The position of a particle in space is defined by its radius vector $\mathbf{r}$, whose components are its Cartesian co-ordinates $x, y, z$. The derivative $\mathbf{v} = d\mathbf{r}/dt$ of $\mathbf{r}$ with respect to the time $t$ is called the velocity of the particle, and the second derivative $d^2\mathbf{r}/dt^2$ is its acceleration. In what follows we shall, as is customary, denote differentiation with respect to time by placing a dot above a letter: $\mathbf{v} = \dot{\mathbf{r}}$.

To define the position of a system of $N$ particles in space, it is necessary to specify $N$ radius vectors, i.e. $3N$ co-ordinates. The number of independent quantities which must be specified in order to define uniquely the position of any system is called the number of degrees of freedom; here, this number is $3N$. These quantities need not be the Cartesian co-ordinates of the particles, and the conditions of the problem may render some other choice of coordinates more convenient. Any $s$ quantities $q_1, q_2, \dots, q_s$ which completely define the position of a system with $s$ degrees of freedom are called generalised co-ordinates of the system, and the derivatives $\dot{q}_i$ are called its generalised velocities.

When the values of the generalised co-ordinates are specified, however, the "mechanical state" of the system at the instant considered is not yet determined in such a way that the position of the system at subsequent instants can be predicted. For given values of the co-ordinates, the system can have any velocities, and these affect the position of the system after an infinitesimal time interval $\Delta t$.

If all the co-ordinates and velocities are simultaneously specified, it is known from experience that the state of the system is completely determined and that its subsequent motion can, in principle, be calculated. Mathematically, this means that, if all the co-ordinates $q$ and velocities $\dot{q}$ are given at some instant, the accelerations $\ddot{q}$ at that instant are uniquely defined.

The relations between the accelerations, velocities and co-ordinates are called the equations of motion. They are second-order differential equations for the functions $q(t)$, and their integration makes possible, in principle, the determination of these functions and so of the path of the system.

## §2. The principle of least action

The most general formulation of the law governing the motion of mechanical systems is the principle of least action or Hamilton's principle, according to which every mechanical system is characterised by a definite function $L(q_1, q_2, \dots, q_s, \dot{q}_1, \dot{q}_2, \dots, \dot{q}_s, t)$ or briefly $L(q, \dot{q}, t)$, and the motion of the system is such that a certain condition is satisfied.

Let the system occupy, at the instants $t_1$ and $t_2$, positions defined by two sets of values of the co-ordinates, $q^{(1)}$ and $q^{(2)}$. Then the condition is that the system moves between these positions in such a way that the integral
$$ S = \int_{t_1}^{t_2} L(q, \dot{q}, t) dt $$
takes the least possible value. The function $L$ is called the Lagrangian of the system concerned, and the integral $S$ is called the action.

The fact that the Lagrangian contains only $q$ and $\dot{q}$, but not the higher derivatives $\ddot{q}, \dddot{q}$, etc., expresses the result already mentioned, that the mechanical state of the system is completely defined when the co-ordinates and velocities are given.

Let us now derive the differential equations which solve the problem of minimising the integral $S$. For simplicity, we shall at first assume that the system has only one degree of freedom, so that only one function $q(t)$ has to be determined.

Let $q = q(t)$ be the function for which $S$ is a minimum. This means that $S$ is increased when $q(t)$ is replaced by any function of the form
$$ q(t) + \delta q(t), $$
where $\delta q(t)$ is a function which is small everywhere in the interval of time from $t_1$ to $t_2$; $\delta q(t)$ is called a variation of the function $q(t)$. Since, for $t = t_1$ and for $t = t_2$, all the functions must take the values $q^{(1)}$ and $q^{(2)}$ respectively, it follows that
$$ \delta q(t_1) = \delta q(t_2) = 0. $$

The change in $S$ when $q$ is replaced by $q + \delta q$ is
$$ \int_{t_1}^{t_2} L(q + \delta q, \dot{q} + \delta \dot{q}, t) dt - \int_{t_1}^{t_2} L(q, \dot{q}, t) dt. $$

When this difference is expanded in powers of $\delta q$ and $\delta \dot{q}$ in the integrand, the leading terms are of the first order. The necessary condition for $S$ to have a minimum is that these terms (called the first variation, or simply the variation, of the integral) should be zero. Thus the principle of least action may be written in the form
$$ \delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) dt = 0, $$
or, effecting the variation,
$$ \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot{q} \right) dt = 0. $$

Since $\delta \dot{q} = \frac{d}{dt} \delta q$, we obtain, on integrating the second term by parts,
$$ \delta S = \left[ \frac{\partial L}{\partial \dot{q}} \delta q \right]_{t_1}^{t_2} + \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt = 0. $$

The conditions $\delta q(t_1) = \delta q(t_2) = 0$ show that the integrated term is zero. There remains an integral which must vanish for all values of $\delta q$. This can be so only if the integrand is zero identically. Thus we have
$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0. $$

When the system has more than one degree of freedom, the $s$ different functions $q_i(t)$ must be varied independently in the principle of least action. We then evidently obtain $s$ equations of the form
$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0 \quad (i = 1, 2, \dots, s). $$

These are the required differential equations, called in mechanics Lagrange's equations. If the Lagrangian of a given mechanical system is known, the equations give the relations between accelerations, velocities and co-ordinates, i.e. they are the equations of motion of the system.

Mathematically, the equations constitute a set of $s$ second-order equations for $s$ unknown functions $q_i(t)$. The general solution contains $2s$ arbitrary constants. To determine these constants and thereby to define uniquely the motion of the system, it is necessary to know the initial conditions which specify the state of the system at some given instant, for example the initial values of all the co-ordinates and velocities.

Let a mechanical system consist of two parts A and B which would, if closed, have Lagrangians $L_A$ and $L_B$ respectively. Then, in the limit where the distance between the parts becomes so large that the interaction between them may be neglected, the Lagrangian of the whole system tends to the value
$$ \lim L = L_A + L_B. $$

This additivity of the Lagrangian expresses the fact that the equations of motion of either of the two non-interacting parts cannot involve quantities pertaining to the other part.

It is evident that the multiplication of the Lagrangian of a mechanical system by an arbitrary constant has no effect on the equations of motion. From this, it might seem, the following important property of arbitrariness can be deduced: the Lagrangians of different isolated mechanical systems may be multiplied by different arbitrary constants. The additive property, however, removes this indefiniteness, since it admits only the simultaneous multiplication of the Lagrangians of all the systems by the same constant. This corresponds to the natural arbitrariness in the choice of the unit of measurement of the Lagrangian, a matter to which we shall return in §4.

One further general remark should be made. Let us consider two functions $L'(q, \dot{q}, t)$ and $L(q, \dot{q}, t)$, differing by the total derivative with respect to time of some function $f(q, t)$ of co-ordinates and time:
$$ L'(q, \dot{q}, t) = L(q, \dot{q}, t) + \frac{d}{dt} f(q, t). $$

The integrals calculated from these two functions are such that
$$ S' = \int_{t_1}^{t_2} L'(q, \dot{q}, t) dt = \int_{t_1}^{t_2} L(q, \dot{q}, t) dt + \int_{t_1}^{t_2} \frac{df}{dt} dt = S + f(q^{(2)}, t_2) - f(q^{(1)}, t_1), $$
i.e. they differ by a quantity which gives zero on variation, so that the conditions $\delta S' = 0$ and $\delta S = 0$ are equivalent, and the form of the equations of motion is unchanged. Thus the Lagrangian is defined only to within an additive total time derivative of any function of co-ordinates and time.

## §3. Galileo's relativity principle

In order to consider mechanical phenomena it is necessary to choose a frame of reference. The laws of motion are in general different in form for different frames of reference. When an arbitrary frame of reference is chosen, it may happen that the laws governing even very simple phenomena become very complex. The problem naturally arises of finding a frame of reference in which the laws of mechanics take their simplest form.

If we were to choose an arbitrary frame of reference, space would be inhomogeneous and anisotropic. This means that, even if a body interacted with no other bodies, its various positions in space and its different orientations would not be mechanically equivalent. The same would in general be true of time, which would likewise be inhomogeneous; that is, different instants would not be equivalent. Such properties of space and time would evidently complicate the description of mechanical phenomena. For example, a free body (i.e. one subject to no external action) could not remain at rest: if its velocity were zero at some instant, it would begin to move in some direction at the next instant.

It is found, however, that a frame of reference can always be chosen in which space is homogeneous and isotropic and time is homogeneous. This is called an inertial frame. In particular, in such a frame a free body which is at rest at some instant remains always at rest.

We can now draw some immediate inferences concerning the form of the Lagrangian of a particle, moving freely, in an inertial frame of reference. The homogeneity of space and time implies that the Lagrangian cannot contain explicitly either the radius vector $\mathbf{r}$ of the particle or the time $t$, i.e. $L$ must be a function of the velocity $\mathbf{v}$ only. Since space is isotropic, the Lagrangian must also be independent of the direction of $\mathbf{v}$, and is therefore a function only of its magnitude, i.e. of $\mathbf{v}^2 = v^2$:
$$ L = L(v^2). $$

Since the Lagrangian is independent of $\mathbf{r}$, we have $\partial L/\partial \mathbf{r} = 0$, and so Lagrange's equation is
$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \mathbf{v}} \right) = 0, $$
whence $\partial L/\partial \mathbf{v} = \text{constant}$. Since $\partial L/\partial \mathbf{v}$ is a function of the velocity only, it follows that
$$ \mathbf{v} = \text{constant}. $$

Thus we conclude that, in an inertial frame, any free motion takes place with a velocity which is constant in both magnitude and direction. This is the law of inertia.

If we consider, besides the inertial frame, another frame moving uniformly in a straight line relative to the inertial frame, then the laws of free motion in the other frame will be the same as in the original frame: free motion takes place with a constant velocity.

Experiment shows that not only are the laws of free motion the same in the two frames, but the frames are entirely equivalent in all mechanical respects. Thus there is not one but an infinity of inertial frames moving, relative to one another, uniformly in a straight line. In all these frames the properties of space and time are the same, and the laws of mechanics are the same. This constitutes Galileo's relativity principle, one of the most important principles of mechanics.

The complete mechanical equivalence of the infinity of such frames shows also that there is no "absolute" frame of reference which should be preferred to other frames.

The co-ordinates $\mathbf{r}$ and $\mathbf{r}'$ of a given point in two different frames of reference $K$ and $K'$, of which the latter moves relative to the former with velocity $\mathbf{V}$, are related by
$$ \mathbf{r} = \mathbf{r}' + \mathbf{V}t. $$
Here it is understood that time is the same in the two frames:
$$ t = t'. $$
The assumption that time is absolute is one of the foundations of classical mechanics.

Formulae for $\mathbf{r}$ and $t$ are called a Galilean transformation. Galileo's relativity principle can be formulated as asserting the invariance of the mechanical equations of motion under any such transformation.

## §4. The Lagrangian for a free particle

Let us now go on to determine the form of the Lagrangian, and consider first of all the simplest case, that of the free motion of a particle relative to an inertial frame of reference. As we have already seen, the Lagrangian in this case can depend only on the square of the velocity. To discover the form of this dependence, we make use of Galileo's relativity principle. If an inertial frame $K$ is moving with an infinitesimal velocity $\mathbf{\epsilon}$ relative to another inertial frame $K'$, then $\mathbf{v}' = \mathbf{v} + \mathbf{\epsilon}$. Since the equations of motion must have the same form in every frame, the Lagrangian $L(v'^2)$ must be converted by this transformation into a function $L'$ which differs from $L(v^2)$, if at all, only by the total time derivative of a function of co-ordinates and time.

We have $L' = L(v'^2) = L(v^2 + 2\mathbf{v} \cdot \mathbf{\epsilon} + \epsilon^2)$. Expanding this expression in powers of $\mathbf{\epsilon}$ and neglecting terms above the first order, we obtain
$$ L(v'^2) = L(v^2) + \frac{\partial L}{\partial v^2} 2\mathbf{v} \cdot \mathbf{\epsilon}. $$

The second term on the right of this equation is a total time derivative only if it is a linear function of the velocity $\mathbf{v}$. Hence $\partial L/\partial v^2$ is independent of the velocity, i.e. the Lagrangian is in this case proportional to the square of the velocity, and we write it as
$$ L = \frac{1}{2} m v^2. $$

From the fact that a Lagrangian of this form satisfies Galileo's relativity principle for an infinitesimal relative velocity, it follows at once that the Lagrangian is invariant for a finite relative velocity $\mathbf{V}$ of the frames $K$ and $K'$. For
$$ L' = \frac{1}{2} m v'^2 = \frac{1}{2} m (\mathbf{v} + \mathbf{V})^2 = \frac{1}{2} m v^2 + m \mathbf{v} \cdot \mathbf{V} + \frac{1}{2} m V^2, $$
or
$$ L' = L + \frac{d}{dt} \left( m \mathbf{r} \cdot \mathbf{V} + \frac{1}{2} m V^2 t \right). $$
The second term is a total time derivative and may be omitted.

The quantity $m$ which appears in the Lagrangian for a freely moving particle is called the mass of the particle. The additive property of the Lagrangian shows that for a system of particles which do not interact we have
$$ L = \sum_a \frac{1}{2} m_a v_a^2. $$

It should be emphasised that the above definition of mass becomes meaningful only when the additive property is taken into account. As has been mentioned in §2, the Lagrangian can always be multiplied by any constant without affecting the equations of motion. As regards the function above, such multiplication amounts to a change in the unit of mass; the ratios of the masses of different particles remain unchanged thereby, and it is only these ratios which are physically meaningful.

It is easy to see that the mass of a particle cannot be negative. For, according to the principle of least action, the integral
$$ S = \int_{t_1}^{t_2} \frac{1}{2} m v^2 dt $$
has a minimum for the actual motion of the particle in space from point 1 to point 2. If the mass were negative, the action integral would take arbitrarily large negative values for a motion in which the particle rapidly left point 1 and rapidly approached point 2, and there would be no minimum.

It is useful to notice that
$$ v^2 = (dl/dt)^2 = (dl)^2 / (dt)^2. $$
Hence, to obtain the Lagrangian, it is sufficient to find the square of the element of arc $dl$ in a given system of co-ordinates. In Cartesian co-ordinates, for example, $dl^2 = dx^2 + dy^2 + dz^2$, and so
$$ L = \frac{1}{2} m (\dot{x}^2 + \dot{y}^2 + \dot{z}^2). $$

In cylindrical co-ordinates $dl^2 = dr^2 + r^2 d\phi^2 + dz^2$, whence
$$ L = \frac{1}{2} m (\dot{r}^2 + r^2 \dot{\phi}^2 + \dot{z}^2). $$

In spherical co-ordinates $dl^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2$, and
$$ L = \frac{1}{2} m (\dot{r}^2 + r^2 \dot{\theta}^2 + r^2 \dot{\phi}^2 \sin^2\theta). $$

## §5. The Lagrangian for a system of particles

Let us now consider a system of particles which interact with one another but with no other bodies. This is called a closed system. It is found that the interaction between the particles can be described by adding to the Lagrangian for non-interacting particles a certain function of the co-ordinates, which depends on the nature of the interaction. Denoting this function by $-U$, we have
$$ L = \sum_a \frac{1}{2} m_a v_a^2 - U(\mathbf{r}_1, \mathbf{r}_2, \dots), $$
where $\mathbf{r}_a$ is the radius vector of the $a$-th particle. This is the general form of the Lagrangian for a closed system. The sum $T = \sum_a \frac{1}{2} m_a v_a^2$ is called the kinetic energy, and $U$ the potential energy, of the system. The significance of these names is explained in §6.

The fact that the potential energy depends only on the positions of the particles at a given instant shows that a change in the position of any particle instantaneously affects all the other particles. We may say that the interactions are instantaneously propagated. The necessity for interactions in classical mechanics to be of this type is closely related to the premises upon which the subject is based, namely the absolute nature of time and Galileo's relativity principle. If the propagation of interactions were not instantaneous, but took place with a finite velocity, then that velocity would be different in different frames of reference in relative motion, since the absoluteness of time necessarily implies that the ordinary law of composition of velocities is applicable to all phenomena. The laws of motion for interacting bodies would then be different in different inertial frames, a result which would contradict the relativity principle.

In §3 only the homogeneity of time has been spoken of. The form of the Lagrangian shows that time is both homogeneous and isotropic, i.e. its properties are the same in both directions. For, if $t$ is replaced by $-t$, the Lagrangian is unchanged, and therefore so are the equations of motion. In other words, if a given motion is possible in a system, then so is the reverse motion (that is, the motion in which the system passes through the same states in the reverse order). In this sense all motions which obey the laws of classical mechanics are reversible.

Knowing the Lagrangian, we can derive the equations of motion:
$$ \frac{d}{dt} \left( \frac{\partial L}{\partial \mathbf{v}_a} \right) = \frac{\partial L}{\partial \mathbf{r}_a}. $$
Substitution of $L$ gives
$$ m_a \frac{d\mathbf{v}_a}{dt} = -\frac{\partial U}{\partial \mathbf{r}_a}. $$

In this form the equations of motion are called Newton's equations and form the basis of the mechanics of a system of interacting particles. The vector
$$ \mathbf{F}_a = -\frac{\partial U}{\partial \mathbf{r}_a} $$
which appears on the right-hand side of the equation is called the force on the $a$-th particle. Like $U$, it depends only on the co-ordinates of the particles, and not on their velocities. The equation therefore shows that the acceleration vectors of the particles are likewise functions of their co-ordinates only.

The potential energy is defined only to within an additive constant, which has no effect on the equations of motion. This is a particular case of the nonuniqueness of the Lagrangian discussed at the end of §2. The most natural and most usual way of choosing this constant is such that the potential energy tends to zero as the distances between the particles tend to infinity.

If we use, to describe the motion, arbitrary generalised co-ordinates $q_i$ instead of Cartesian co-ordinates, the following transformation is needed to obtain the new Lagrangian:
$$ x_a = f_a(q_1, q_2, \dots, q_s), \quad \dot{x}_a = \sum_k \frac{\partial f_a}{\partial q_k} \dot{q}_k, \quad \text{etc.} $$
Substituting these expressions in the function $L = \sum_a \frac{1}{2} m_a (\dot{x}_a^2 + \dot{y}_a^2 + \dot{z}_a^2) - U$, we obtain the required Lagrangian in the form
$$ L = \frac{1}{2} \sum_{i,k} a_{ik}(q) \dot{q}_i \dot{q}_k - U(q), $$
where the $a_{ik}$ are functions of the co-ordinates only. The kinetic energy in generalised co-ordinates is still a quadratic function of the velocities, but it may depend on the co-ordinates also.

Hitherto we have spoken only of closed systems. Let us now consider a system A which is not closed and interacts with another system B executing a given motion. In such a case we say that the system A moves in a given external field (due to the system B). Since the equations of motion are obtained from the principle of least action by independently varying each of the coordinates (i.e. by proceeding as if the remainder were given quantities), we can find the Lagrangian $L_A$ of the system A by using the Lagrangian $L$ of the whole system A + B and replacing the co-ordinates $q_B$ therein by given functions of time.

Assuming that the system A + B is closed, we have $L = T_A(q_A, \dot{q}_A) + T_B(q_B, \dot{q}_B) - U(q_A, q_B)$, where the first two terms are the kinetic energies of the systems A and B and the third term is their combined potential energy. Substituting for $q_B$ the given functions of time and omitting the term $T_B[q_B(t), \dot{q}_B(t)]$ which depends on time only, and is therefore the total time derivative of a function of time, we obtain $L_A = T_A(q_A, \dot{q}_A) - U[q_A, q_B(t)]$. Thus the motion of a system in an external field is described by a Lagrangian of the usual type, the only difference being that the potential energy may depend explicitly on time.

For example, when a single particle moves in an external field, the general form of the Lagrangian is
$$ L = \frac{1}{2} m \mathbf{v}^2 - U(\mathbf{r}, t), $$
and the equation of motion is
$$ m \dot{\mathbf{v}} = -\frac{\partial U}{\partial \mathbf{r}}. $$

A field such that the same force $\mathbf{F}$ acts on a particle at any point in the field is said to be uniform. The potential energy in such a field is evidently
$$ U = -\mathbf{F} \cdot \mathbf{r}. $$

To conclude this section, we may make the following remarks concerning the application of Lagrange's equations to various problems. It is often necessary to deal with mechanical systems in which the interaction between different bodies (or particles) takes the form of constraints, i.e. restrictions on their relative position. In practice, such constraints are effected by means of rods, strings, hinges and so on. This introduces a new factor into the problem, in that the motion of the bodies results in friction at their points of contact, and the problem in general ceases to be one of pure mechanics. In many cases, however, the friction in the system is so slight that its effect on the motion is entirely negligible. If the masses of the constraining elements of the system are also negligible, the effect of the constraints is simply to reduce the number of degrees of freedom $s$ of the system to a value less than $3N$. To determine the motion of the system, the Lagrangian can again be used, with a set of independent generalised co-ordinates equal in number to the actual degrees of freedom.

## PROBLEMS

Find the Lagrangian for each of the following systems when placed in a uniform gravitational field (acceleration $g$).

**PROBLEM 1.** A coplanar double pendulum.

**SOLUTION.** We take as co-ordinates the angles $\phi_1$ and $\phi_2$ which the strings $l_1$ and $l_2$ make with the vertical. Then we have, for the particle $m_1$, $T_1 = \frac{1}{2} m_1 l_1^2 \dot{\phi}_1^2$, $U_1 = -m_1 g l_1 \cos \phi_1$. In order to find the kinetic energy of the second particle, we express its Cartesian co-ordinates $x_2, y_2$ (with the origin at the point of support and the $y$-axis vertically downwards) in terms of the angles $\phi_1$ and $\phi_2$: $x_2 = l_1 \sin \phi_1 + l_2 \sin \phi_2$, $y_2 = l_1 \cos \phi_1 + l_2 \cos \phi_2$. Then we find
$$ T_2 = \frac{1}{2} m_2 (\dot{x}_2^2 + \dot{y}_2^2) = \frac{1}{2} m_2 [ l_1^2 \dot{\phi}_1^2 + l_2^2 \dot{\phi}_2^2 + 2 l_1 l_2 \dot{\phi}_1 \dot{\phi}_2 \cos(\phi_1 - \phi_2) ]. $$
Finally,
$$ L = \frac{1}{2}(m_1 + m_2)l_1^2 \dot{\phi}_1^2 + \frac{1}{2} m_2 l_2^2 \dot{\phi}_2^2 + m_2 l_1 l_2 \dot{\phi}_1 \dot{\phi}_2 \cos(\phi_1 - \phi_2) + (m_1 + m_2)g l_1 \cos \phi_1 + m_2 g l_2 \cos \phi_2. $$

**PROBLEM 2.** A simple pendulum of mass $m_2$, with a mass $m_1$ at the point of support which can move on a horizontal line lying in the plane in which $m_2$ moves.

**SOLUTION.** Using the co-ordinate $x$ of $m_1$ and the angle $\phi$ between the string and the vertical, we have
$$ L = \frac{1}{2}(m_1 + m_2)\dot{x}^2 + \frac{1}{2} m_2 (l^2 \dot{\phi}^2 + 2l \dot{x} \dot{\phi} \cos \phi) + m_2 g l \cos \phi. $$

**PROBLEM 3.** A simple pendulum of mass $m$ whose point of support (a) moves uniformly on a vertical circle with constant frequency $\gamma$, (b) oscillates horizontally in the plane of motion of the pendulum according to the law $x = a \cos \gamma t$, (c) oscillates vertically according to the law $y = a \cos \gamma t$.

**SOLUTION.** 
(a) The co-ordinates of $m$ are $x = a \cos \gamma t + l \sin \phi$, $y = -a \sin \gamma t + l \cos \phi$. The Lagrangian is
$$ L = \frac{1}{2} m l^2 \dot{\phi}^2 + m l a \gamma^2 \sin(\phi - \gamma t) + m g l \cos \phi; $$
here terms depending only on time have been omitted, together with the total time derivative of $m l a \gamma \cos(\phi - \gamma t)$.

(b) The co-ordinates of $m$ are $x = a \cos \gamma t + l \sin \phi$, $y = l \cos \phi$. The Lagrangian is (omitting total derivatives)
$$ L = \frac{1}{2} m l^2 \dot{\phi}^2 + m l a \gamma^2 \cos \gamma t \sin \phi + m g l \cos \phi. $$

(c) Similarly,
$$ L = \frac{1}{2} m l^2 \dot{\phi}^2 + m l a \gamma^2 \cos \gamma t \cos \phi + m g l \cos \phi. $$

**PROBLEM 4.** The system shown in Fig. 4. The particle $m_1$ moves on a vertical axis and the whole system rotates about this axis with a constant angular velocity $\Omega$.

**SOLUTION.** Let $\theta$ be the angle between one of the segments $a$ and the vertical, and $\phi$ the angle of rotation of the system about the axis; $\dot{\phi} = \Omega$. For each particle $m_2$, the infinitesimal displacement is given by $dl_2^2 = a^2 d\theta^2 + a^2 \sin^2 \theta d\phi^2$. The distance of $m_1$ from the point of support A is $2a \cos \theta$, and so $dl_1 = -2a \sin \theta d\theta$. The Lagrangian is
$$ L = m_2 a^2 (\dot{\theta}^2 + \Omega^2 \sin^2 \theta) + 2 m_1 a^2 \dot{\theta}^2 \sin^2 \theta + 2(m_1 + m_2)g a \cos \theta. $$
"""
with open("/home/igorkan/repos/phyc54h3/extra/landau-chapter-1.qmd", "w") as f:
    f.write(content)
