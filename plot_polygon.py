import datetime as dt
from itertools import cycle
import matplotlib.pyplot as plt

import numpy as np

from utils import modules_to_coords, log_modules_to_json

__author__ = 'wliu'


def get_poly_coordinates(poly):
    poly_points = poly.vertices
    poly_points.append(poly_points[0])
    x = [point.args[0] for point in poly_points]
    y = [point.args[1] for point in poly_points]
    return x, y


def plot_polygons(poly_list, plot_name):
    time_str = dt.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'{plot_name}_{time_str}'
    
    # plot and save
    cycol = cycle('bgrcmk')
    plt.axis('equal')
    
    for k, poly in enumerate(poly_list): 
        x, y = get_poly_coordinates(poly)
        color = next(cycol)
        
        for i in range(len(x)):
            plt.plot(x[i:i+2], y[i:i+2], c=color, linestyle='-')
    
    plt.savefig(f'outputs/{file_name}_layout.png')
    plt.close()
    
    # log coordinates of modules
    log_modules_to_json(poly_list, f'outputs/{file_name}_coords')