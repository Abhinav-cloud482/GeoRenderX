import math
import random
from typing import List, Optional, Tuple

EPSILON = 1e-6

# =========================
# VECTOR
# =========================
class Vec3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __add__(self, o): return Vec3(self.x+o.x, self.y+o.y, self.z+o.z)
    def __sub__(self, o): return Vec3(self.x-o.x, self.y-o.y, self.z-o.z)
    def __mul__(self, s): return Vec3(self.x*s, self.y*s, self.z*s)

    def dot(self, o): return self.x*o.x + self.y*o.y + self.z*o.z

    def norm(self):
        l = math.sqrt(self.dot(self))
        return self * (1.0 / (l + EPSILON))


# =========================
# OBJECTS
# =========================
class Sphere:
    def __init__(self, center: Vec3, radius: float, color: Vec3):
        self.center = center
        self.radius = radius
        self.color = color

    def intersect(self, origin: Vec3, direction: Vec3):
        oc = origin - self.center
        a = direction.dot(direction)
        b = 2 * oc.dot(direction)
        c = oc.dot(oc) - self.radius**2

        disc = b*b - 4*a*c
        if disc < 0:
            return None

        t = (-b - math.sqrt(disc)) / (2*a)
        return t if t > EPSILON else None


class Light:
    def __init__(self, position: Vec3):
        self.position = position


# =========================
# RAY TRACER (IMPROVED)
# =========================
def in_shadow(point, light, objects):
    dir = (light.position - point).norm()
    for obj in objects:
        if obj.intersect(point + dir * EPSILON, dir):
            return True
    return False


def trace_ray(origin, direction, objects, light):
    closest_t = float("inf")
    hit_obj = None

    for obj in objects:
        t = obj.intersect(origin, direction)
        if t and t < closest_t:
            closest_t = t
            hit_obj = obj

    if not hit_obj:
        return 0

    hit_point = origin + direction * closest_t
    normal = (hit_point - hit_obj.center).norm()

    light_dir = (light.position - hit_point).norm()

    # Shadow check
    if in_shadow(hit_point, light, objects):
        return 0.1  # ambient only

    diffuse = max(0, normal.dot(light_dir))
    ambient = 0.1

    return min(1, diffuse + ambient)


# =========================
# KD-TREE
# =========================
class KDNode:
    def __init__(self, points: List[Vec3], depth=0):
        if not points:
            self.point = None
            return

        axis = depth % 3
        points.sort(key=lambda p: (p.x, p.y, p.z)[axis])
        mid = len(points) // 2

        self.point = points[mid]
        self.left = KDNode(points[:mid], depth+1) if mid > 0 else None
        self.right = KDNode(points[mid+1:], depth+1) if mid+1 < len(points) else None


def nearest_neighbor(node, target, depth=0, best=None):
    if not node or not node.point:
        return best

    axis = depth % 3

    dist = (node.point - target).dot(node.point - target)
    if best is None or dist < best[1]:
        best = (node.point, dist)

    diff = (target.x - node.point.x,
            target.y - node.point.y,
            target.z - node.point.z)[axis]

    close, away = (node.left, node.right) if diff < 0 else (node.right, node.left)

    best = nearest_neighbor(close, target, depth+1, best)

    if diff**2 < best[1]:
        best = nearest_neighbor(away, target, depth+1, best)

    return best


# =========================
# CONVEX HULL
# =========================
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])


def convex_hull(points):
    points = sorted(points)

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


# =========================
# VORONOI
# =========================
def voronoi(points, w=40, h=20):
    grid = [["." for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            best, best_d = 0, float("inf")
            for i, (px, py) in enumerate(points):
                d = (px-x)**2 + (py-y)**2
                if d < best_d:
                    best_d, best = d, i
            grid[y][x] = str(best)

    return grid


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    # -------- RAY TRACER --------
    width, height = 80, 40
    camera = Vec3(0, 0, -2)

    objects = [
        Sphere(Vec3(0, 0, 4), 1, Vec3(1, 0, 0)),
        Sphere(Vec3(2, 0, 5), 1, Vec3(0, 1, 0)),
        Sphere(Vec3(-2, 0, 5), 1, Vec3(0, 0, 1)),
    ]

    light = Light(Vec3(5, 5, -10))

    chars = " .:-=+*#%@"

    print("\nRay Tracer Output:\n")
    for y in range(height):
        for x in range(width):
            dir = Vec3((x-width/2)/width, (y-height/2)/height, 1).norm()
            brightness = trace_ray(camera, dir, objects, light)

            idx = int(brightness * (len(chars)-1))
            print(chars[idx], end="")
        print()

    # -------- KD TREE --------
    pts = [Vec3(random.random(), random.random(), random.random()) for _ in range(30)]
    tree = KDNode(pts)
    target = Vec3(0.5, 0.5, 0.5)

    nearest = nearest_neighbor(tree, target)
    print("\nKD-Tree Nearest Neighbor:")
    print("Point:", (nearest[0].x, nearest[0].y, nearest[0].z))
    print("Distance:", math.sqrt(nearest[1]))

    # -------- CONVEX HULL --------
    pts2d = [(random.randint(0,20), random.randint(0,20)) for _ in range(20)]
    hull = convex_hull(pts2d)

    print("\nConvex Hull Points:\n", hull)

    # -------- VORONOI --------
    seeds = [(5,5), (30,10), (20,15)]
    grid = voronoi(seeds)

    print("\nVoronoi Diagram:\n")
    for row in grid:
        print("".join(row))