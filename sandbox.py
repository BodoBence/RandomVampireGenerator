from default_data import sample_character_sheet


sample_data = sample_character_sheet()

def testing(dictionary_container, number_of_stat_key_value_pairs):

    stat_lists_container = {}
    i = 1
    for level1 in dictionary_container.keys():
        stat_list_value_name = "keys" + str(i)
        stat_list_key_name = "values" + str(i)
        stat_list_keys = list(dictionary_container[level1].keys())
        stat_list_values = list(dictionary_container[level1].values())
        stat_lists_container[stat_list_value_name] = stat_list_keys
        stat_lists_container[stat_list_key_name] = stat_list_values
        print(stat_lists_container)
        i = i+1
    return stat_lists_container

testing(sample_data['Character_Details'], 2)