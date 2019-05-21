import json

import numpy as np
import sympy as sym

__author__ = 'wliu'


def build_box(box_dim):
    height, width = box_dim
    rec_points = map(sym.Point2D, [(0, 0), (0, height), (width, height), (width, 0)])
    rec = sym.Polygon(*rec_points)
    return rec


def build_module(module_coordinates):
    module_points = map(sym.Point2D, module_coordinates)
    module = sym.Polygon(*module_points)
    return module


def polygon_to_coords(poly):
    coords_list = []
    for point in poly.vertices:
        coords_list.append(point.args)
    return coords_list


def modules_to_coords(list_of_modules):
    module_coords = []
    
    for module_idx, module in enumerate(list_of_modules):
        coords_list = polygon_to_coords(module)
        module_info = {}
        
        for point_idx, coords in enumerate(coords_list):
            module_info[f"module_{module_idx}_point_{point_idx}_x"] = str(coords[0])
            module_info[f"module_{module_idx}_point_{point_idx}_y"] = str(coords[1])

        module_coords.append(module_info)
    
    return module_coords


def log_modules_to_json(poly_list, file_name):
    coords_data = modules_to_coords(poly_list)
    with open(f'{file_name}.json', 'w') as fp:
        json.dump(coords_data, fp)


def _compute_width_and_height(shape):
    x_list = [point.args[0] for point in shape.vertices]
    y_list = [point.args[1] for point in shape.vertices]
    width = np.max(x_list) - np.min(x_list)
    height = np.max(y_list) - np.min(y_list)

    width, height = max([width, height]), min([width, height])

    return width, height
