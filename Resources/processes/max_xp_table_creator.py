import sys
import pprint
import json
import default_data

generation_based_max_points = default_data.default_generation_based_point_data()
costs = default_data.default_costs_data()

max_xps = {}

def create_max_data(data_type, data_container, nubmer_of_values, costs):
    data_container[data_type] = {}
    discipline_cost_modifier = 1

    if data_type == 'Disciplines':
        cost_infotmation = costs['Disciplines']['Clan_Disciplines'] + discipline_cost_modifier
    else:
        cost_infotmation = costs[data_type]
    
    for generation in range(1, 17):

        data_container[data_type][str(generation)] = 0

        for level in range(1, generation_based_max_points[generation]):

            data_container[data_type][str(generation)] =  data_container[data_type][str(generation)] + (cost_infotmation * level) * nubmer_of_values
            # print(data_container[data_type][str(generation)])
    
    return data_container

# for attributes
create_max_data('Attributes', max_xps, 9, costs)
create_max_data('Skills', max_xps, 27, costs)
create_max_data('Disciplines', max_xps, 5, costs)

# pprint.pprint(max_xps)

with open('flaskr/static/max_xps.json', 'w') as json_file:
    json.dump(max_xps, json_file, indent=4, sort_keys=True)