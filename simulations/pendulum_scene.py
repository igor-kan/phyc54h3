from manim import *
import numpy as np

class DoublePendulumScene(Scene):
    def construct(self):
        title = Text("PHYC54: Double Pendulum Chaos", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))

        # Pivot point
        pivot = Dot(ORIGIN, color=WHITE)
        self.add(pivot)

        # Pendulum parameters
        l1 = 2.0
        l2 = 1.8

        theta1 = ValueTracker(PI / 2)
        theta2 = ValueTracker(PI / 2)

        # Dynamic rods and bobs
        def get_bob1_pos():
            th1 = theta1.get_value()
            return ORIGIN + np.array([l1 * np.sin(th1), -l1 * np.cos(th1), 0])

        def get_bob2_pos():
            th2 = theta2.get_value()
            return get_bob1_pos() + np.array([l2 * np.sin(th2), -l2 * np.cos(th2), 0])

        rod1 = always_redraw(lambda: Line(ORIGIN, get_bob1_pos(), color=GRAY, stroke_width=3))
        rod2 = always_redraw(lambda: Line(get_bob1_pos(), get_bob2_pos(), color=GRAY, stroke_width=3))

        bob1 = always_redraw(lambda: Dot(get_bob1_pos(), radius=0.15, color=BLUE))
        bob2 = always_redraw(lambda: Dot(get_bob2_pos(), radius=0.15, color=RED))

        # Trace path of bob 2
        trace = TracedPath(bob2.get_center, stroke_color=RED, stroke_width=2, stroke_opacity=0.8)

        self.add(rod1, rod2, bob1, bob2, trace)

        # Animate simple oscillation
        self.play(
            theta1.animate.set_value(-PI / 3),
            theta2.animate.set_value(PI / 4),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)
