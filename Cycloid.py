#Cycloid
from manim import *


class Cycloid(Scene):

    def construct(self):

        CycloidTxt = Text("Cycloid", font="TeX Gyre Termes").scale(1.5).to_edge(UP)

        r = 3 / PI
        corr = 1 / config.frame_rate  # missed frame correction

        BL = NumberLine().shift(DOWN * r * 2)  # Base Line

        C = Circle(r, color="#F72119").next_to(BL.n2p(-6), UP, buff=0)
        DL = DashedLine(C.get_center(), C.get_top(), color="#A5ADAD")
        CP = Dot(DL.get_start(), color="#ff3503")  # Center Point
        TP = Dot(DL.get_end(), color="#00EAFF").scale(1.2)  # Tracing Point

        RC = VGroup(C, DL, CP, TP)  # Rolling Circle

        self.dir = 1  # direction of motion

        def Rolling(m, dt):  # update_function
            theta = self.dir * -PI
            m.rotate(dt * theta, about_point=m[0].get_center()).shift(dt * LEFT * theta * r)

        Cycloid = TracedPath(TP.get_center, stroke_width=6.5, stroke_color="#4AF1F2")

        self.add(CycloidTxt, BL, Cycloid, RC)

        RC.add_updater(Rolling)
        self.wait(4 + corr)

        RC.suspend_updating(Rolling)
        Cycloid.clear_updaters()

        self.wait()
        self.dir = -1  # direction change, rolling back

        RC.resume_updating(Rolling)
        self.play(Uncreate(Cycloid, rate_func=lambda t: linear(1 - t), run_time=4 + corr))
            
        RC.clear_updaters()
        self.wait()
