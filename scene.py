from manim import *

class Multiplication(Scene):
    def construct(self):
        base = Line([-4, -2, 0], [4, -2, 0])
        a = Line([-1, -2, 0], [0, -0.267949192431, 0])
        ab = Line([2, -2, 0], [4, 1.46410162, 0])
        hyp = Line([-4, -2, 0], [4.05, 1.46410162, 0])

        alpha1 = Arc(arc_center=[-1, -2, 0], start_angle=PI, angle=-2.0943951, radius=0.50)
        alpha2 = Arc(arc_center=[2, -2, 0], start_angle=PI, angle=-2.0943951, radius=0.50)

        arc1 = Arc(arc_center=[2, -2, 0], start_angle=PI/2+0.1, angle=-PI/2-0.4, radius=1)
        arc2 = Arc(arc_center=[3, -2, 0], start_angle=PI/2-0.1, angle=PI/3, radius=1)

        self.play(Create(base))
        self.play(Create(a))
        self.wait(0.5)
        self.play(Create(arc1))
        self.wait(0.5)
        self.play(Create(arc2))
        self.wait(0.5)
        self.play(Create(ab))
        self.wait(1)

        self.play(FadeOut(arc1))
        self.play(FadeOut(arc2))

        self.play(Create(alpha1))
        self.play(Create(alpha2))
        self.play(Create(hyp))

# class SquareToCircle(Scene):
#     def construct(self):
#         ax = Axes(
#             tips=False
#         )
#         number_plane = NumberPlane(
#             background_line_style={
#                 "stroke_color": TEAL,
#                 "stroke_width": 4,
#                 "stroke_opacity": 0.6
#             }
#         )
#         self.play(Create(ax))
#         self.wait(3)
#         self.play(Create(number_plane))
#         self.wait(5)