from io import StringIO
import json
import re
import pprint

INPUT_SKILLS_CEERMONES_RITUALS = '/Users/benceleventebodo/Documents/github/RandomVampireGenerator/Resources/processes/discipline_skills_rituals_ceremonies.json'

def restructure_skilss():
    with open(INPUT_SKILLS_CEERMONES_RITUALS) as input_file:
        input_dict = json.load(input_file)

        for discipline, discipline_details in input_dict.items():
            for ability, ability_details  in discipline_details.items():
                for level, level_details in ability_details.items():
                    for skill, skill_description in level_details.items():
                        
                        has_metadata = False

                        # check requires
                        if 'Requires' in skill_description:
                            has_metadata = True

                        if 'Amalgam:' in skill_description:
                            has_metadata = True

                        # No requiremnets case
                        # regulate description

                        if not skill_description.endswith('.'):
                            skill_description = f'{skill_description}.'
                        
                        input_dict[discipline][ability][level][skill] = {'Description': skill_description}

                        # Has requiremnets:
                        if has_metadata == True:
                            if 'Requires' in skill_description:
                                input_dict[discipline][ability][level][skill] = {}
                                split_description = skill_description.split('Requires', 1)

                                input_dict[discipline][ability][level][skill]['Description'] = split_description[0]
                                input_dict[discipline][ability][level][skill]['Required_skills'][split_description[1].strip()] = ''
                            
                            if 'Amalgam' in skill_description:
                                split_amalgam_description = input_dict[discipline][ability][level][skill]['Description'].split('Amalgam:', 1)

                                input_dict[discipline][ability][level][skill]['Description'] = split_amalgam_description[0]
 
                                discipline_level = re.findall('\d+', split_amalgam_description[1])
                                re_split_amalgam_description = split_amalgam_description[1].split(discipline_level[0], 1)
                                input_dict[discipline][ability][level][skill]['Required_disciplines'][re_split_amalgam_description[0].strip()] = int(discipline_level[0])
        
        with open('restructured_discipline_skills_rituals_ceremonies.json', 'w') as output_file:
            json.dump(input_dict, output_file, indent=4)


restructure_skilss()
