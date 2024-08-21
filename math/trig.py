""" 
The study of angles and rotation applied to triangles and circles.
"""
import decimal

D = decimal.Decimal
cntxt = decimal.getcontext()


def run():
    pi5 = D("3.14159")
    tau5 = 2 * pi5
    print(str(pi5) + " or PI is the perimeter divided by DIAMETER.")
    print(str(tau5) + " or TAU, is the perimeter divided by RADIUS.")


if __name__ == "__main__":
    run()
