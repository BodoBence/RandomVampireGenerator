import csv
import pprint

pipe_shit_filename = 'discipline_related_skills.tsv'
output_shit_filename = 'discipline_related_skills_sorted.csv'

with open(pipe_shit_filename) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter = '\t')
    
    storage = {}
    counter = 1

    for line in tsvreader:

        url = line[0] 
        discipline = line[1] 
        level = line[2]
        skill = line[3]

        row_name = 'row' + str(counter)
        storage[row_name] = [url, discipline, level, skill]

        while '|' in storage[row_name][3]:

            split_skills = skill.split('|')
            for i in range(0, len(split_skills)):
                counter = counter + 1
                storage[row_name] = [url, discipline, level, split_skills[i]]

        counter = counter + 1

with open(output_shit_filename, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(storage.keys())
    writer.writerows(zip(*storage.values()))

#pprint.pprint(storage)

