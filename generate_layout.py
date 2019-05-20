from collections import defaultdict
from utils import build_box, build_module
from search import search_for_next_module_position, random_search_for_next_module_position
from plot_polygon import plot_polygons

__author__ = 'wliu'


def generate_2d_packing_layout(box, module, max_iter=5000, random_search=False, save_plot=False):
    
    module_list = [module, ]
    
    consecutive_failed_count = 0
    
    for iter_num in range(max_iter):
        
        if random_search:
            new_module = random_search_for_next_module_position(box=box, 
                                                                module=module, 
                                                                existing_modules=module_list)
        else:
            new_module = search_for_next_module_position(box=box, 
                                                         module=module, 
                                                         existing_modules=module_list)

        if new_module:
            module_list.append(new_module)
            consecutive_failed_count = 0
        else:
            consecutive_failed_count += 1
        
        if consecutive_failed_count > 1000:
            break
            
    if save_plot:
        plot_polygons(poly_list=[box, *module_list], plot_name='')
    
    return module_list


def simulation(box_dim, module_coordinates, max_iter_per_simulation=5000, N=50, plot_name=''):
    
    box = build_box(box_dim)
    module = build_module(module_coordinates)
    
    max_num = int(box.area / module.area) + 1
    print(f'Number of modules is bounded by {max_num}')
    
    module_layouts = defaultdict(list)
    max_num_modules = 0
    
    for iter_num in range(1, N+1):
        print(f'Simulation {iter_num}...')
        modules = generate_2d_packing_layout(box=box, 
                                             module=module, 
                                             max_iter=max_iter_per_simulation,
                                             random_search=True,
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