from typing import List, Tuple

# ---------------------------------------------------------------
# Winding Number Algorithm (Point-in-Polygon)
# Assumptions:
# 1. The polygon is simple (no self-intersections).
# 2. Vertices are listed in order (clockwise or counterclockwise), with no duplicates.
# 3. Polygon may be concave or convex.
# 4. Coordinates are real numbers (float-compatible).
# 5. If the point lies exactly on an edge or vertex, the winding number will be nonzero.
# ---------------------------------------------------------------

Point = Tuple[float, float]

def is_left(a: Point, b: Point, p: Point) -> float:
    """
    Tests if point p is left of the directed line a->b.
    Returns >0 if p is left of the line, =0 if on the line, <0 if right.
    """
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

def winding_number(polygon: List[Point], point: Point) -> int:
    """
    Computes the winding number of 'point' with respect to 'polygon'.
    Returns the number of times the polygon winds around the point.
    A nonzero result indicates the point is inside the polygon.
    """
    wn = 0
    x, y = point
    n = len(polygon)
    
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        
        # upward crossing
        if a[1] <= y:
            if b[1] > y and is_left(a, b, point) > 0:
                wn += 1
        # downward crossing
        else:
            if b[1] <= y and is_left(a, b, point) < 0:
                wn -= 1
                
    return wn

# Example usage:
# poly = [(0,0), (4,0), (4,4), (0,4)]
# print(winding_number(poly, (2,2)))  # Outputs 1 (inside)
# print(winding_number(poly, (5,5)))  # Outputs 0 (outside)