from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

__author__ = 'wliu'


def sympy_polygon_to_shapely(sympy_polygon):
    try:
        coords = [point.args for point in sympy_polygon.vertices]
        shapely_poly = Polygon(coords)
        return shapely_poly
    except:
        return sympy_polygon

    
def sympy_point_to_shapely(sympy_point):
    try:
        shapely_point = Point(sympy_point.args)
        return shapely_point
    except:
        return sympy_point