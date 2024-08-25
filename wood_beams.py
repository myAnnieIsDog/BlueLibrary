""" Lumber Design per National Design Specification """

from dataclasses import dataclass


def run():
    geo = LumberGeometry(span=16 * 12, depth=12, width=5.5)
    mat = Material()  # Defaults to properties for 4"x__" DFL No. 2
    load1 = PointLoad("Dead", unit_load=40, area=400)
    load2 = DistLoad(unit_load=40, width=12)
    reactions = Reactions(geo, mat, load1, load2)
    print(beam1.E(), beam1.EI())


@dataclass
class Material:
    category: str = 'Visually Graded Dimension Lumber (2"-4" thick)'
    species: str = "DFL"
    grade: str = "No. 2"
    Fb: float = 900  # Bending
    Ft: float = 575  # Tension
    Fv: float = 180  # Shear
    Fcp: float = 625  # Bearing
    Fc: float = 1_350  # Compression
    E: float = 1_600_000  # Modulus of Elasticity (Deflection)
    Emin: float = 580_000  # Minimum E
    G: float = 0.50  # Specific Gravity; unit weight = x * 62.4 lb/ft3
    Agency: str = "PLIB WWPA"
    CD: float = 1.0  # Load Duration (ASD)
    CM: bool = True  # Wet Service
    Ct: bool = False  # Temperature
    CL: bool = False  # Beam Stability
    CF: float = 1.0  # Size
    Cfu: bool = False  # Flat Use
    Ci: bool = False  # Incising (Pressure Treated)
    Cr: bool = False  # True -> 1.15
    CP: bool = False  # Column Stability
    CT: bool = False  # Bearing Area
    KF: float = False  # LRFD Format Conversion
    phi: float = False  # LRFD Resistance
    lamb: float = False  # Time Effect


@dataclass
class LumberGeometry:
    span: float  # feet --> inches
    nom_depth: float  # nominal inches
    nom_width: float  # nominal inches
    lat_restrained = False
    start_restrained = False
    end_restrained = False

    def depth(self) -> float:
        if self.depth >= 11:
            return self.depth - 0.75
        return self.depth - 0.5

    def width(self) -> float:
        if self.depth >= 11:
            return self.depth - 0.75
        return self.depth - 0.5

    def area(self) -> float:  # in**2
        return self.width * self.depth

    def S(self) -> float:  # in**3
        return self.width * self.depth**2 / 6

    def I(self) -> float:  # in**4
        return self.width * self.depth**3 / 12


@dataclass
class PointLoad:
    type: str  # Dead, Live, Roof, Seismic, Wind, etc.
    unit_load: float = 0  # lb per square foot
    area: float = 0  # tributary area
    load_p: float = 0  # lbs
    load_x: float = 0

    def load_ft(self):
        x = self.load_x
        a = self.load_p
        if a:
            return (a, x)
        b = self.unit_load * self.area
        if b:
            return (b, x)
        raise ValueError(
            "PointLoad.load() must have arguments for 'load_x' and either 'load_p' or 'unit_load' and 'area'."
        )


@dataclass
class DistLoad:
    type: str  # Dead, Live, Roof, Seismic, Wind, etc.
    unit_load: float = 0  # lb per square foot
    width: float = 0  # tributary width
    load_c: float = 0
    load_x: float = 0
    load_x2: str = 0
    load_x3: str = 0
    start: float = 0  # starts at x
    end: float = 0  # ends at x

    def load_ft(self, x) -> float:
        if x < self.start or x > self.end:
            return 0
        a = self.unit_load * self.width
        if a:
            return a
        b = (
            self.load_c
            + self.load_x * x
            + self.load_x2 * (x**2)
            + self.load_x2 * (x**3)
        )
        if b:
            return b
        raise ValueError(
            "DistLoad.load() must have arguments for 'load_c', 'load_x', 'load_x2', 'load_x3', or both 'unit_load' and 'width'."
        )


"""
class CombinedLoads():

    self.uniform = 200 / 12  # pounds per foot --> inch
    self.R = self.uniform * self.span / 2
    self.V = self.uniform * self.span / 2
    self.M = self.uniform * self.span**2 / 8 # in-lbs
    self.D = self.uniform * self.span**4 * 5 / (384 * self.EI)

"""

def Reactions(span, *loads):
    Dx = span / 100 # Divide the span into 100 segments.
    Fx, Fg, M0 = 0, 0, 0
    Fs, Vx, Mx = [], [], []

    # This math is wrong because Eliza was distracting me.
    for load in loads:
        for i in range(100):
            Fx = load.load_ft(Dx * (i + 0.5 )) * Dx
            Fg += Fx
            M0 += Fx * (Dx * i)
            Fs.append(Fg)
            for i in Fs:
                V = i * Dx
            Vx.append(V)
    
    R100 = M0 / span
    R0 = Fg - R100
    moment_0 = (
        for load in loads:
            
    )
        

    

@dataclass
class Beam:


    def EI(self) -> float:  # in**2-lb
        return self.E * self.I


if __name__ == "__main__":
    run()
