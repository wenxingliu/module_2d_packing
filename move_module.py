import sympy as sym

__author__ = 'wliu'


def move_rotate_module_polygon(module, rotate_point, offset, angle):
    offset_points = []

    for point in module.vertices:
        offset_point = (point.args[0] + offset[0], point.args[1] + offset[1])
        offset_points.append(sym.Point2D(offset_point))

    offset_polygon = sym.Polygon(*offset_points)
    
    return offset_polygon.rotate(angle, rotate_point)