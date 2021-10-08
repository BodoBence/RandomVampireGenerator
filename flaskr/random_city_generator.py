import pprint

def gather_inputs():
    inputs = {
        'number_of_vampires': 10,
    }
    return inputs

def generate_citizen():
    generated_citizen = 1
    return generated_citizen

def generate_random_city():
    city_generator_inputs = gather_inputs()
    
    citizens = {}
    for citizen in range(city_generator_inputs['number_of_vampires']):
        citizens[citizen] = generate_citizen()

    return citizens

pprint.pprint(generate_random_city())
        



