import csv
import pprint

pipe_shit_filename = 'discipline_related_skills_2.tsv'
output_shit_filename = 'discipline_related_skills_sorted_2.csv'

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

        row_name = 'row' + str(counter)

        split_skills = skill.split('|')
        for i in range(0, len(split_skills)):
            storage[row_name] = [url, discipline, veriation, level, split_skills[i]]
            print('row', counter, storage[row_name])
            counter = counter + 1

with open(output_shit_filename, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(storage.keys())
    writer.writerows(zip(*storage.values()))

pprint.pprint(storage)

