from io import StringIO
import json
import pprint

INPUT_SKILLS_CEERMONES_RITUALS = '/Users/benceleventebodo/Documents/github/RandomVampireGenerator/Resources/processes/discipline_skills_rituals_ceremonies.json'

def restructure_skilss():
    with open(INPUT_SKILLS_CEERMONES_RITUALS) as input_file:
        input_dict = json.load(input_file)

        for discipline, discipline_details in input_dict.items():
            for ability, ability_details  in discipline_details.items():
                for level, level_details in ability_details.items():
                    for skill, skill_description in level_details.items():

                        working_description = skill_description
                        input_dict[discipline][ability][level][skill] = {}

                        if 'Requires' not in working_description:
                            input_dict[discipline][ability][level][skill]['Description'] = skill_description
                        else:
                            split_description = working_description.split('Requires', 1)

                            input_dict[discipline][ability][level][skill]['Description'] = split_description[0]
                            input_dict[discipline][ability][level][skill]['Required_skill'] = split_description[1]
                            skill_level = [int(i) for i in split_description[1].split(i) if i.isdigit()]
                            input_dict[discipline][ability][level][skill]['Required_skill_level'] = skill_level[0]

                        if 'Amalgam:' in working_description:
                            resplit_description = input_dict[discipline][ability][level][skill]['Description'].split('Amalgam:', 1)

                            input_dict[discipline][ability][level][skill]['Description'] = resplit_description[0]
                            input_dict[discipline][ability][level][skill]['Required_discipline'] = resplit_description[1]

                        if  'Required_skill' not in input_dict[discipline][ability][level][skill].keys():
                            input_dict[discipline][ability][level][skill]['Required_skill'] = 'N/A'
                            input_dict[discipline][ability][level][skill]['Required_skill_level'] = 'N/A'
                        
                        if  'Required_discipline' not in input_dict[discipline][ability][level][skill].keys():
                            input_dict[discipline][ability][level][skill]['Required_discipline'] = 'N/A'
                            input_dict[discipline][ability][level][skill]['Required_discipline_level'] = 'N/A'

        
        with open('restructured_discipline_skills_rituals_ceremonies.json', 'w') as output_file:
            json.dump(input_dict, output_file, indent=4)


restructure_skilss()
