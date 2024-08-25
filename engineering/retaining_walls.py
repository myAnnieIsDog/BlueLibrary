"""
CA Building Code 1610.1 Lateral Pressures and 
CAvBuilding Code 1807.2 Retaining Walls

Retaining walls shall be designed to ensure stability against
    overturning, 
    sliding, 
    excessive foundation pressure, and 
    water uplift. 

For structures assigned to Seismic Design Category D, E, or F, the design of retaining walls supporting more than 6 feet of backfill height shall incorporate the additional seismic lateral earth pressure in accordance with the geotechnical investigation where required in Section 1803.2.

SOIL LATERAL LOAD:
Design lateral soil loads are given for moist conditions for the specified soils at their optimum densities. Actual field conditions shall govern. Submerged or saturated soil pressures shall include the weight of the buoyant soil plus the hydrostatic loads.

Foundation walls extending not more than 8 feet (2438 mm) below grade and laterally supported at the top by flexible diaphragms shall be permitted to be designed for active pressure.

Foundation walls and retaining walls shall be designed to resist lateral soil loads from adjacent soil. Soil loads specified in Table 1610.1 shall be used as the minimum design lateral soil loads unless determined otherwise by a geotechnical investigation in accordance with Section 1803. 

Foundation walls and other walls in which horizontal movement is restricted at the top shall be designed for at-rest pressure. 

Retaining walls free to move and rotate at the top shall be permitted to be designed for active pressure. 

Lateral pressure from surcharge loads shall be added to the lateral soil load. 

Lateral pressure shall be increased if expansive soils are present at the site. 

Foundation walls shall be designed to support the weight of the full hydrostatic pressure of undrained backfill unless a drainage system is installed in accordance with Sections 1805.4.2 and 1805.4.3.

1807.2.3 Safety Factor
Retaining walls shall be designed to resist the lateral action of soil to produce sliding and overturning with a minimum safety factor of 1.5 in each case. EXCEPTION: Where earthquake loads are included, the minimum safety factor for retaining wall sliding and overturning shall be 1.1.

The load combinations of Section 1605 shall not apply to this requirement. Instead, design shall be based on 0.7 times nominal earthquake loads, 1.0 times other nominal loads, and investigation with one or more of the variable loads set to zero. 

The safety factor against lateral sliding shall be taken as the available soil resistance at the base of the retaining wall foundation divided by the net lateral force applied to the retaining wall.

1807.2.4 Segmental Retaining Walls
Dry-cast concrete units used in the construction of segmental retaining walls shall comply with ASTM C1372.
"""

from dataclasses import dataclass

# Design Values for INORGANIC CLAYS OF LOW TO MEDIUM PLASTICITY
# Classified as CL per ASTM D2487 Unified Soil Classification.

# MAXIMUM BEARING PRESSURE
VERTICAL = 1500  # psf
FRICTION = 0  # Use 0.25 for non-CL
COHESION = 130  # psf to be multiplied by the contact area.
# The lateral sliding resistance shall not exceed one-half the dead load.
LATERAL = 100  # psf per foot below natural grade.
# The lateral bearing pressures specified in Table 1806.2
# shall be permitted to be increased by the tabular value
# for each additional foot of depth to a value that is
# not greater than 15 times the tabular value.

# Isolated poles for uses such as flagpoles or signs and poles
# used to support buildings that are not adversely affected by a
# 1/2-inch (12.7 mm) motion at the ground surface due to short-term
# lateral loads shall be permitted to be designed using lateral
# bearing pressures equal to two times the tabular values.

# SOIL LATERAL LOADS:
ACTIVE = 60  # psf per foot of depth
REST = 100  # psf per foot of depth

# Material Unit Weights
CONC = 150  # pounds per cubic foot
SOIL = 115  # pounds per cubic foot
H2O = 62.4  # pounds per cubic foot


def run():
    i = 1  # placeholder
    d = Wall(4, 2, 2, 2, 0.6, 0.6, 0)
    wordy = f"""
        Parameter   OK     Safety Factor     
        Overturning {d.OT_OK()}     {str(d.OT_SF())[2:4]}% 
        Sliding     {d.slide_OK()}     {str(d.slide_SF())[2:4]}%  and  {} of gravity load.
        Bearing     {i}          {i}
        Uplift      {i}          {i}"""
    print(wordy)


def verbose(data):
    return "{}: {} lateral pressure causes a moment of {} ft-lb and results in a soil bearing pressure of {} psf which is {} of the allowable {} psf.\n".format(
        data[0],
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
    )


@dataclass
class Wall:
    # PROD add support for hyrdostatic and surcharge
    height: float  # above grade
    depth: float  # below grade to bottom of base, not key
    toe: float  # base passive extension
    heel: float  # base active extension
    t_stem: float  # thickness of stem
    t_base: float  # thickness of base
    key: float  # key depth
    active: bool = True

    def g_stem(self):
        return CONC * self.height * self.t_stem

    def g_toe(self):
        return CONC * self.toe * self.t_base

    def g_heel(self):
        return CONC * self.heel * self.t_base

    def g_key(self):
        return CONC * self.key * self.t_stem

    def g_soil(self):
        return SOIL * self.heel * (self.height - self.t_base)

    def gravity(self):
        return sum(
            [self.g_stem(), self.g_toe(), self.g_heel(), self.g_key(), self.g_soil()]
        )

    def lateral(self):
        return REST * ((self.height + self.depth) ** 2) / 2

    def M_ovt(self):
        return REST * ((self.height + self.depth) ** 3) / 6

    def M_res(self):
        return self.gravity() * (self.toe + self.t_stem / 2)

    def OT_SF(self):
        return self.M_res() / self.M_ovt()

    def OT_OK(self):
        return self.OT_SF() >= 1.5

    def slide_res(self):
        return COHESION * (self.toe + self.heel + self.t_stem)

    def slide_SF(self):
        return self.slide_res() / self.lateral()

    def slide_OK(self):
        return self.slide_SF() >= 1


if __name__ == "__main__":
    run()

