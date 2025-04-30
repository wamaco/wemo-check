from typing import List, Tuple

def polygon_area(vertices: List[Tuple[float, float]]) -> float:
    """
    Computes the area of a simple polygon using the shoelace formula.
    The polygon is defined by a list of (x, y) points in order.
    """
    n = len(vertices)
    area = 0.0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # next vertex (wrap around)
        area += (x1 * y2) - (x2 * y1)

    return abs(area) / 2.0