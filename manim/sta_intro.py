"""STA1 homepage intro: symbol field plus a data-to-model loop.

Light and dark variants share duration, motion, and beats. Only colours
and background differ.
"""

from __future__ import annotations

import random

import numpy as np
from manim import *

DURATION = 20.0

STA_SYMBOLS = [
    r"\bar{x}",
    r"s^{2}",
    r"\mu",
    r"\sigma",
    r"H_{0}",
    r"H_{1}",
    r"p",
    r"\alpha",
    r"\chi^{2}",
    r"F",
    r"t",
    r"R^{2}",
    r"\hat{y}=\beta_{0}+\beta_{1}x",
    r"\mathrm{CI}",
    r"\mathrm{SE}",
    r"N(\mu,\sigma^{2})",
    r"\text{ANOVA}",
    r"\text{Binomial}",
    r"\text{Poisson}",
    r"\text{STA1}",
    r"\text{VIA}",
]


def _symbol_rain(colors: list[str], n: int = 48) -> VGroup:
    drops = VGroup()
    y_top, y_bot = 4.2, -4.2
    for _ in range(n):
        mob = MathTex(random.choice(STA_SYMBOLS), color=random.choice(colors))
        mob.scale(random.uniform(0.28, 0.42))
        mob.move_to([random.uniform(-6.8, 6.8), random.uniform(y_bot, y_top), 0])
        mob.speed = random.uniform(0.35, 0.7)
        drops.add(mob)

    def update(group, dt):
        for m in group:
            m.shift(DOWN * m.speed * dt)
            if m.get_y() < y_bot:
                m.set_y(y_top)
                m.set_x(random.uniform(-6.8, 6.8))
            m.set_opacity(0.12 + 0.18 * (0.5 + 0.5 * np.sin(m.get_y())))

    drops.add_updater(update)
    return drops


def _points(rng: np.random.Generator, n: int = 36) -> np.ndarray:
    x = rng.uniform(-3.2, 3.2, size=n)
    y = 0.45 * x + rng.normal(0, 0.55, size=n)
    return np.column_stack([x, y])


def build_scene(background: str, glyph_colors: list[str], accent: str, ink: str):
    class StatsIntro(Scene):
        def construct(self):
            self.camera.background_color = background
            rng = np.random.default_rng(26)
            rain = _symbol_rain(glyph_colors)
            self.add(rain)

            pts = _points(rng)
            dots = VGroup(
                *[
                    Dot(point=[p[0], p[1] + 0.3, 0], radius=0.055, color=accent)
                    for p in pts
                ]
            )
            self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 0.4) for d in dots], lag_ratio=0.04), run_time=3.2)

            # Histogram along the lower half
            xs = pts[:, 0]
            bins = np.linspace(-3.4, 3.4, 9)
            counts, edges = np.histogram(xs, bins=bins)
            counts = counts / counts.max()
            bars = VGroup()
            for c, left, right in zip(counts, edges[:-1], edges[1:]):
                h = 1.6 * c
                rect = Rectangle(
                    width=right - left - 0.04,
                    height=max(h, 0.02),
                    fill_color=accent,
                    fill_opacity=0.85,
                    stroke_width=0,
                )
                rect.move_to([(left + right) / 2, -2.4 + h / 2, 0])
                bars.add(rect)

            self.play(
                dots.animate.set_opacity(0.25).shift(DOWN * 1.8 + LEFT * 0.0),
                FadeIn(bars, shift=UP * 0.2),
                run_time=3.0,
            )

            mu, sd = float(xs.mean()), float(xs.std())
            curve = FunctionGraph(
                lambda t: -2.4 + 1.55 * np.exp(-0.5 * ((t - mu) / (sd + 1e-6)) ** 2),
                x_range=[-3.4, 3.4, 0.05],
                color=ink,
                stroke_width=4,
            )
            self.play(Create(curve), run_time=2.4)
            self.wait(1.2)

            self.play(FadeOut(bars), FadeOut(curve), dots.animate.set_opacity(1).shift(UP * 1.8), run_time=2.2)

            # Regression line on the cloud
            x = pts[:, 0]
            y = pts[:, 1]
            beta1 = np.cov(x, y, ddof=1)[0, 1] / np.var(x, ddof=1)
            beta0 = y.mean() - beta1 * x.mean()
            line = Line(
                start=[-3.3, beta0 + beta1 * (-3.3) + 0.3, 0],
                end=[3.3, beta0 + beta1 * 3.3 + 0.3, 0],
                color=ink,
                stroke_width=5,
            )
            self.play(Create(line), run_time=2.0)
            self.wait(2.0)
            self.play(FadeOut(line), FadeOut(dots), run_time=1.6)
            self.wait(max(0.1, DURATION - 17.8))

    StatsIntro.__name__ = "StatsIntro"
    return StatsIntro


StatsIntroLight = build_scene(
    background="#FFFFFF",
    glyph_colors=["#363636", "#6CA2C6", "#C0D4F0"],
    accent="#6CA2C6",
    ink="#363636",
)
StatsIntroLight.__name__ = "StatsIntroLight"

StatsIntroDark = build_scene(
    background="#0d1017",
    glyph_colors=["#C0D4F0", "#2A9DF4", "#88A1C9"],
    accent="#2A9DF4",
    ink="#C0D4F0",
)
StatsIntroDark.__name__ = "StatsIntroDark"
