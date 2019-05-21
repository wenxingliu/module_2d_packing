from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import sympy as sym

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
    
    
def shapely_polygon_to_sym(shapely_polygon):
    try:
        poly_coords = shapely_polygon.exterior.coords.xy
        poly_coords = [(poly_coords[0][i],poly_coords[1][i]) for i in range(len(poly_coords[0]))]
        sym_poly = sym.Polygon(*poly_coords)
        return sym_poly
    except:
        return shapely_polygon
