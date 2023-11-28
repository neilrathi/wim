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
        arc2center = Dot([3, -2, 0])

        self.play(Create(base))
        self.play(Create(Dot([-1, -2, 0])))
        self.play(Create(a))
        self.wait(0.5)
        self.play(Create(Dot([2, -2, 0])))
        self.play(Create(arc1))
        self.play(Create(arc2center))
        self.play(Create(arc2))
        self.wait(0.5)
        self.play(Create(ab))

        self.play(FadeOut(arc1, arc2, arc2center))

        self.play(Create(hyp))
        self.wait(1)
        self.play(Create(alpha1))
        self.play(Create(alpha2))
        self.wait(3)

class SquareRoot(Scene):
    def construct(self):
        unit = Line([-2.5, -0.75, 0], [-2, -0.75, 0])
        a = Line([-2, -0.75, 0], [2.5, -0.75, 0])
        sqrta = Line([-2, -0.75, 0], [-2, 0.75, 0])
        l1 = Line([-2.5, -0.75, 0], [-2, 0.75, 0])
        l2 = Line([2.5, -0.75, 0], [-2, 0.75, 0])

        midline = Line([0, -3.25, 0], [0, 2.5, 0])

        midpoint = Dot([0, -0.75, 0])

        arc1 = Arc(arc_center=[-2.5, -0.75, 0], start_angle=PI/3, angle=-2*PI/3, radius = 3.0)
        arc2 = Arc(arc_center=[2.5, -0.75, 0], start_angle=2*PI/3, angle=2*PI/3, radius = 3.0)

        circle = Arc(arc_center=[0, -0.75, 0], angle=PI, radius=2.5)

        self.play(Create(unit))
        self.play(Create(Dot([-2, -0.75, 0])))
        self.play(Create(a))
        self.wait(0.5)
        self.play(Create(arc1))
        self.play(Create(arc2))

        self.play(Create(midline))
        self.play(Create(midpoint))

        self.play(FadeOut(midline, arc1, arc2))

        self.play(Create(circle))
        self.play(FadeOut(midpoint))
        self.play(Create(sqrta))
        self.play(Create(Dot([-2, 0.75, 0])))

        self.play(Create(l1))
        self.play(Create(l2))
        self.wait(3)


class GenerateCartesian(Scene):
    def construct(self):
        unit = Line([0, 0, 0], [1, 0, 0])

        x1 = Dot([1, 0, 0])
        x2 = Dot([2, 0, 0])
        x3 = Dot([3, 0, 0])

        number_plane = NumberPlane(
            x_range=(- 7.111111111111111, 7.111111111111111, 1),
            y_range=(- 4.0, 4.0, 1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        self.play(Create(Dot([0, 0, 0])))
        self.play(Create(unit))
        self.play(Create(x1))
        self.play(Transform(unit, Line([1, 0, 0], [2, 0, 0])))
        self.play(Create(x2))
        self.play(Transform(unit, Line([2, 0, 0], [3, 0, 0])))
        self.play(Create(x3))
        self.wait(0.5)
        x = VGroup()
        for i in range(0,9):
            x.add(Dot())
        x.arrange_in_grid(rows = 1, buff = 0.85)
        self.play(Create(x), FadeOut(unit))
        self.wait(1)
        xydots = VGroup()
        for i in range(0,63):
            xydots.add(Dot())
        xydots.arrange_in_grid(rows = 7, buff = 0.85)
        self.play(Transform(x, xydots))
        self.wait(1)
        self.play(Create(number_plane), FadeOut(x, x1, x2, x3))
        self.wait(3)

# class DrawLine(Scene):
#     def construct(self):
#         self.add(Dot([-2, -1, 0]), Dot([2, 1, 0]))
#         self.wait(1)
#         self.play(Create(Line([-2, -1, 0], [2, 1, 0])))
#         self.wait(3)

# class DrawCircle(Scene):
#     def construct(self):
#         self.add(Dot([0, 0, 0]), Dot([3, 0, 0]))
#         self.wait(1)
#         self.play(Create(Arc(arc_center=[0, 0, 0], radius=3, start_angle = 0, angle = 2 * PI)))
#         self.wait(3)

class LineIntersection(Scene):
    def construct(self):
        self.add(Line([-10, -9, 0], [10, 9, 0], color=TEAL_C), Line([-9, 10, 0], [9, -10, 0], color=GREEN_C))
        self.play(Create(Dot([0,0,0], radius = 0.1)))
        self.wait(3)

class CircleIntersection(Scene):
    def construct(self):
        c1 = Dot([0.5, 0.5, 0], color=TEAL_C)
        c2 = Dot([-1, -1, 0], color=GREEN_C)

        self.add(c1,
            c2,
            Circle(arc_center = [0.5, 0.5, 0], radius = 2, color=TEAL_C),
            Circle(arc_center = [-1, -1, 0], radius = 1.5, color=GREEN_C))
        self.play(Create(Dot([-1.4982, 0.4149, 0], radius = 0.1)), Create(Dot([0.4149, -1.4982, 0], radius = 0.1)))
        self.wait(3)

class CircleLine(Scene):
    def construct(self):
        c = Dot([0, 0, 0], color=TEAL_C)

        self.add(c,
            Circle(arc_center = [0, 0, 0], radius = 1.5, color=TEAL_C),
            Line([12.5, 14, 0], [-14.5, -13, 0], color = GREEN_C))
        self.play(Create(Dot([-1.5, 0, 0], radius = 0.1)), Create(Dot([0, 1.5, 0], radius = 0.1)))
        self.wait(3)

class CosineFromAngle(Scene):
    def construct(self):
        l1 = Line([-2, -1.73205081, 0], [2, -1.73205081, 0])
        l2 = Line([-2, -1.73205081, 0], [0, 1.73205081, 0])
        a = Angle(l1, l2, radius = 1)

        drop = Line([0, 1.73205081, 0], [0, -1.73205081, 0])
        dot1 = Dot([0, 1.73205081, 0])
        dot = Dot([0, -1.73205081, 0])

        self.add(a,
            l1,
            l2)

        self.play(Create(dot1))
        self.play(Create(drop))
        self.play(Create(dot), Create(RightAngle(l1, drop, length=0.5, quadrant=(-1,-1))))

        self.wait(3)

class AngleFromCosine(Scene):
    def construct(self):
        l1 = Line([-2, -1.73205081, 0], [2, -1.73205081, 0])
        l2 = Line([-2, -1.73205081, 0], [0.5, 2.59807621135, 0])
        a = Angle(l1, l2, radius = 1)

        drop = Line([0, -1.73205081, 0], [0, 3, 0])
        c = Dot([-2, -1.73205081, 0])
        dot = Dot([0, -1.73205081, 0])
        dot2 = Dot([0, 1.73205081, 0])
        ra = RightAngle(l1, drop, length=0.33, quadrant=(-1,1))

        circ = Arc(arc_center=[-2, -1.73205081, 0], angle= 2 * (PI / 3) - 0.1, radius=4)

        self.add(c, dot, l1)

        self.play(Create(drop), Create(ra))
        self.play(Create(circ))
        self.play(Create(l2))
        self.play(Create(dot2))
        self.play(Create(a))

        self.wait(3)

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