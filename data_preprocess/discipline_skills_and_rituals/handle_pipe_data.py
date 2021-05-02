import csv
import pprint

pipe_shit_filename = 'scraped_discipline_skills_and_rituals.tsv'
output_shit_filename = 'discipline_skills_and_rituals_1.csv'

with open(pipe_shit_filename) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter = '\t')
    
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
        row = '\t'.join(storage[row_name])
        outfile.write(f'{row}\n')

# pprint.pprint(storage)

