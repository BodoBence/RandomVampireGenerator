import csv
import pprint

pipe_shit_filename = 'discipline_skills_and_rituals_2.csv'
output_shit_filename = 'discipline_skills_and_rituals_3.csv'

with open(pipe_shit_filename) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter = ',')
    
    storage = {}
    counter = 1

    for line in tsvreader:
        url = line[0] 
        discipline = line[1] 
        veriation = line[2]
        level = line[3]
        skill = line[4]
        split_skills = skill.split('|')
        
        for i in range(0, len(split_skills)):
            row_name = 'row' + str(counter)
            storage[row_name] = [url, discipline, veriation, level, split_skills[i]]
            counter = counter + 1

with open(output_shit_filename, "w") as outfile:
    for i in range(1, counter):
        row_name = f'row{i}'
        row_elements = storage[row_name]
        if i == 1:
            row_elements.append('Description')
        else: 
            try:
                name, description = row_elements[-1].split(':', 1)
            except ValueError:
                name = row_elements[-1]
                description = 'N/A'

            row_elements[-1] = name
            row_elements.append(description)

        row = '\t'.join(row_elements)
        outfile.write(f'{row}\n')

# pprint.pprint(storage)

