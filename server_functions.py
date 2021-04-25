def dictionary_to_flask_table(character_dictionary):
    table = []
    # category separator rows
    for categoreies_keys, categories_values in character_dictionary.items():
        row = {'col1': categoreies_keys,
               'col2': "Nothing",
               'col3': "Nothing",
               'col4': "Nothing",
               'col5': "Nothing",
               'col6': "Nothing",}
        table.append(row)
        for types_keys, types_values in categories_values.items():
            row = {'col1': types_keys,
                   'col2': "Nothing",
                   'col3': "Nothing",
                   'col4': "Nothing",
                   'col5': "Nothing",
                   'col6': "Nothing",}
            table.append(row)
            for stats_keys, stats_values in types_values.items():
                row = {'col1': stats_keys,
                       'col2': stats_values,
                       'col3': "Nothing",
                       'col4': "Nothing",
                       'col5': "Nothing",
                       'col6': "Nothing",}
            table.append(row)

    return table


# generate numberred names
    # i = 1
    # name_base = 'row'

# i = i + 1
# name = name_base + str(i)
# table.append(name)
# table.apend(stat)

# result = dictionary_to_flask_table(genreated_char)
# print(result)