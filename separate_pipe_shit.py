'''
this shit is ritten to separate bence's pipe shit 
so we can do some other shit tonight
'''

pipe_shit_filename = 'All-Vamp-Data-1-1119-Raw-Data.tsv'
output_shit_filename = 'no_pipe_shit.tsv'

all_parameter_types = []
vamp_data = {}

with open(pipe_shit_filename) as inf: 
    for line in inf:
        if not line.startswith('Name'):
            name, source_url, picture_url, description, parameters, parameter_types =  line.split('\t')

            description = description.replace('No notifications yet.|', '')
            description = description.replace('|', '')
            description = description.replace('\'', ' ')

            vamp_data[name] = {'source_url': source_url, 
                                'picture_url': picture_url,
                                'description': description}

            parameter_types = parameter_types.strip().split('|')
            if '' in parameter_types:
                parameter_types.remove('')
            parameters = parameters.split('|')
            
            for i, parameter_type in enumerate(parameter_types):
                parameter_type = parameter_type.replace(':', '')
                parameter_type = parameter_type[0].upper() + parameter_type[1:]
                parameter = parameters[i]
                vamp_data[name][parameter_type] = parameter
                all_parameter_types.append(parameter_type)

            all_parameter_types = list(set(all_parameter_types))

all_parameter_types.sort()

with open(output_shit_filename, 'w') as outf:
    outf.write('\t'.join(['name', 'source_url', 'picture_url', 'description']))
    for parameter_type in all_parameter_types:
        outf.write(f'\t{parameter_type}')
    outf.write('\n')

    for name, vamp_parameters in vamp_data.items():
        outf.write('\t'.join([name, vamp_parameters['source_url'], vamp_parameters['picture_url'], vamp_parameters['description']]))
        for parameter_type in all_parameter_types:
            if parameter_type not in vamp_parameters:
                outf.write('\tN/A')
            else:
                outf.write(f'\t{vamp_parameters[parameter_type]}')
        outf.write('\n')
                

