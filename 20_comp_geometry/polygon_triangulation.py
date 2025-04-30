from typing import List, Tuple

# -------------------------------
# Polygon Triangulation (Ear Clipping)
# Assumptions:
# 1. The polygon is simple (no self-intersections)
# 2. The polygon has no holes
# 3. The vertices are given in counter-clockwise (CCW) order
# 4. The polygon has no collinear consecutive triples
# -------------------------------

Point = Tuple[float, float]

def cross(a: Point, b: Point, c: Point) -> float:
    """Returns the z-component of the cross product of vectors AB and AC."""
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def is_convex(prev: Point, curr: Point, next: Point) -> bool:
    """Returns True if the angle at 'curr' is convex (using CCW orientation)."""
    return cross(prev, curr, next) > 0

def point_in_triangle(p: Point, a: Point, b: Point, c: Point) -> bool:
    """Check if point p lies inside triangle abc using sign-based method."""
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    b1 = sign(p, a, b) < 0.0
    b2 = sign(p, b, c) < 0.0
    b3 = sign(p, c, a) < 0.0
    return (b1 == b2 == b3)

def triangulate_polygon(vertices: List[Point]) -> List[Tuple[Point, Point, Point]]:
    """Performs ear clipping triangulation on a simple polygon."""
    n = len(vertices)
    if n < 3:
        return []

    triangles = []
    verts = vertices[:]
    indices = list(range(n))  # work on index list for easy deletion

    while len(indices) > 3:
        found_ear = False
        for i in range(len(indices)):
            prev = verts[indices[i - 1]]
            curr = verts[indices[i]]
            next = verts[indices[(i + 1) % len(indices)]]

            if not is_convex(prev, curr, next):
                continue

            # Check that no other point lies inside this potential ear
            ear_valid = True
            for j in indices:
                if j in [indices[i - 1], indices[i], indices[(i + 1) % len(indices)]]:
                    continue
                if point_in_triangle(verts[j], prev, curr, next):
                    ear_valid = False
                    break

            if ear_valid:
                triangles.append((prev, curr, next))
                del indices[i]
                found_ear = True
                break

        if not found_ear:
            raise ValueError("Polygon may be non-simple or degenerate.")

    # One triangle remains
    a, b, c = verts[indices[0]], verts[indices[1]], verts[indices[2]]
    triangles.append((a, b, c))
    return triangles