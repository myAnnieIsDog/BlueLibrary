"""
National Design Specification
"""

from dataclasses import dataclass
import datetime
from pprint import pprint, pformat
import time


def run():
    beam1 = Beam()
    print(beam1.M)


@dataclass
class Beam:
    span_ft = 16  # feet
    depth = 12  # inches
    width = 5.5  # inches
    species = "DFL"  # Douglas Fir-Larch
    grade = "Structural Select"  # Structural Select
    E = 1_300_000  # psi

    def calc_properties(self):
        self.area = self.width * self.depth  # in**2
        self.S = self.width * self.depth**2 / 6  # in**3
        self.I = self.width * self.depth**3 / 12  # in**4
        self.EI = self.E * I  # in**2-lb

    def calc_reactions(self, uniform_loads, point_loads):
        """Update this function to work for various beam types and load combinations."""
        self.R = uniform_loads * self.span_ft / 2
        self.V = uniform_loads * self.span_ft / 2
        self.M = uniform_loads * self.span_ft**2 / 8  # in-lbs
        self.D = uniform_loads * self.span_ft**4 * 5 / (384 * self.EI)


@dataclass
class UniformLoad:
    """A basic unit of distributed load."""

    type: str = "Dead"
    load: float  # psf
    start: float = 0  # % of length
    end: float = 100  # % of length


@dataclass
class PointLoad:
    type: str = "Dead"
    load: float  # lb
    loc: float = 50  # % of length


if __name__ == "__main__":
    run()
