import csv
import pprint
import json

def create_discipline_skill_and_ritual_dictionary():
    # read in the csv file
   
    source_file =  'discipline_skills_and_rituals_2.csv'
    discipline_skills_and_rituals = {}

    with open(source_file) as my_data:
        csvreader = csv.reader(my_data, delimiter = ',')
        # fill up a working dicitonary

        for line in csvreader:
            print(line)
            url = line[0] 
            discipline = line[1] 
            variation = line[2]
            level = int(line[3])
            skill_name = line[4]
            skill_description = line[5]

            if discipline in discipline_skills_and_rituals:
                if variation in discipline_skills_and_rituals[discipline]:
                    if level in discipline_skills_and_rituals[discipline][variation]:
                        discipline_skills_and_rituals[discipline][variation][level][skill_name] = skill_description 
                    else:
                        discipline_skills_and_rituals[discipline][variation][level] = {skill_name: skill_description}
                else:
                    discipline_skills_and_rituals[discipline][variation] = {level: {}}
            else:
                discipline_skills_and_rituals[discipline] = {variation: {}}

    with open('WORKINGDICT.json', 'w') as json_file:
        json.dump(discipline_skills_and_rituals, json_file, indent=4, sort_keys=True)

    #return discipline_skills_and_rituals

create_discipline_skill_and_ritual_dictionary()