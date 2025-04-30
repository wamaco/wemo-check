from typing import List, Tuple

# ---------------------------------------------------------------
# Closest Pair of Points (2D) - Divide and Conquer
# Assumptions:
# 1. The input is a list of distinct 2D points (x, y) as tuples
# 2. Euclidean distance is used (we return the squared distance)
# 3. No math module used (no square roots)
# 4. Points are float-compatible; returns squared distance
# Time Complexity: O(n log n)
# ---------------------------------------------------------------

Point = Tuple[float, float]

def squared_distance(p1: Point, p2: Point) -> float:
    """Returns squared Euclidean distance (no sqrt)."""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx * dx + dy * dy

def brute_force(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    min_dist = float('inf')
    pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = squared_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return min_dist, pair

def strip_closest(strip: List[Point], delta: float, best_pair: Tuple[Point, Point]) -> Tuple[float, Tuple[Point, Point]]:
    min_dist = delta
    n = len(strip)
    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            if (strip[j][1] - strip[i][1]) ** 2 >= min_dist:
                break
            dist = squared_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                best_pair = (strip[i], strip[j])
    return min_dist, best_pair

def closest_pair_rec(Px: List[Point], Py: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    n = len(Px)
    if n <= 3:
        return brute_force(Px)

    mid = n // 2
    midpoint = Px[mid][0]

    Qx = Px[:mid]
    Rx = Px[mid:]
    Qy = [p for p in Py if p[0] <= midpoint]
    Ry = [p for p in Py if p[0] > midpoint]

    d1, pair1 = closest_pair_rec(Qx, Qy)
    d2, pair2 = closest_pair_rec(Rx, Ry)

    if d1 < d2:
        delta, best_pair = d1, pair1
    else:
        delta, best_pair = d2, pair2

    strip = [p for p in Py if (p[0] - midpoint) ** 2 < delta]
    return strip_closest(strip, delta, best_pair)

def closest_pair(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(Px, Py)