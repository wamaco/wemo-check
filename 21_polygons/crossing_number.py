from typing import List, Tuple

# ---------------------------------------------------------------
# Crossing Number Algorithm (Point-in-Polygon)
# Assumptions:
# 1. The polygon is simple (no self-intersections).
# 2. Vertices are listed in order (clockwise or counterclockwise) with no duplicates.
# 3. Both polygon vertices and query point coordinates are real numbers.
# 4. If the point lies exactly on an edge, the function returns True.
# 5. Horizontal edges are handled via a half-open interval convention.
# ---------------------------------------------------------------

Point = Tuple[float, float]

def crossing_number(polygon: List[Point], point: Point) -> bool:
    """
    Determines if a point lies inside a polygon using the crossing number algorithm.
    Returns True if inside or on the boundary, False otherwise.
    """
    x, y = point
    n = len(polygon)
    count = 0

    # Helper to check if point is on segment ab
    def on_segment(a: Point, b: Point) -> bool:
        (x1, y1), (x2, y2) = a, b
        # Collinearity check via cross product
        if (b[0] - a[0]) * (y - a[1]) != (b[1] - a[1]) * (x - a[0]):
            return False
        # Check within bounding box
        return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]

        # If point is exactly on an edge, consider it inside
        if on_segment(a, b):
            return True

        x1, y1 = a
        x2, y2 = b

        # Check if the edge crosses the horizontal ray to the right of the point
        if (y1 > y) != (y2 > y):  # One endpoint above, one below
            # Compute intersection x-coordinate of the edge with the horizontal line at y
            x_int = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x_int > x:
                count += 1

    # Inside if crossings count is odd
    return (count % 2) == 1

# Example usage:
# polygon = [(0,0), (4,0), (4,4), (0,4)]
# print(crossing_number(polygon, (2,2)))  # True (inside)
# print(crossing_number(polygon, (5,5)))  # False (outside)
