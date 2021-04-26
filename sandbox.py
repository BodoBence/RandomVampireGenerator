test_dictionary = {'level11': {'level21': 'a',
                               'level22': 'b'},
                    'level12': {'level23': 'x',
                                'level24': 'y'}}

print(test_dictionary)



def stat_block_for_flask_table(number_of_stat_key_value_pairs,
                                dictionary_container):

    stat_lists_container = {}
    for level1 in dictionary_container.keys():
        for i in range(1, number_of_stat_key_value_pairs + 1):
            stat_list_value_name = "keys" + str(i)
            stat_list_key_name = "values" + str(i)
            stat_list_keys = list(dictionary_container[level1].keys())
            stat_list_values = list(dictionary_container[level1].values())
            stat_lists_container[stat_list_value_name] = stat_list_keys
            stat_lists_container[stat_list_key_name] = stat_list_values
    return stat_lists_container
test_case = stat_block_for_flask_table(2, test_dictionary)
print(test_case)


