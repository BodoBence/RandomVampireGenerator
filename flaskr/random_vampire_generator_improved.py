import random
import pprint
import string
from unicodedata import category
import default_data
from dataclasses import dataclass

from default_data import MAX_AGE

@dataclass
class Basic_info:
    name: str
    age: int
    sex: str
    clan: str
    sire: str
    generation: int
    blood_potency: int
    dementation: string

@dataclass
class Social_attributes:

@dataclass
class Physical_attributes:

@dataclass
class Mental_attributes:

@dataclass
class Social_skills:

@dataclass
class Physical_skills:

@dataclass
class Mental_skills:



@dataclass
class Character:
    basic_info: Basic_info
    social_attributes: Social_attributes
    skills: list
    discipllines: list





# uncomment for simluation input testing

# input_values = default_data.start_values()
# input_conditions = default_data.start_conditions()
# input_weights = default_data.start_weights()
# character_sheet = generate(input_values, input_conditions, input_weights)
# pprint.pprint(character_sheet)