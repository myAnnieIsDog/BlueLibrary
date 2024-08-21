"""
Tools for structural engineering. 

Lengths are feet unless noted otherwise (u.n.o.)
Inches are used frequently for user interface. Be careful.

Point loads are # where 1# = 1 pound u.n.o.
Area loads are PSF where 1 psf = 1# per square foot u.n.o.

Stresses are KSI where 1 psi = 1# pound per square inch u.n.o.
Moments (torques) are KIP-FT u.n.o.
Strain is IN/IN u.n.o
"""


def run():
    a = check_overturning(
        lateral_load=1,
        lateral_height=1,
        extra_moment=0,
        uplift=0,
        mass=1,
        center=1.5,
    )
    print(a)

def check_overturning(
    lateral_load, # resultant lateral load magnitude
    lateral_height, # resultant lateral load height
    extra_moment, # additional applied moment
    uplift, # uplift forces during overturning event
    mass, # mass of the object
    center, # lateral distance from the center of mass to fulcrum
    SF_req=1.5, # Required safety factor against overturning  
):
    OT_moment = extra_moment + lateral_load * lateral_height
    R_moment = (mass - uplift) * center
    SF_actual = R_moment / OT_moment
    ok = True if SF_actual >= SF_req else False
    return [ok, SF_actual]

def check_sliding(
    lateral_load, # resultant lateral load magnitude
    soil_depth, # Depth of foundation below the soil surface
    friction, # Coefficient of friction between soil and foundation
    cohesion, # Soil cohesion to the foundation
    soil_sg, # Specific gravity of the soil 
):
    pass  
    

    
class load_dist():
    self.start = 0
    self.end = 1 
    self.magnitude = None


class load_point():
    pass

class Beam():
    def __ini__():
        self.material = None
        self.length = None
        self.height = None
        self.width = None
        
        self.load_axial = None
        self.load_primary = None
        self.load_secondary = None
        self.load_torsion = None
        
    
    def method(self):
        print(PI5) 
"""


if __name__ == "__main__":
    run()

