import numpy as np
from random import choice

import sympy as sym
from sympy import geometry as geom

from polygon_computation import check_if_polygons_overlap_with_each_other, check_if_module_is_in_box, find_open_area
from plot_polygon import plot_polygons
from move_module import move_rotate_module_polygon

__author__ = 'wliu'


def _compute_width_and_height(shape):
    x_list = [point.args[0] for point in shape.vertices]
    y_list = [point.args[1] for point in shape.vertices]
    width = np.max(x_list) - np.min(x_list)
    height = np.max(y_list) - np.min(y_list)
    return width, height


def _compute_search_grid_params(box, module, existing_modules):
    
    box_width, box_height = _compute_width_and_height(box)
    
    grid_search_angle = np.array([-sym.pi/2, 0, sym.pi/2, sym.pi])
    
    offset_step = 1
    grid_search_offset_x = np.arange(0, box_width + offset_step, offset_step)
    grid_search_offset_y = np.arange(0, box_height + offset_step, offset_step)
    
    start_points = [point for m in existing_modules for point in m.vertices]
    
    grid_search_params = {"start_point": start_points,
                          "angle": grid_search_angle, 
                          "x_offset": grid_search_offset_x, 
                          "y_offset": grid_search_offset_y}
    
    return grid_search_params


def search_for_next_module_position(box, module, existing_modules):
    
    grid_search_params = _compute_search_grid_params(box=box, module=module, existing_modules=existing_modules)
    
    grid_search_start_point = grid_search_params['start_point']
    grid_search_angle = grid_search_params['angle']
    grid_search_offset_x = grid_search_params['x_offset']
    grid_search_offset_y = grid_search_params['y_offset']
    
    open_area_shapely_obj = find_open_area(box=box, existing_modules=existing_modules)
    
    for start_point in grid_search_start_point:

        for x in grid_search_offset_x:

            for y in grid_search_offset_y:
                offset = (x, y)

                for angle in grid_search_angle: 
                    new_module = move_rotate_module_polygon(offset=offset, 
                                                            angle=angle, 
                                                            rotate_point=start_point,
                                                            module=module)

                    if (check_if_module_is_in_box(new_module, open_area_shapely_obj) 
                        and not check_if_polygons_overlap_with_each_other(new_poly=new_module, 
                                                                          list_of_polys=existing_modules)):
                        return new_module
                    

def random_search_for_next_module_position(box, module, existing_modules):
    
    open_area_shapely_obj = find_open_area(box=box, existing_modules=existing_modules)
    
    grid_search_params = _compute_search_grid_params(box=box, module=module, existing_modules=existing_modules)
    
    grid_search_start_point = grid_search_params['start_point']
    grid_search_angle = grid_search_params['angle']
    grid_search_offset_x = grid_search_params['x_offset']
    grid_search_offset_y = grid_search_params['y_offset']
    
    new_module = None
    
    while new_module is None:
        
        start_point = choice(grid_search_start_point)
        x = choice(grid_search_offset_x)
        y = choice(grid_search_offset_y)
        offset = (x, y)
        angle = choice(grid_search_angle)

        new_module = move_rotate_module_polygon(offset=offset, 
                                                angle=angle, 
                                                rotate_point=start_point,
                                                module=module)
        
        if (new_module is not None 
            and check_if_module_is_in_box(new_module, open_area_shapely_obj) 
            and not check_if_polygons_overlap_with_each_other(new_poly=new_module, 
                                                              list_of_polys=existing_modules)):
            return new_module
                    
                    
                    