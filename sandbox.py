#for small stuff

import default_data
import pprint

soemthing = default_data.create_discipline_skill_and_ritual_dictionary()

pprint.pprint(soemthing)

# OUTLINE

if current_category == 'Disciplines':
    if can_upgrade_disciplice == True and can_extend_discipline == True:
        chose_new_discipline_skill(current_stat)
        calculate_xp_cost(current_stat)
        current_xp = current_xp - xp_cost
    else:
        if can_expend_discipline ==True:
            chose_new_discipline_skill(current_stat)
            calculate_xp_cost(current_stat)
            current_xp = current_xp - xp_cost
        else: 
            stagnation_counter = stagnation_counter + 1
else:
    if current_level == maximum_level
        stagnation_counter = stagnation_counter + 1
    else:
        current_xp_cost = calculate_xp_cost(current_stat)
        if current_xp_cost > current_xp:
            level_up(current_stat)
            current_xp = current_xp - current_xp_cost
