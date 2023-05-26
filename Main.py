import Simulate_wildfire_of_the_forest as WF_simulation


WF_simulation.map_height = 100
WF_simulation.map_width = 150

WF_simulation.number_of_lakes = 2
WF_simulation.size_of_lakes = 200

WF_simulation.number_of_wildfires = 1
WF_simulation.chance_to_spread_fire = 0.05
WF_simulation.rate_of_fire_extinction = 0.01

WF_simulation.chance_to_change_wind_direction_every_5_hours = 0.4

WF_simulation.number_of_hours = 120

show_simulation_canvas = False
save_simulation_as_gif = True

WF_simulation.create_forest()
WF_simulation.run_wildfire(show_simulation_canvas, save_simulation_as_gif)
