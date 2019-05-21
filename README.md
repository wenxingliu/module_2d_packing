## Requirements

python==3.6

sympy==1.4

matplotlib==2.2.3

shapely==1.6.4.post2


## How To Use

#### Run function
Please use *main.ipynb* to run the main function. Inputs are:
1. Box size, a tuple of (height, width).
2. The corners of a given module. Remeber to position the left-bottom corner to origin, and place the entire module in first quadrant.

#### Hyper Parameters

Since this is a brute-force algorithm, there are two hyper parameters:
1. Number of iterations per simulation.
2. Total number of simulations.

Running the script with larger hyper parameters will always give you better results. On the other hand, it will always take longer.


#### Outputs
For a given set of box and module, the script will find layouts that can hold a max number of modules, where this max is determined from repeated simulation. The script will export a plot showing the layout, as well as a csv file with coordinates of all corners. Outputs are stored in *outputs* folder. And as you can see in the following plots, each scenario could have more than one optimal layout.


#### Examples of M-type modules Layout

![Alt text](outputs/M_type_eg1.png?raw=true "M-type Module")

![Alt text](outputs/M_type_eg2.png?raw=true "M-type Module")