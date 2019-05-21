from collections import defaultdict
from utils import build_box, build_module
from search import search_in_all_open_area
from polygon_computation import find_open_area
from plot_polygon import plot_polygons

__author__ = 'wliu'


def generate_2d_packing_layout(box, module, random_search=False, save_plot=False):
    module_list = [module, ]

    list_of_open_area = find_open_area(box=box, existing_modules=module_list)

    for iter_num in range(1000):

        new_module = search_in_all_open_area(open_area_list=list_of_open_area, module=module,
                                             random_search=random_search)

        if new_module:
            module_list.append(new_module)
            list_of_open_area = find_open_area(box=box, existing_modules=module_list)

        no_feasible_open_area_left = len(list_of_open_area) == 0

        if no_feasible_open_area_left or (new_module is None):
            break

    if save_plot:
        plot_polygons(poly_list=[box, *module_list], plot_name='')

    return module_list


def simulation(box_dim, module_coordinates, N=50, plot_name='', random_search=False):
    box = build_box(box_dim)
    module = build_module(module_coordinates)

    max_num = int(box.area / module.area)
    print(f'Number of modules is bounded by {max_num}')

    module_layouts = defaultdict(list)
    max_num_modules = 0

    for iter_num in range(1, N + 1):
        print(f'Simulation {iter_num}...')
        modules = generate_2d_packing_layout(box=box,
                                             module=module,

                                             random_search=random_search,
                                             save_plot=False)
        num_modules = len(modules)
        module_layouts[num_modules].append(modules)

        print(f'Layout from {iter_num} simulation can fit in {num_modules} modules')

        if num_modules > max_num_modules:
            max_num_modules = num_modules

    print(f'Best layout can fit in {max_num_modules} modules')

    for best_layout in module_layouts[max_num_modules]:
        plot_polygons(poly_list=[box, *best_layout], plot_name=plot_name)

    return module_layouts[max_num_modules]
