import random
import matplotlib
from matplotlib.colors import LinearSegmentedColormap

matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

map_height = 150
map_width = 200

number_of_lakes = 1
size_of_lakes = 1
number_of_wildfires = 1
chance_to_spread_fire = 0.15
chance_to_change_wind_direction_every_5_hours = 0.08
number_of_hours = 200
rate_of_fire_extinction = 0.01

fig, ax = plt.subplots(num="Wildfire simulator")
map_of_forest = []
map_size = ()
element = ''

line2d, = ax.plot([])

wind_possible_directions = ["North", "North East", "East", "South East", "South",
                            "South West", "West", "North West"]
actual_wind_direction = random.choice(wind_possible_directions)

fire_patterns = {'North': [[1, 2, 1], [0, 0, 0], [0, 0, 0]], 'North East': [[0, 1, 2], [0, 0, 1], [0, 0, 0]],
                 'East': [[0, 0, 1], [0, 0, 2], [0, 0, 1]], 'South East': [[0, 0, 0], [0, 0, 1], [0, 1, 2]],
                 'South': [[0, 0, 0], [0, 0, 0], [1, 2, 1]], 'South West': [[0, 0, 0], [1, 0, 0], [2, 1, 0]],
                 'West': [[1, 0, 0], [2, 0, 0], [1, 0, 0]], 'North West': [[2, 1, 0], [1, 0, 0], [0, 0, 0]]}

cmap = LinearSegmentedColormap.from_list('GreenRed', ['forestgreen', 'darkblue', 'black', 'black', 'black', 'red'])


def refresh_map_with_fire(pattern):
    global list_of_old_maps, map_size, element, chance_to_spread_fire
    tmp_map_of_forest = map_of_forest.copy()
    for i in range(1, map_size[0] - 1):
        for j in range(1, map_size[1] - 1):
            if map_of_forest[i][j] == 0:
                chance_of_fire = 0
                if tmp_map_of_forest[i - 1][j - 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i - 1][j] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.25
                if tmp_map_of_forest[i - 1][j + 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i][j + 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.25
                if tmp_map_of_forest[i + 1][j + 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i + 1][j] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.25
                if tmp_map_of_forest[i + 1][j - 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i][j - 1] > 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.25

                if tmp_map_of_forest[i + 1][j - 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[0][0]
                if tmp_map_of_forest[i + 1][j] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[0][1]
                if tmp_map_of_forest[i + 1][j + 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[0][2]
                if tmp_map_of_forest[i][j - 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[1][0]
                if tmp_map_of_forest[i][j + 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[1][2]
                if tmp_map_of_forest[i - 1][j - 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[2][0]
                if tmp_map_of_forest[i - 1][j] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[2][1]
                if tmp_map_of_forest[i - 1][j + 1] >= 0.8:
                    chance_of_fire += chance_to_spread_fire * 0.5 * pattern[2][2]
                if chance_of_fire > 1:
                    chance_of_fire = 1
                tmp_map_of_forest[i][j] = 1 if random.randint(0, 100) < chance_of_fire * 100 else 0

    for i in range(map_size[0]):
        for j in range(map_size[1]):
            if tmp_map_of_forest[i][j] > 0.78 and random.randint(0, 10) < 5:
                tmp_map_of_forest[i][j] = tmp_map_of_forest[i][j] - rate_of_fire_extinction

    return tmp_map_of_forest


def refresh_map_with_water(pattern):
    global list_of_old_maps, map_size, element, chance_to_spread_fire
    tmp_map_of_forest = map_of_forest.copy()
    for i in range(1, map_size[0] - 1):
        for j in range(1, map_size[1] - 1):
            if map_of_forest[i][j] == 0:
                chance_of_water = 0
                if tmp_map_of_forest[i - 1][j - 1] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i - 1][j] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.25
                if tmp_map_of_forest[i - 1][j + 1] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i][j + 1] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.25
                if tmp_map_of_forest[i + 1][j + 1] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i + 1][j] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.25
                if tmp_map_of_forest[i + 1][j - 1] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.125
                if tmp_map_of_forest[i][j - 1] >= 0.06:
                    chance_of_water += chance_to_spread_fire * 0.25
                if chance_of_water > 1:
                    chance_of_water = 1
                tmp_map_of_forest[i][j] = 0.06 if random.randint(0, 100) < chance_of_water * 100 else 0

    for i in range(map_size[0]):
        for j in range(map_size[1]):
            if 0.34 > tmp_map_of_forest[i][j] >= 0.06 and random.randint(0, 10) < 5:
                tmp_map_of_forest[i][j] = tmp_map_of_forest[i][j] + 0.02

    return tmp_map_of_forest


def changeWindDirection():
    global actual_wind_direction
    actual_wind_direction_index = wind_possible_directions.index(actual_wind_direction)
    direction_change = random.choice([-2, -1, -1, -1, 1, 1, 1, 2])
    if actual_wind_direction_index == 0 and (direction_change == -1 or direction_change == -2):
        actual_wind_direction = wind_possible_directions[len(wind_possible_directions) + direction_change]
    elif actual_wind_direction_index == 1 and direction_change == -2:
        actual_wind_direction = wind_possible_directions[len(wind_possible_directions) - 1]
    elif actual_wind_direction_index == len(wind_possible_directions) - 1 and (
            direction_change == 1 or direction_change == 2):
        actual_wind_direction = wind_possible_directions[2 - direction_change]
    elif actual_wind_direction_index == len(wind_possible_directions) - 2 and direction_change == 2:
        actual_wind_direction = wind_possible_directions[0]
    else:
        actual_wind_direction = wind_possible_directions[actual_wind_direction_index + direction_change]


def animate(hours):
    global actual_wind_direction, map_of_forest, ax, element
    # if hours % 50 ==0:
    #     plt.savefig(str(str(hours/5)) + ".png")
    if (hours) % (number_of_hours / 2) == 0 and hours != 0:
        print(str(hours / (number_of_hours / 20)) + "%")
    elif (number_of_hours * 5) - 1 == hours:
        print("100.0%")
    if random.randint(0, 100) < (chance_to_change_wind_direction_every_5_hours * 100) and hours % 25 == 0:
        changeWindDirection()
    plt.cla()

    pattern = fire_patterns[actual_wind_direction]
    map_of_forest = refresh_map_with_fire(pattern)
    ax = sns.heatmap(data=map_of_forest, vmin=0, vmax=1, cbar=False, cmap=cmap, yticklabels=False,
                     xticklabels=False)

    title = "Hours: " + str(int(hours / 5) + 1).zfill(4) + "       Wind direction: " + actual_wind_direction
    fig.suptitle(title, fontsize=15, x=0.15, y=.95, horizontalalignment='left')
    return line2d,


def run_wildfire(run_simulation_canvas, save_simulation_as_gif):
    global map_of_forest, map_size, element, fig
    element = 'fire'

    animation_of_simulation = animation.FuncAnimation(fig, animate, frames=number_of_hours * 5,
                                                      interval=1, blit=True, repeat=False)

    if run_simulation_canvas:
        plt.show()

    if save_simulation_as_gif:
        animation_of_simulation.save('Wildfire in the forest no0.gif', writer='imagemagick', fps=14)

    plt.close()


def create_forest():
    global map_of_forest, map_size, element, actual_wind_direction, number_of_wildfires
    element = "water"
    map_size = (map_height, map_width)
    map_of_forest = np.zeros(map_size)

    for i in range(number_of_lakes):
        lake = [random.randint(10, map_size[0] - 10), random.randint(10, map_size[1] - 10)]
        map_of_forest[lake[0]][lake[1]] = 0.06

    for i in range(int(number_of_hours / 150 * size_of_lakes)):
        if random.randint(0, 1) == 1 and i % 15 == 1:
            changeWindDirection()
        pattern = fire_patterns[actual_wind_direction]
        map_of_forest = refresh_map_with_water(pattern)

    while number_of_wildfires > 0:
        wildfire = [random.randint(10, map_size[0] - 10), random.randint(10, map_size[1] - 10)]
        if map_of_forest[wildfire[0]][wildfire[1]] == 0:
            map_of_forest[wildfire[0]][wildfire[1]] = 1
            number_of_wildfires = number_of_wildfires - 1
