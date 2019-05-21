import numpy as np
from random import choice

import sympy as sym
from sympy import geometry as geom

from polygon_computation import check_if_polygons_overlap_with_each_other, check_if_module_is_in_box, find_open_area, \
    check_if_point_in_feasible_area
from shapely_sympy_converter import shapely_polygon_to_sym
from plot_polygon import plot_polygons
from move_module import move_rotate_module_polygon

__author__ = 'wliu'


def _compute_width_and_height(shape):
    x_list = [point.args[0] for point in shape.vertices]
    y_list = [point.args[1] for point in shape.vertices]
    width = np.max(x_list) - np.min(x_list)
    height = np.max(y_list) - np.min(y_list)
    return width, height


def _compute_search_grid_params(box):
    box_br = shapely_polygon_to_sym(box)

    box_width, box_height = _compute_width_and_height(box_br)

    grid_search_angle = np.array([-sym.pi / 2, 0, sym.pi / 2, sym.pi])

    offset_step = 1
    grid_search_offset_x = np.arange(0, box_width + offset_step, offset_step)
    grid_search_offset_y = np.arange(0, box_height + offset_step, offset_step)

    start_points = [point for point in box_br.vertices]

    grid_search_params = {"start_point": start_points,
                          "angle": grid_search_angle,
                          "x_offset": grid_search_offset_x,
                          "y_offset": grid_search_offset_y}

    return grid_search_params


def search_for_next_module_position(open_area, module):
    grid_search_params = _compute_search_grid_params(box=open_area)

    grid_search_start_point = grid_search_params['start_point']
    grid_search_angle = grid_search_params['angle']
    grid_search_offset_x = grid_search_params['x_offset']
    grid_search_offset_y = grid_search_params['y_offset']

    for start_point in grid_search_start_point:

        for x in grid_search_offset_x:

            for y in grid_search_offset_y:

                offset = (x, y)
                offset_point = sym.Point2D(x, y)

                if not check_if_point_in_feasible_area(point=offset_point,
                                                       open_area=open_area):
                    break

                for angle in grid_search_angle:
                    new_module = move_rotate_module_polygon(offset=offset,
                                                            angle=angle,
                                                            rotate_point=start_point,
                                                            module=module)

                    if check_if_module_is_in_box(new_module, open_area):
                        return new_module


def random_search_for_next_module_position(open_area, module):
    grid_search_params = _compute_search_grid_params(box=open_area)

    grid_search_start_point = grid_search_params['start_point']
    grid_search_angle = grid_search_params['angle']
    grid_search_offset_x = grid_search_params['x_offset']
    grid_search_offset_y = grid_search_params['y_offset']

    new_module = None
    fail_ct = 0
    fail_ct_limit = np.sqrt(open_area.area)

    while (new_module is None) and (fail_ct < fail_ct_limit):

        start_point = choice(grid_search_start_point)
        x = choice(grid_search_offset_x)
        y = choice(grid_search_offset_y)
        angle = choice(grid_search_angle)

        offset = (x, y)
        offset_point = sym.Point2D(x, y)

        if not check_if_point_in_feasible_area(point=offset_point,
                                               open_area=open_area):
            continue

        new_module = move_rotate_module_polygon(offset=offset,
                                                angle=angle,
                                                rotate_point=start_point,
                                                module=module)

        if (new_module is not None) and check_if_module_is_in_box(new_module, open_area):
            return new_module
        else:
            new_module = None
            fail_ct += 1


def search_in_all_open_area(open_area_list, module, random_search=False):
    for open_area in open_area_list:

        if random_search:
            new_module = random_search_for_next_module_position(open_area=open_area, module=module)
        else:
            new_module = search_for_next_module_position(open_area=open_area, module=module)

        return new_module
