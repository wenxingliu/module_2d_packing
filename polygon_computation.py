from shapely_sympy_converter import sympy_polygon_to_shapely

__author__ = 'wliu'


def check_if_two_polygons_overlap(poly_1, poly_2) -> bool:
    '''
    If overlaps, return True
    '''
    
    poly_1_tr = sympy_polygon_to_shapely(poly_1)
    poly_2_tr = sympy_polygon_to_shapely(poly_2)
    
    intersection_poly = poly_1_tr.intersection(poly_2_tr)
    return intersection_poly.area != 0
    

def check_if_polygons_overlap_with_each_other(new_poly, list_of_polys) -> bool:
    '''
    If new polygon overlaps with any in the list, returns True
    '''
    for poly in list_of_polys:
        if check_if_two_polygons_overlap(new_poly, poly):
            return True
    return False


def check_if_module_is_in_box(module, box):
    box_tr = sympy_polygon_to_shapely(box)
    module_tr = sympy_polygon_to_shapely(module)
    return box_tr.contains(module_tr)


def find_open_area(box, existing_modules):

    module_union = sympy_polygon_to_shapely(existing_modules[0])

    for module in existing_modules[1:]:
        module_tr = sympy_polygon_to_shapely(module)
        module_union = module_union.union(module_tr)
    
    box_tr = sympy_polygon_to_shapely(box)
    open_area = box_tr.difference(module_union)

    return open_area