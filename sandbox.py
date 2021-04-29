import pprint

something = {  'manual_age': 300,
                'manual_age_condition': False,
                'manual_clan': 'Malkavian',
                'manual_clan_condition': True,
                'manual_generation': 10,
                'manual_generation_condition': False,
                'manual_name': 'Default Dampire',
                'manual_name_condition': False,
                'manual_sex': 'Female',
                'manual_sex_condition': False,
                'Attributes': {'Mental_Attributes': 50,
                                'Physical_Attributes': 50,
                                'Social_Attributes': 50},
                'Categories': {'Attributes': 50, 'Disciplines': 50, 'Skills': 50},
                'Disciplines': {'Clan_Disciplines': 50, 'Non-Clan_Disciplines': 50},
                'Skills': {'Mental_Skills': 50, 'Physical_Skills': 50, 'Social_Skills': 50}}

def c(input_data):
    result = {}

    for main_property, detail in input_data.items():
        if isinstance(detail, dict):
            for sub_property, sub_detail in detail.items():
                result[sub_property] = sub_detail
        else:
            result[main_property] = detail

    return result


pprint.pprint(input_form_to_field(something))