from typing import List, Tuple
import math

# ---------------------------------------------------------------
# Closest Pair of Points (2D) - Divide and Conquer
# Assumptions:
# 1. The input is a list of distinct 2D points (x, y) as tuples
# 2. Euclidean distance is used
# 3. No duplicate points
# 4. Points are real numbers (float-compatible)
# Time Complexity: O(n log n)
# ---------------------------------------------------------------

Point = Tuple[float, float]

def euclidean_distance(p1: Point, p2: Point) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Handles small point sets directly."""
    min_dist = float('inf')
    pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return min_dist, pair

def strip_closest(strip: List[Point], delta: float, best_pair: Tuple[Point, Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Find closest pair in the strip (within delta of midline)."""
    min_dist = delta
    n = len(strip)
    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            if abs(strip[j][1] - strip[i][1]) >= min_dist:
                break
            dist = euclidean_distance(strip[i], strip[j])
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

    # Build strip of points within delta of midpoint
    strip = [p for p in Py if abs(p[0] - midpoint) < delta]
    return strip_closest(strip, delta, best_pair)

def closest_pair(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Main function to return the closest pair and their distance."""
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(Px, Py)