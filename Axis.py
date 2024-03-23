from manim import *

class QuarterCircleExample(Scene):
    def construct(self):
        # Define the radius and angle of the quarter circle
        radius = 1
        start_angle = 0
        end_angle = PI / 2  # Quarter of a full circle

        # Create the outline of the quarter circle
        outline = Arc(radius=radius, start_angle=start_angle, angle=end_angle)

        # Create the filled square portion of the quarter circle
        square_fill = Polygon(
            outline.points[1],  # Start point (bottom left)
            outline.points[1],  # Second point (bottom right)
            outline.points[1],  # Third point (top right)
            outline.points[1] + radius * UP,  # Fourth point (top left)
            fill_color=BLUE,
            fill_opacity=1,
            stroke_width=0  # No outline
        )
        Q1 = VGroup(outline, square_fill)
        # Display the quarter circle with square fill
        self.play(Create(outline), Create(square_fill))
        self.wait(2)
