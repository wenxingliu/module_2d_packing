from generate_layout import simulation

if __name__ == '__main__':
    box_dim = (8, 10)
    L_module_coordinates = [(0, 0), (0, 4), (1, 4), (1, 1), (2, 1), (2, 0)]
    L_modules = simulation(box_dim, L_module_coordinates, max_iter_per_simulation=500, N=50, plot_name='L',
                           random_search=True)

    # M_module_coordinates = [(0, 0), (0, 5), (3, 5), (1, 3), (3, 0)]  # start from (0, 0)
    # M_modules = simulation(box_dim, M_module_coordinates, max_iter_per_simulation=500, N=50, plot_name='M',
    #                        random_search=False)

    print('breakpoint')
