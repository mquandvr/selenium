def rightTriangle(sides):
    sides.sort()
    return sides[0]**2+sides[1]**2==sides[2]**2